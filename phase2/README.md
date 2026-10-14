# Phase 2 — Application Containerization & Amazon ECR Deployment

## 1. Executive Summary & Overview
Phase 2 transitions the ZeetaFin Enterprise Resource Planning (ERP) platform from source code into hardened, production-ready, multi-stage Docker container images, verified locally via Docker Compose and prepared for deployment to Amazon Elastic Container Registry (Amazon ECR).

```text
[ Developer Machine ]
        │
        ├──► phase2/backend  ──(Multi-stage Dockerfile)──► zeetafin-backend:local  (369 MB)
        ├──► phase2/frontend ──(Standalone Dockerfile) ──► zeetafin-frontend:local (224 MB)
        └──► docker-compose.yml ──► [ Local Verification Stack ]
                                         │── zeetafin-db (PostgreSQL 16)
                                         │── zeetafin-backend (NestJS :3001)
                                         └── zeetafin-frontend (Next.js :3000)
                                         │
                                         ▼
                            [ Amazon ECR (us-east-1) ]
```

---

## 2. Architecture & Tech Stack Analysis

| Layer | Service | Framework / Engine | Port | Base Image | Security Context |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Frontend** | `zeetafin-frontend` | Next.js 14, React 18, Tailwind CSS | `3000` | `node:20-alpine` | Non-root (`nextjs:nodejs`, UID 1001) |
| **Backend** | `zeetafin-backend` | NestJS 10, TypeORM, Swagger, Passport JWT | `3001` | `node:20-alpine` | Non-root (`node`, UID 1000) |
| **Database** | `zeetafin-db` | PostgreSQL 16 | `5432` | `postgres:16-alpine` | Dedicated postgres user |

---

## 3. DevOps Containerization Strategy

### A. Backend (`backend/Dockerfile`)
* **Multi-stage Build Pipeline:**
  1. `deps`: Resolves full dependency tree via `npm ci`.
  2. `builder`: Compiles TypeScript source code to native JavaScript in `dist/`.
  3. `runner`: Ultra-lightweight runtime containing only production dependencies (`npm ci --omit=dev`) and compiled code.
* **Security:** Runs as non-root user `node`.
* **Healthcheck:** Automated `wget` probe against `http://localhost:3001/api/docs`.

### B. Frontend (`frontend/Dockerfile`)
* **Next.js Standalone Build:** Leverages `output: 'standalone'` in Next.js configuration to bundle only necessary node modules directly into `.next/standalone`.
* **Layer Caching:** Isolates dependency installation (`package.json` + `package-lock.json`) before copying application code.
* **Security:** Custom non-root system user and group (`nextjs:nodejs`).
* **Healthcheck:** Automated HTTP spider against `http://localhost:3000/`.

---

## 4. Repository Structure

```text
phase2/
├── backend/
│   ├── src/                    # NestJS controllers, services, entities, DTOs
│   ├── .dockerignore           # Excludes node_modules, dist, .env, git
│   ├── Dockerfile              # Production multi-stage Docker build
│   └── package.json
├── frontend/
│   ├── app/                    # Next.js 14 App Router pages
│   ├── components/             # Reusable UI components
│   ├── .dockerignore           # Excludes node_modules, .next, .env, git
│   ├── Dockerfile              # Standalone multi-stage Docker build
│   └── package.json
├── docker-compose.yml          # Local multi-service orchestration
└── README.md                   # Operational guide & verification evidence
```

---

## 5. Local Orchestration & Verification

### Running the Full Stack
```bash
docker compose up -d
```

### Verification Endpoints
* **Frontend Web Application:** [http://localhost:3000](http://localhost:3000)
* **Backend REST API:** [http://localhost:3001/api](http://localhost:3001/api)
* **Backend Swagger API Documentation:** [http://localhost:3001/api/docs](http://localhost:3001/api/docs)
* **PostgreSQL Database:** `localhost:5432` (`db: zeetafin`, `user: postgres`)

---

## 6. Amazon ECR Deployment Guide

### 1. Authenticate Docker CLI to Amazon ECR
```bash
aws ecr get-login-password --region us-east-1 --profile phase1 | docker login --username AWS --password-stdin 672061768969.dkr.ecr.us-east-1.amazonaws.com
```

### 2. Create ECR Repositories (if not already created)
```bash
aws ecr create-repository --repository-name zeetafin-backend --region us-east-1 --profile phase1
aws ecr create-repository --repository-name zeetafin-frontend --region us-east-1 --profile phase1
```

### 3. Tag Docker Images for ECR
```bash
docker tag zeetafin-backend:local 672061768969.dkr.ecr.us-east-1.amazonaws.com/zeetafin-backend:latest
docker tag zeetafin-frontend:local 672061768969.dkr.ecr.us-east-1.amazonaws.com/zeetafin-frontend:latest
```

### 4. Push to Amazon ECR
```bash
docker push 672061768969.dkr.ecr.us-east-1.amazonaws.com/zeetafin-backend:latest
docker push 672061768969.dkr.ecr.us-east-1.amazonaws.com/zeetafin-frontend:latest
```
