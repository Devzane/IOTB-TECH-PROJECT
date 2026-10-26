# Phase 3 — CI/CD Pipeline for Automated AWS Application Deployment

## 1. Executive Summary & Objective

Phase 3 delivers an enterprise-grade Continuous Integration and Continuous Deployment (CI/CD) pipeline using **GitHub Actions**, **Amazon Elastic Container Registry (Amazon ECR)**, and **Amazon EC2**. 

When a developer pushes changes to the repository, the automated pipeline:
1. Validates and checks out the application code.
2. Builds optimized multi-stage Docker images for both the NestJS backend and Next.js frontend.
3. Authenticates with AWS and pushes immutable SHA-tagged and `latest`-tagged images to Amazon ECR.
4. Securely connects to the hardened Phase 1 EC2 instance over SSH using secrets stored in GitHub Secrets.
5. Deploys the updated containers, replacing older instances with zero port collision and zero orphaned resources.
6. Executes local and external availability smoke tests before declaring the deployment successful.

---

## 2. Architecture & Deployment Workflow

```mermaid
sequenceDiagram
    autonumber
    actor Dev as 🧑‍💻 Developer
    participant GH as 🐙 GitHub Repository
    participant GHA as ⚙️ GitHub Actions Runner
    participant ECR as 📦 Amazon ECR
    participant EC2 as 🖥️ AWS EC2 Server
    actor User as 🌍 End User / Browser

    Dev->>GH: git push origin main
    GH->>GHA: Trigger .github/workflows/deploy.yml
    activate GHA
    GHA->>GHA: Checkout code & setup Docker Buildx
    GHA->>ECR: Authenticate & push zeetafin-backend (SHA & latest)
    GHA->>ECR: Authenticate & push zeetafin-frontend (SHA & latest)
    GHA->>EC2: SSH Connection & sync deploy manifests
    activate EC2
    EC2->>ECR: Authenticate & pull new images
    EC2->>EC2: docker compose up -d --force-recreate
    EC2->>EC2: Run internal health checks (3001 & 3000)
    EC2-->>GHA: Deployment exit code 0 (Healthy)
    deactivate EC2
    GHA->>EC2: External HTTP smoke test (:3000)
    GHA-->>GH: Pipeline Status: SUCCESS (Green checkmark)
    deactivate GHA
    User->>EC2: Access Web UI (http://<EC2_IP>:3000)
```

### High-Level Architecture Diagram

```mermaid
graph TD
    subgraph GitHub ["🐙 GitHub Environment"]
        Repo["Git Repository\n(main branch)"]
        Secrets["🔐 GitHub Secrets\n- AWS Keys\n- EC2 Host & SSH Key"]
        Actions["⚙️ GitHub Actions Workflow\n(.github/workflows/deploy.yml)"]
        Repo --> Actions
        Secrets -.-> Actions
    end

    subgraph AWS ["☁️ Amazon Web Services (us-east-1)"]
        subgraph ECR ["📦 Amazon Elastic Container Registry"]
            ECR_BE["zeetafin-backend:latest / SHA"]
            ECR_FE["zeetafin-frontend:latest / SHA"]
        end

        subgraph VPC ["🔲 AWS VPC (10.0.0.0/16)"]
            subgraph EC2_INST ["🖥️ EC2 Deployment Target (Ubuntu 24.04 LTS)"]
                DeployEngine["🚀 deploy.sh Engine"]
                Compose["📄 docker-compose.prod.yml"]
                
                subgraph DockerRuntime ["🐳 Docker CE Engine"]
                    DB_C["🗄️ zeetafin-db-prod\n(PostgreSQL 16)"]
                    BE_C["⚙️ zeetafin-backend-prod\n(:3001)"]
                    FE_C["🌐 zeetafin-frontend-prod\n(:3000)"]
                    DB_C <--> BE_C
                    BE_C <--> FE_C
                end
            end
        end
    end

    Actions -- "1. Build & Push Images" --> ECR
    Actions -- "2. SSH & Trigger Deployment" --> DeployEngine
    DeployEngine --> Compose
    Compose -- "3. Pull Images" --> ECR
    Compose --> DockerRuntime
```

---

## 3. GitHub Secrets Configuration

All sensitive credentials and host targets are strictly managed using **GitHub Encrypted Secrets** (`Settings -> Secrets and variables -> Actions`). No credentials or IP addresses are hardcoded into workflow manifests.

| Secret Name | Required | Description | Example / Recommended Source |
| :--- | :--- | :--- | :--- |
| `AWS_ACCESS_KEY_ID` | **Yes** | AWS IAM Access Key with ECR push/pull permissions | IAM User: `zeetafin-ci-cd-bot` |
| `AWS_SECRET_ACCESS_KEY` | **Yes** | AWS IAM Secret Access Key | IAM Secret Key |
| `AWS_REGION` | **Yes** | Target AWS Region hosting ECR repositories | `us-east-1` |
| `EC2_HOST` | **Yes** | Public IP address or Elastic IP of the EC2 instance | `54.210.xx.xx` (from Phase 1 Terraform output) |
| `EC2_USERNAME` | **Yes** | SSH user login for the EC2 operating system | `ubuntu` |
| `EC2_SSH_KEY` | **Yes** | OpenSSH Private Key corresponding to instance key pair | Output from Phase 1 (`phase1-key.pem`) |

> [!SECURITY]
> **Least Privilege Principle:** The IAM user credentials supplied to GitHub Secrets must only possess the `AmazonEC2ContainerRegistryPowerUser` managed policy (or custom policy restricted to `zeetafin-*` repository ARNs), preventing unauthorized access to other AWS infrastructure.

---

## 4. EC2 Infrastructure Preparation

To allow GitHub Actions to deploy and allow users to access the application, ensure the Phase 1 Security Group permits required ingress traffic:

1. **SSH Port 22:** Ingress allowed from GitHub Actions runner IP or operator `/32` (or open to `0.0.0.0/0` if utilizing runner pools without fixed IP ranges).
2. **Frontend Port 3000:** Ingress allowed from `0.0.0.0/0` (Web UI access).
3. **Backend API Port 3001:** Ingress allowed from `0.0.0.0/0` (REST API & Swagger docs).

### Host Directory Layout on EC2
```text
/home/ubuntu/zeetafin-app/
├── docker-compose.prod.yml    # Production container definitions
├── .env                       # Host-specific environment configuration
└── scripts/
    ├── deploy.sh              # Idempotent container rollout engine
    └── healthcheck.sh         # Endpoint verification utility
```

---

## 5. Container Replacement & Zero-Collision Mechanics

A critical requirement of Phase 3 is ensuring that **old application containers are cleanly replaced when new versions are deployed**.

The deployment engine (`phase3/scripts/deploy.sh`) implements this using Docker Compose native reconciliation:

```bash
docker compose -f docker-compose.prod.yml pull
docker compose -f docker-compose.prod.yml up -d --remove-orphans --force-recreate
```

### Why this guarantees zero collision and zero downtime:
1. **Parallel Image Pulling:** Docker downloads the new image layers from ECR in the background *while the old container continues serving traffic*.
2. **Atomic Replacement (`--force-recreate`):** Docker Compose creates the replacement container, atomically switches port bindings (`3000:3000` and `3001:3001`), and stops/removes the outdated container without name collisions.
3. **Orphan Removal (`--remove-orphans`):** Any deprecated services from prior revisions are automatically dismantled.
4. **Volume Preservation:** PostgreSQL database state stored in `zeetafin_prod_pgdata` persists across container updates.
5. **Disk Hygiene:** Obsolete dangling images are cleaned up via `docker image prune -f --filter "until=24h"`.

---

## 6. Pipeline Execution Walkthrough

### Triggering via Git Push
Any commit pushed to `main` modifying application code automatically initiates the workflow:
```bash
git checkout main
git add phase2/backend/src/app.service.ts
git commit -m "feat: update enterprise invoice generator"
git push origin main
```

### Manual Trigger (`workflow_dispatch`)
The workflow can also be triggered manually on demand via the GitHub Actions UI with custom image tag overrides.

### Expected Pipeline Steps:
```text
✓ Checkout Application Code               [1s]
✓ Set Image Tag                           [0s]
✓ Set up Docker Buildx                    [3s]
✓ Authenticate with AWS                   [1s]
✓ Log in to Amazon ECR                    [2s]
✓ Build & Push Backend Container Image    [45s]
✓ Build & Push Frontend Container Image   [55s]
✓ Configure Secure SSH Key                [1s]
✓ Sync Production Manifests to EC2        [3s]
✓ Execute Deployment & Rollout on EC2     [28s]
✓ Automated External Availability Check   [5s]
```

---

## 7. Phase 3 Verification Evidence & Deliverables Gallery

Below is the complete visual evidence proving end-to-end CI/CD automation, secure secret management, container image publication to Amazon ECR, zero-collision deployment on Amazon EC2, automated smoke verification, and live production application access.

### Verification Commands on EC2
Connect to the server to verify running containers:
```bash
ssh -i phase1-key.pem ubuntu@<EC2_PUBLIC_IP>

# Check running production containers
cd /home/ubuntu/zeetafin-app
docker compose -f docker-compose.prod.yml ps

# Execute automated health check
./scripts/healthcheck.sh 127.0.0.1
```

Expected output:
```text
NAME                     IMAGE                                                  COMMAND                  SERVICE    CREATED          STATUS                    PORTS
zeetafin-backend-prod    123456789012.dkr.ecr.us-east-1.amazonaws.com/...      "docker-entrypoint.s…"   backend    45 seconds ago   Up 44 seconds (healthy)   0.0.0.0:3001->3001/tcp
zeetafin-db-prod         postgres:16-alpine                                     "docker-entrypoint.s…"   db         2 minutes ago    Up 2 minutes (healthy)    0.0.0.0:5432->5432/tcp
zeetafin-frontend-prod   123456789012.dkr.ecr.us-east-1.amazonaws.com/...      "docker-entrypoint.s…"   frontend   45 seconds ago   Up 44 seconds (healthy)   0.0.0.0:3000->3000/tcp
```

---

### Deliverable 1: GitHub Encrypted Secrets Configuration
Proof that AWS IAM access keys, target EC2 host IP, SSH username, and OpenSSH private key are registered securely in GitHub Secrets:

![GitHub Secrets Configuration](docs/images/github-secrets.png)

---

### Deliverable 2: Automated End-to-End GitHub Actions Pipeline Execution
Proof of a 100% green pipeline run executing buildx multi-stage compilation, Amazon ECR publication, SSH deployment to EC2, and external automated smoke testing:

![GitHub Actions Success Pipeline](docs/images/github-actions-success.png)

---

### Deliverable 3: Amazon ECR Private Container Repositories (`zeetafin-backend`)
Proof of backend images pushed to Amazon ECR with immutable commit SHA tags and `latest` pointer, including automated vulnerability scan results:

![ECR Backend Repositories and Images](docs/images/ecr-backend-images.png)

---

### Deliverable 4: Amazon ECR Private Container Repositories (`zeetafin-frontend`)
Proof of frontend Next.js standalone container images pushed to Amazon ECR with commit SHA tags and `latest` pointer:

![ECR Frontend Repositories and Images](docs/images/ecr-frontend-images.png)

---

### Deliverable 5: Production Multi-Container Rollout on EC2 (`docker compose ps`)
Proof of running production containers (`zeetafin-db-prod`, `zeetafin-backend-prod`, and `zeetafin-frontend-prod`) on the EC2 instance, all healthy with zero port collision:

![EC2 Production Docker Compose Status](docs/images/ec2-docker-compose-ps.png)

---

### Deliverable 6: Automated External Smoke & Health Check
Proof of the post-deployment curl verification probe confirming HTTP 200 OK availability on the live public endpoints:

![External Smoke Check](docs/images/external-smoke-check.png)

---

### Deliverable 7: Live Web Application Production UI (`http://<EC2_PUBLIC_IP>:3000`)
Proof of the Next.js 14 ERP frontend accessible via browser over the public internet on EC2 port 3000:

![Live Frontend Web UI on EC2](docs/images/live-frontend-public-ip.png)

---

### Deliverable 8: Live Backend REST API & Swagger Explorer (`http://<EC2_PUBLIC_IP>:3001/api/docs`)
Proof of the interactive OpenAPI Swagger documentation running live on EC2 port 3001:

![Live Backend Swagger Docs on EC2](docs/images/live-backend-swagger-public-ip.png)

---

## 8. Troubleshooting Guide

| Issue / Error Message | Root Cause | Remediation Step |
| :--- | :--- | :--- |
| `Permission denied (publickey)` in SSH step | Invalid SSH private key or incorrect `EC2_USERNAME` | Verify `EC2_SSH_KEY` includes complete `-----BEGIN RSA PRIVATE KEY-----` and `-----END RSA PRIVATE KEY-----` headers without trailing spaces. Ensure user is `ubuntu`. |
| `Cannot connect to the Docker daemon` on EC2 | Docker service inactive or user not in `docker` group | Run `sudo systemctl restart docker` and ensure `sudo usermod -aG docker ubuntu` was applied in Phase 1 Ansible playbook. |
| `no basic auth credentials` during ECR pull on EC2 | Expired ECR Docker login authorization token | The `deploy.sh` script automatically runs `aws ecr get-login-password`. Ensure AWS CLI credentials or IAM instance profile are valid. |
| `port is already allocated` | Stale orphan container binding ports 3000 or 3001 | Run `docker rm -f $(docker ps -aq)` on EC2 or ensure `--remove-orphans --force-recreate` is enabled in `docker compose up`. |
| External Smoke Test Timeout | Security Group blocking port 3000 | Add an inbound Security Group rule allowing TCP port 3000 from `0.0.0.0/0`. |
