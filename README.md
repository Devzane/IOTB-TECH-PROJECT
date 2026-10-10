# Phase 1: EC2 + Docker

## Overview

Provisions an AWS EC2 instance (Ubuntu 24.04 LTS) with Terraform and configures it with Ansible. The Ansible docker role installs Docker CE from the official Docker apt repository, starts the service, and verifies operation with `docker run hello-world`. This is Phase 1 of a three-phase portfolio project:

- Phase 1 (this repo): Provision EC2, install Docker.
- Phase 2: Build a Docker image, push it to Amazon ECR, pull and run it on EC2.
- Phase 3: GitHub Actions pipeline automates the full build-push-deploy cycle.

## Architecture

```
Your machine
    |
    | SSH (port 22, your IP only)
    v
[EC2 t3.micro] ── public subnet (10.0.1.0/24)
    |                  |
    |             [Internet Gateway]
    |                  |
    |             [Route Table: 0.0.0.0/0 -> IGW]
    |
[Docker daemon]
[hello-world container]

VPC: 10.0.0.0/16
Security Group: ingress SSH/22 from your IP/32, egress all
IAM Role: EC2 trust policy, no policies attached (Phase 1 needs no AWS API access)
EBS: 20 GiB gp3, encrypted
IMDSv2: required
```

## Prerequisites

| Requirement | Version | Notes |
|---|---|---|
| Terraform | >= 1.7 | `terraform version` |
| AWS CLI | >= 2.x | `aws --version` |
| Ansible | >= 2.14 | `ansible --version` |
| Python | >= 3.9 | On the control machine |
| AWS profile `phase1` | — | `aws configure --profile phase1` |

Your AWS profile needs permissions to create: VPC, subnets, IGW, route tables, security groups, key pairs, IAM roles/instance profiles, EC2 instances, EBS volumes.

## Setup

### 1. Generate SSH key pair

```bash
ssh-keygen -t ed25519 -f ~/.ssh/phase1-key -C "phase1-ec2"
# Do not add a passphrase if you want non-interactive Ansible runs.
# The private key stays local. Terraform reads only the .pub file.
```

### 2. Find your public IP

```bash
curl -s ifconfig.me
# Note the output, e.g. 203.0.113.5 — you will use it as 203.0.113.5/32
```

### 3. Configure AWS CLI profile

```bash
aws configure --profile phase1
# Enter: Access Key ID, Secret Access Key, region (us-east-1), output format (json)
```

### 4. Create your tfvars file

```bash
cd phase1/
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars — fill in my_ip with YOUR_IP/32
```

## Run Order

Run every command from inside the `phase1/` directory unless stated otherwise.

### Step 1: Format check

```bash
terraform fmt -check -recursive
```

Expected: exit 0, no output. If files are reformatted, run `terraform fmt` (without `-check`) and re-run with `-check`.

### Step 2: Validate

```bash
terraform init
terraform validate
```

Expected: `Success! The configuration is valid.`

### Step 3: Plan

```bash
terraform plan -out=tfplan
```

Review the plan. You should see approximately 11 resources to create. Confirm the AMI name shown in the plan contains `noble-24.04`.

### Step 4: Apply

```bash
terraform apply tfplan
```

Expected: `Apply complete! Resources: 11 added, 0 changed, 0 destroyed.`

Note the outputs:

```
ami_id       = "ami-0xxxxxxxxxxxxxxxxx"
ami_name     = "ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-..."
instance_id  = "i-0xxxxxxxxxxxxxxxxx"
public_ip    = "x.x.x.x"
ssh_command  = "ssh -i ~/.ssh/phase1-key ubuntu@x.x.x.x"
```

### Step 5: Verify the inventory was generated

```bash
cat ansible/inventory/hosts.ini
```

Expected: a valid ini file with the public IP from the Terraform output.

### Step 6: Test SSH connectivity (manual check)

```bash
# Copy the ssh_command from Terraform output and run it
ssh -i ~/.ssh/phase1-key ubuntu@<public_ip>
exit
```

[INSERT SCREENSHOT: Terminal showing successful SSH login to the EC2 instance, including the Ubuntu 24.04 welcome banner]

### Step 7: Ansible connectivity test

```bash
cd ansible/
ansible webservers -m ansible.builtin.ping
```

Expected:

```
phase1-dev | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

[INSERT SCREENSHOT: Terminal showing ansible ping returning SUCCESS]

### Step 8: Syntax check

```bash
ansible-playbook playbooks/site.yml --syntax-check
```

Expected: `playbook: playbooks/site.yml` with no errors.

### Step 9: Dry run (check mode)

```bash
ansible-playbook playbooks/site.yml --check
```

Note: check mode will report failures on tasks that require earlier tasks to have actually run (for example, the apt_repository task will fail in check mode if the prerequisites package task was skipped). This is expected. Check mode here validates syntax and task structure, not idempotency.

### Step 10: Real run

```bash
ansible-playbook playbooks/site.yml
```

A successful first run ends with a play recap showing no failures:

```
PLAY RECAP
phase1-dev : ok=N  changed=N  unreachable=0  failed=0  skipped=0
```

[INSERT SCREENSHOT: Full terminal output of the ansible-playbook run showing PLAY RECAP with failed=0]

### Step 11: Verify Docker on the instance

```bash
ssh -i ~/.ssh/phase1-key ubuntu@<public_ip> "docker --version && docker info | head -5"
```

[INSERT SCREENSHOT: Terminal showing docker --version and docker info output from the EC2 instance]

### Step 12: Idempotency check (second run)

```bash
ansible-playbook playbooks/site.yml
```

Expected outcome: all tasks except `Verify Docker is functional by running hello-world` report `ok` (not `changed`). The hello-world task will always report `changed=1` because `docker run` is a command with no idempotency check. This is documented in the task itself.

[INSERT SCREENSHOT: Second ansible-playbook run PLAY RECAP showing changed=1 (hello-world only), failed=0]

## How to Destroy

```bash
# From phase1/
terraform destroy
```

Terraform will show a plan of all 11 resources to be destroyed. Type `yes` to confirm. This terminates the EC2 instance, deletes the VPC and all network resources, and deregisters the key pair. The local `terraform.tfstate` file is updated accordingly.

[INSERT SCREENSHOT: Terminal showing terraform destroy complete]

## Cost Notes

All resources are within the AWS free tier under normal usage:

| Resource | Free tier limit | This project |
|---|---|---|
| EC2 t2.micro / t3.micro | 750 hrs/month (first 12 months) | 1 instance |
| EBS gp2/gp3 | 30 GiB/month | 20 GiB |
| Data transfer out | 1 GB/month | Near zero |
| Elastic IP | Free if attached | Not used |

Estimated cost if left running continuously after the free tier period: approximately $8-10/month for a t3.micro in us-east-1. Destroy when not in use with `terraform destroy`.

## Design Decisions and Trade-offs

### Flat Terraform layout vs. modules

Phase 1 uses a single flat `main.tf` rather than reusable modules. The rationale: at this scale (one instance, one environment), the indirection of modules adds reading cost without meaningful reuse benefit. Phases 2 and 3 will refactor toward modules as the networking and compute layers diverge in requirements.

Trade-off: if you need a second environment today, you would duplicate the flat config. With modules, you would call the same module twice. The correct time to extract a module is when you need a second caller.

### No remote state backend

Phase 1 uses local state to reduce bootstrap complexity (no S3 bucket, no DynamoDB, no separate apply step). This means only one person can safely run Terraform at a time and the state file must not be committed to git.

Trade-off: local state is not shareable and is lost if your machine is lost. Phase 2 adds an S3 remote backend.

### Ansible inventory generated by Terraform

`templatefile()` writes `hosts.ini` from Terraform outputs after every apply. This eliminates the manual step of copying an IP address between tools. The generated file is gitignored so it is never stale in the repository.

Trade-off: if you run Ansible without a fresh `terraform apply` (for example, after an instance stop/start that changes the public IP), the inventory is stale. The fix is to re-run `terraform apply` (which is a no-op for infrastructure but regenerates the inventory file) or to use an Elastic IP.

### No provisioners

Terraform provisioners (`remote-exec`, `local-exec`) are an anti-pattern for configuration management. They run only on resource creation, do not appear in plans, cannot be re-run without destroying the resource, and produce no Terraform-managed state. Ansible is run manually after `terraform apply`. This clean separation means infrastructure and configuration can be iterated independently.

### IMDSv2 required

`http_tokens = "required"` in the metadata_options block enforces the newer Instance Metadata Service v2, which requires a session token. IMDSv1, which allows any process to query instance metadata via a plain HTTP GET, is a known SSRF escalation path. Requiring v2 closes that path.

### IAM role with no policies

Phase 1 attaches an empty IAM role to the instance. The instance makes no AWS API calls, so no permissions are needed. The role exists so Phase 2 (ECR pull) can attach `AmazonEC2ContainerRegistryReadOnly` without modifying the instance. Granting no permissions by default is correct least-privilege practice.

### docker run hello-world is not idempotent

The verification task uses `ansible.builtin.command`, which Ansible cannot assess without running. It will always report `changed=1`. The alternative is to use `community.docker.docker_container`, which requires installing an extra Ansible collection and the `docker` Python SDK on the control machine. For Phase 1, the command module is the simpler choice. The task is clearly commented.

### host_key_checking = False

Disabling SSH host key verification is a security risk (man-in-the-middle). It is acceptable in this lab context because instances are frequently destroyed and recreated, making it impractical to maintain a known_hosts file. In production, pre-populate known_hosts using `ssh-keyscan` or AWS Systems Manager Session Manager, and set `host_key_checking = True`.
