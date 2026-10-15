# IOTB DevOps Engineering Projects

A structured, multi-phase enterprise DevOps repository demonstrating cloud infrastructure automation, containerization, registry distribution, and orchestration.

---

## Project Roadmap & Phases

| Phase | Title | Tech Stack | Status | Documentation |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 1** | **Cloud Infrastructure & Configuration Automation** | Terraform, Ansible, AWS EC2, Ubuntu 24.04, Docker CE | Completed | [Phase 1 Documentation](./phase1/README.md) |
| **Phase 2** | **Application Containerization & Amazon ECR Deployment** | Docker, Docker Compose, NestJS, Next.js, PostgreSQL, Amazon ECR | In Progress | [Phase 2 Documentation](./phase2/README.md) |
| **Phase 3** | ** Automated CI/CD Pipeline** |  GitHub Actions | Upcoming | [Phase 3 Documentation](./phase3/README.md) |

---

## Repository Structure

```text
.
├── phase1/                       # Infrastructure as Code & Configuration Management
│   ├── ansible/                  # Ansible playbooks and modular roles (Docker CE)
│   ├── docs/                     # Architecture diagrams and execution evidence
│   ├── main.tf                   # Terraform root module (VPC, Subnet, SG, EC2, IAM)
│   ├── outputs.tf                # Infrastructure output values
│   ├── variables.tf              # Configurable input variables
│   └── README.md                 # Complete Phase 1 operational documentation
├── phase2/                       # Application Containerization & ECR Deployment
│   ├── backend/                  # NestJS TypeScript REST API + Multi-stage Dockerfile
│   ├── frontend/                 # Next.js 14 Standalone App + Production Dockerfile
│   ├── docker-compose.yml        # Local multi-service stack (Postgres + Backend + Frontend)
│   └── README.md                 # Phase 2 containerization & ECR operational guide
├── phase3/                       # Container Orchestration & CI/CD Deployment
│   └── README.md                 # Phase 3 planned architecture & deployment guide
├── AGENTS.md                     # Engineering standards & conventional commit rules
└── README.md                     # Project portfolio root documentation
```

---

## Phase Summaries

### [Phase 1: Cloud Infrastructure & Configuration Management](./phase1/README.md)
* **Goal:** Automated provisioning of a secure AWS EC2 host using Terraform and programmatic installation of Docker Engine using Ansible.
* **Key Achievements:**
  * Provisioned modular AWS VPC, Internet Gateway, public subnet, and stateful security groups.
  * Enforced SSH key-based access and automated dynamic Ansible inventory generation.
  * Executed modular Ansible playbooks installing official Docker CE and verified with the test container.

### [Phase 2: Application Containerization & Amazon ECR Deployment](./phase2/README.md)
* **Goal:** Multi-tier containerization of the ZeetaFin ERP application suite, local verification via Docker Compose, and artifact publication to Amazon Elastic Container Registry (ECR).
* **Key Achievements:**
  * Architected multi-stage Docker builds for NestJS API (`zeetafin-backend`) and Next.js Frontend (`zeetafin-frontend`).
  * Implemented non-root security context (`USER node` and `USER nextjs`) and strict `.dockerignore` filters.
  * Orchestrated local testing environment via `docker-compose.yml` with health checks against PostgreSQL.
  * Prepared Amazon ECR repository structure for container distribution.
