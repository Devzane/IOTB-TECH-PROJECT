#!/usr/bin/env python3
import os
from generate_labs import COMMON_CSS, COMMON_SCRIPT, generate_navbar

def get_part1_html():
    nav = generate_navbar(1)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>AWS IAM, Amazon ECR &amp; GitHub Secrets — ZeetaFin Phase 3 Lab Part 1</title>
<meta name="description" content="Part 1 of the ZeetaFin Phase 3 CI/CD Lab: configure least-privilege IAM credentials, Amazon ECR container registries, and hardened GitHub Secrets.">
<meta name="color-scheme" content="light dark">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,700;1,9..40,400&family=JetBrains+Mono:wght@400;500;700&family=Sora:wght@500;600;700;800&display=swap" rel="stylesheet">
<style>
{COMMON_CSS}
</style></head><body>
<div class="progress"><i></i></div>

<!-- ===== HERO ===== -->
<header class="hero"><div class="wrap">
{nav}

<h1>AWS IAM, Amazon ECR &amp; GitHub Secrets Hardening</h1>
<p class="dek">Architecting the zero-trust CI/CD authentication boundary: configuring least-privilege IAM bot users, provisioning AES-256 encrypted Amazon ECR registries with vulnerability scanning, and managing encrypted GitHub Secrets.</p>

<p class="meta">
  <span><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> Oct 2026</span>
  <span><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> ~45 min read</span>
  <span><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a4 4 0 0 0 5 5L21 12.6a2 2 0 0 1 0 2.8l-5.6 5.6a2 2 0 0 1-2.8 0L3 11.4a2 2 0 0 1 0-2.8L8.6 3a2 2 0 0 1 2.8 0z" transform="translate(0 0) scale(.9) translate(1.3 1.3)"/></svg> ~50 min hands-on</span>
  <span><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v16H6.5A2.5 2.5 0 0 0 4 21.5z"/><path d="M4 18.5A2.5 2.5 0 0 1 6.5 16H20"/></svg> AWS IAM, Amazon ECR, GitHub Actions Secrets</span>
</p>

<div class="tools">
  <span class="tool">🔐 AWS IAM Least Privilege</span>
  <span class="tool">📦 Amazon ECR Repositories</span>
  <span class="tool">🛡️ GitHub Encrypted Secrets</span>
  <span class="tool">🔍 ECR Scan on Push</span>
</div>

<div class="hero-art">
<svg viewBox="0 0 1080 340" role="img" aria-label="AWS IAM and ECR Credential Architecture">
  <defs>
    <linearGradient id="g-gh" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#1e293b"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <linearGradient id="g-iam" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#312e81"/><stop offset="100%" stop-color="#1e1b4b"/></linearGradient>
    <linearGradient id="g-ecr" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#064e3b"/><stop offset="100%" stop-color="#022c22"/></linearGradient>
    <marker id="arr-c1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 1 L 10 5 L 0 9 z" fill="#818cf8"/></marker>
    <marker id="arr-c4" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 1 L 10 5 L 0 9 z" fill="#34d3b4"/></marker>
  </defs>

  <!-- GitHub Boundary -->
  <rect x="40" y="30" width="340" height="280" rx="16" fill="url(#g-gh)" stroke="#475569" stroke-width="2"/>
  <text x="60" y="65" fill="#f8fafc" font-family="Sora, sans-serif" font-size="15" font-weight="700">🐙 GitHub Actions Environment</text>
  <rect x="65" y="90" width="290" height="90" rx="10" fill="#1e293b" stroke="#334155"/>
  <text x="80" y="115" fill="#cbd5e1" font-family="JetBrains Mono, monospace" font-size="12">🔐 GitHub Encrypted Secrets:</text>
  <text x="80" y="135" fill="#818cf8" font-family="JetBrains Mono, monospace" font-size="11">AWS_ACCESS_KEY_ID</text>
  <text x="80" y="152" fill="#818cf8" font-family="JetBrains Mono, monospace" font-size="11">AWS_SECRET_ACCESS_KEY</text>
  <text x="80" y="169" fill="#34d3b4" font-family="JetBrains Mono, monospace" font-size="11">EC2_HOST, EC2_SSH_KEY</text>

  <!-- AWS Boundary -->
  <rect x="440" y="30" width="600" height="280" rx="16" fill="#070d1a" stroke="#6366f1" stroke-width="2" stroke-dasharray="6 6"/>
  <text x="465" y="65" fill="#c7d2fe" font-family="Sora, sans-serif" font-size="15" font-weight="700">☁️ AWS Cloud · us-east-1</text>

  <!-- IAM User Box -->
  <rect x="470" y="90" width="240" height="90" rx="10" fill="url(#g-iam)" stroke="#6366f1"/>
  <text x="485" y="118" fill="#e0e7ff" font-family="Sora, sans-serif" font-size="13" font-weight="700">👤 IAM Bot User</text>
  <text x="485" y="138" fill="#a5b4fc" font-family="JetBrains Mono, monospace" font-size="11">zeetafin-ci-cd-bot</text>
  <text x="485" y="158" fill="#cbd5e1" font-family="JetBrains Mono, monospace" font-size="10">EC2ContainerRegistryPowerUser</text>

  <!-- ECR Repositories Box -->
  <rect x="750" y="90" width="260" height="190" rx="10" fill="url(#g-ecr)" stroke="#10b981"/>
  <text x="770" y="120" fill="#a7f3d0" font-family="Sora, sans-serif" font-size="13" font-weight="700">📦 Amazon ECR</text>
  <rect x="765" y="135" width="230" height="55" rx="6" fill="#064e3b" stroke="#059669"/>
  <text x="775" y="158" fill="#ecfdf5" font-family="JetBrains Mono, monospace" font-size="11">zeetafin-backend</text>
  <text x="775" y="176" fill="#6ee7b7" font-family="JetBrains Mono, monospace" font-size="10">AES-256 · Scan on push: ON</text>
  
  <rect x="765" y="200" width="230" height="55" rx="6" fill="#064e3b" stroke="#059669"/>
  <text x="775" y="223" fill="#ecfdf5" font-family="JetBrains Mono, monospace" font-size="11">zeetafin-frontend</text>
  <text x="775" y="241" fill="#6ee7b7" font-family="JetBrains Mono, monospace" font-size="10">AES-256 · Scan on push: ON</text>

  <!-- Connectors -->
  <line x1="355" y1="135" x2="470" y2="135" stroke="#818cf8" stroke-width="2.5" marker-end="url(#arr-c1)"/>
  <line x1="710" y1="135" x2="750" y2="135" stroke="#34d3b4" stroke-width="2.5" marker-end="url(#arr-c4)"/>
</svg>
</div>

</div></header>

<div class="wrap"><div class="layout">

<!-- Table of Contents -->
<nav class="toc" aria-label="Table of Contents">
  <h2>Contents</h2>
  <ol>
    <li><a href="#overview">1. Overview &amp; Architecture</a></li>
    <li><a href="#threat-model">2. CI/CD Threat Modeling</a></li>
    <li><a href="#iam-policy">3. Least-Privilege IAM Policy</a></li>
    <li><a href="#iam-user">4. Creating IAM Bot User</a></li>
    <li><a href="#ecr-setup">5. Provisioning ECR Repos</a></li>
    <li><a href="#security-scan">6. Vulnerability Scanning</a></li>
    <li><a href="#lifecycle">7. ECR Lifecycle Policies</a></li>
    <li><a href="#secrets-setup">8. GitHub Secrets Setup</a></li>
    <li><a href="#local-test">9. Verifying ECR Auth</a></li>
    <li><a href="#checklist">10. Review Checklist</a></li>
    <li><a href="#next">11. What Comes Next</a></li>
  </ol>

  <div class="sidecard">
    <b>Lab Focus</b>
    <p>Establishing the authentication and authorization bedrock so automated pipelines never compromise cloud infrastructure.</p>
  </div>
</nav>

<!-- Article Content -->
<article>

<!-- SECTION 1 -->
<h2 id="overview"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg></span>1. Overview &amp; Architecture</h2>

<p class="lead">An automated CI/CD pipeline is only as secure as the credentials executing it. In Phase 3, GitHub Actions operates as an autonomous agent that must authenticate with AWS to push container images and connect over SSH to deploy onto our EC2 host.</p>

<p>Before writing a single line of GitHub Actions workflow YAML, we must configure three essential security boundaries:</p>

<div class="cards">
  <div class="card" style="--c:#6366f1">
    <h4>1. Dedicated IAM Bot User</h4>
    <p>A programmatic non-human entity (<code>zeetafin-ci-cd-bot</code>) restricted strictly to Amazon ECR authorization, repository discovery, and image uploads.</p>
  </div>
  <div class="card" style="--c:#10b981">
    <h4>2. Encrypted ECR Repositories</h4>
    <p>Server-side encrypted (KMS/AES-256) container registries with automated image vulnerability scanning and immutable layer storage.</p>
  </div>
  <div class="card" style="--c:#f59e0b">
    <h4>3. GitHub Encrypted Secrets</h4>
    <p>Zero-exposure credential vault within the GitHub repository, preventing access keys and SSH private keys from leaking into version control.</p>
  </div>
</div>

<!-- SECTION 2 -->
<h2 id="threat-model"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></span>2. CI/CD Credential Threat Modeling</h2>

<p>Why can't we simply use our personal AWS Administrator credentials in GitHub Secrets? In enterprise DevOps, shared administrative credentials violate basic compliance and expose organizations to catastrophic blast radiuses:</p>

<div class="tbl">
  <table>
    <thead>
      <tr>
        <th>Vector</th>
        <th>Administrative Credentials (Dangerous)</th>
        <th>Scoped Least-Privilege IAM (Production)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Compromise Impact</td>
        <td>Total AWS account takeover, data deletion, crypto-mining.</td>
        <td>Attacker can only write images to <code>zeetafin-*</code> ECR repos.</td>
      </tr>
      <tr>
        <td>Audit &amp; Attribution</td>
        <td>CloudTrail events indistinguishable from operator actions.</td>
        <td>Every push is strictly tagged to <code>zeetafin-ci-cd-bot</code>.</td>
      </tr>
      <tr>
        <td>Revocation Velocity</td>
        <td>Revoking disrupts human engineers and admin consoles.</td>
        <td>Single-click deactivation without affecting engineers.</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="callout warn">
  <svg viewBox="0 0 24 24"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
  <div>
    <b class="t">Never Commit Secrets to Version Control</b>
    <p>Git history is immutable. Committing <code>.pem</code> keys, AWS credentials, or <code>.env</code> files to GitHub—even for a few seconds before deleting them—exposes them to automated scrapers. Always verify <code>.gitignore</code> before staging.</p>
  </div>
</div>

<!-- SECTION 3 -->
<h2 id="iam-policy"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg></span>3. Least-Privilege IAM Policy</h2>

<p>AWS provides the managed policy <code>AmazonEC2ContainerRegistryPowerUser</code>, which grants permissions to read, write, and list ECR repositories, but forbids deleting repositories. For higher security environments, we can scope this even further to our specific project ARN prefix:</p>

<div class="code">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">zeetafin-ecr-least-privilege-policy.json</span>
    <span class="tag">JSON</span>
    <button class="copy" type="button"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy</button>
  </div>
<pre><code>{{
  <span class="k">"Version"</span>: <span class="s2">"2012-10-17"</span>,
  <span class="k">"Statement"</span>: [
    {{
      <span class="k">"Sid"</span>: <span class="s2">"ECRAuthToken"</span>,
      <span class="k">"Effect"</span>: <span class="s2">"Allow"</span>,
      <span class="k">"Action"</span>: [
        <span class="s2">"ecr:GetAuthorizationToken"</span>
      ],
      <span class="k">"Resource"</span>: <span class="s2">"*"</span>
    }},
    {{
      <span class="k">"Sid"</span>: <span class="s2">"ManageZeetaFinRepositories"</span>,
      <span class="k">"Effect"</span>: <span class="s2">"Allow"</span>,
      <span class="k">"Action"</span>: [
        <span class="s2">"ecr:BatchCheckLayerAvailability"</span>,
        <span class="s2">"ecr:GetDownloadUrlForLayer"</span>,
        <span class="s2">"ecr:BatchGetImage"</span>,
        <span class="s2">"ecr:PutImage"</span>,
        <span class="s2">"ecr:InitiateLayerUpload"</span>,
        <span class="s2">"ecr:UploadLayerPart"</span>,
        <span class="s2">"ecr:CompleteLayerUpload"</span>,
        <span class="s2">"ecr:DescribeRepositories"</span>,
        <span class="s2">"ecr:ListImages"</span>,
        <span class="s2">"ecr:DescribeImages"</span>
      ],
      <span class="k">"Resource"</span>: <span class="s2">"arn:aws:ecr:us-east-1:*:repository/zeetafin-*"</span>
    }}
  ]
}}</code></pre>
</div>

<!-- SECTION 4 -->
<h2 id="iam-user"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg></span>4. Creating the IAM Bot User</h2>

<p>We create the dedicated IAM user <code>zeetafin-ci-cd-bot</code> and attach the ECR PowerUser policy using the AWS CLI or AWS Management Console:</p>

<div class="term">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">Terminal (Local Operator Machine)</span>
    <span class="tag">BASH</span>
    <button class="copy" type="button"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy</button>
  </div>
<pre><code><span class="p">$ </span><span class="c"># 1. Create the IAM user</span>
<span class="p">$ </span>aws iam create-user --user-name zeetafin-ci-cd-bot

<span class="p">$ </span><span class="c"># 2. Attach ECR PowerUser policy</span>
<span class="p">$ </span>aws iam attach-user-policy \
    --user-name zeetafin-ci-cd-bot \
    --policy-arn arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryPowerUser

<span class="p">$ </span><span class="c"># 3. Generate Programmatic Access Key pair</span>
<span class="p">$ </span>aws iam create-access-key --user-name zeetafin-ci-cd-bot</code></pre>
</div>

<p>The CLI outputs the Access Key credentials. Save these temporarily in a secure buffer—we will paste them directly into GitHub Secrets:</p>

<div class="term">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">Output — create-access-key</span>
    <span class="tag exp">JSON</span>
  </div>
<pre><code>{{
    <span class="k">"AccessKey"</span>: {{
        <span class="k">"UserName"</span>: <span class="s2">"zeetafin-ci-cd-bot"</span>,
        <span class="k">"AccessKeyId"</span>: <span class="n">"AKIAIOSFODNN7EXAMPLE"</span>,
        <span class="k">"Status"</span>: <span class="ok">"Active"</span>,
        <span class="k">"SecretAccessKey"</span>: <span class="n">"wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"</span>,
        <span class="k">"CreateDate"</span>: <span class="s2">"2026-10-19T13:45:00Z"</span>
    }}
}}</code></pre>
</div>

<!-- SECTION 5 -->
<h2 id="ecr-setup"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"/><rect x="2" y="14" width="20" height="8" rx="2" ry="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/></svg></span>5. Provisioning Amazon ECR Repositories</h2>

<p>Our Phase 2 application consists of two decoupled services: the NestJS backend and Next.js frontend. We provision two discrete ECR repositories with KMS encryption and scan-on-push enabled:</p>

<div class="term">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">Terminal (AWS CLI)</span>
    <span class="tag">BASH</span>
    <button class="copy" type="button"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy</button>
  </div>
<pre><code><span class="p">$ </span><span class="c"># Create zeetafin-backend repository</span>
<span class="p">$ </span>aws ecr create-repository \
    --repository-name zeetafin-backend \
    --image-tag-mutability MUTABLE \
    --image-scanning-configuration scanOnPush=true \
    --encryption-configuration encryptionType=AES256 \
    --region us-east-1

<span class="p">$ </span><span class="c"># Create zeetafin-frontend repository</span>
<span class="p">$ </span>aws ecr create-repository \
    --repository-name zeetafin-frontend \
    --image-tag-mutability MUTABLE \
    --image-scanning-configuration scanOnPush=true \
    --encryption-configuration encryptionType=AES256 \
    --region us-east-1</code></pre>
</div>

<!-- SECTION 6 -->
<h2 id="security-scan"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></span>6. Vulnerability Scanning &amp; CVE Auditing</h2>

<p>By enabling <code>scanOnPush=true</code>, Amazon ECR automatically scans container layers against the Common Vulnerabilities and Exposures (CVE) database upon receipt. When images land in ECR, you can query their security health immediately:</p>

<div class="term">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">Terminal (AWS CLI)</span>
    <span class="tag">BASH</span>
    <button class="copy" type="button"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy</button>
  </div>
<pre><code><span class="p">$ </span>aws ecr describe-image-scan-findings \
    --repository-name zeetafin-backend \
    --image-id imageTag=latest \
    --region us-east-1</code></pre>
</div>

<!-- SECTION 7 -->
<h2 id="lifecycle"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/></svg></span>7. ECR Lifecycle Policies: Automated Pruning</h2>

<p>Every CI/CD push generates new image tags. Without a lifecycle policy, untagged and historical layers accumulate, driving up AWS storage billing. We apply a policy to retain only the last 10 tagged builds and purge untagged intermediate layers after 7 days:</p>

<div class="code">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">ecr-lifecycle-policy.json</span>
    <span class="tag">JSON</span>
    <button class="copy" type="button"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy</button>
  </div>
<pre><code>{{
  <span class="k">"rules"</span>: [
    {{
      <span class="k">"rulePriority"</span>: <span class="n">1</span>,
      <span class="k">"description"</span>: <span class="s2">"Expire untagged images older than 7 days"</span>,
      <span class="k">"selection"</span>: {{
        <span class="k">"tagStatus"</span>: <span class="s2">"untagged"</span>,
        <span class="k">"countType"</span>: <span class="s2">"sinceImagePushed"</span>,
        <span class="k">"countUnit"</span>: <span class="s2">"days"</span>,
        <span class="k">"countNumber"</span>: <span class="n">7</span>
      }},
      <span class="k">"action"</span>: {{
        <span class="k">"type"</span>: <span class="s2">"expire"</span>
      }}
    }},
    {{
      <span class="k">"rulePriority"</span>: <span class="n">2</span>,
      <span class="k">"description"</span>: <span class="s2">"Retain only the 10 most recent tagged releases"</span>,
      <span class="k">"selection"</span>: {{
        <span class="k">"tagStatus"</span>: <span class="s2">"any"</span>,
        <span class="k">"countType"</span>: <span class="s2">"imageCountMoreThan"</span>,
        <span class="k">"countNumber"</span>: <span class="n">10</span>
      }},
      <span class="k">"action"</span>: {{
        <span class="k">"type"</span>: <span class="s2">"expire"</span>
      }}
    }}
  ]
}}</code></pre>
</div>

<div class="term">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">Terminal (AWS CLI)</span>
    <span class="tag">BASH</span>
    <button class="copy" type="button"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy</button>
  </div>
<pre><code><span class="p">$ </span>aws ecr put-lifecycle-policy \
    --repository-name zeetafin-backend \
    --lifecycle-policy-text file://ecr-lifecycle-policy.json

<span class="p">$ </span>aws ecr put-lifecycle-policy \
    --repository-name zeetafin-frontend \
    --lifecycle-policy-text file://ecr-lifecycle-policy.json</code></pre>
</div>

<!-- SECTION 8 -->
<h2 id="secrets-setup"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg></span>8. Configuring GitHub Repository Secrets</h2>

<p>Navigate to your repository on GitHub: <strong>Settings &gt; Secrets and variables &gt; Actions &gt; New repository secret</strong>. Configure each of the following 6 secrets:</p>

<div class="tbl">
  <table>
    <thead>
      <tr>
        <th>Secret Name</th>
        <th>Value / Origin</th>
        <th>Purpose</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>AWS_ACCESS_KEY_ID</code></td>
        <td><code>AKIA...</code> from IAM user creation</td>
        <td>Authenticates GitHub Actions runner to AWS.</td>
      </tr>
      <tr>
        <td><code>AWS_SECRET_ACCESS_KEY</code></td>
        <td>Secret key string from IAM creation</td>
        <td>AWS cryptographic signature key.</td>
      </tr>
      <tr>
        <td><code>AWS_REGION</code></td>
        <td><code>us-east-1</code></td>
        <td>Target AWS Region for ECR and EC2.</td>
      </tr>
      <tr>
        <td><code>EC2_HOST</code></td>
        <td>Public IP from Phase 1 Terraform (e.g. <code>54.210.xx.xx</code>)</td>
        <td>Destination host for SSH deployment connection.</td>
      </tr>
      <tr>
        <td><code>EC2_USERNAME</code></td>
        <td><code>ubuntu</code></td>
        <td>Default SSH system user for Ubuntu 24.04 LTS.</td>
      </tr>
      <tr>
        <td><code>EC2_SSH_KEY</code></td>
        <td>Complete contents of <code>phase1-key.pem</code></td>
        <td>OpenSSH RSA Private key used to authenticate SSH session.</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="callout info">
  <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
  <div>
    <b class="t">Formatting the EC2_SSH_KEY Secret</b>
    <p>Ensure the entire PEM content is pasted, including the opening line <code>-----BEGIN RSA PRIVATE KEY-----</code> and ending line <code>-----END RSA PRIVATE KEY-----</code>, without adding extra blank lines or spaces.</p>
  </div>
</div>

<!-- SECTION 9 -->
<h2 id="local-test"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/></svg></span>9. Verifying ECR Auth &amp; Registry Reachability</h2>

<p>Before launching GitHub Actions, test the credentials locally to verify that the IAM user possesses valid permissions to retrieve an ECR authorization token and log in to Docker:</p>

<div class="term">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">Terminal (Verification Command)</span>
    <span class="tag">BASH</span>
    <button class="copy" type="button"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy</button>
  </div>
<pre><code><span class="p">$ </span>AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
<span class="p">$ </span>echo "AWS Account: ${{AWS_ACCOUNT_ID}}"

<span class="p">$ </span><span class="c"># Authenticate Docker client against Amazon ECR registry</span>
<span class="p">$ </span>aws ecr get-login-password --region us-east-1 | \
    docker login --username AWS --password-stdin "${{AWS_ACCOUNT_ID}}.dkr.ecr.us-east-1.amazonaws.com"</code></pre>
</div>

<p>Expected successful output:</p>
<div class="term">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">Output</span>
    <span class="tag ok">SUCCESS</span>
  </div>
<pre><code>WARNING! Your password will be stored unencrypted in /home/ubuntu/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

<span class="ok">Login Succeeded</span></code></pre>
</div>

<!-- SECTION 10 -->
<h2 id="checklist"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg></span>10. Verification Checklist &amp; Challenge</h2>

<ol class="steps">
  <li>
    <b>IAM Bot User Configured</b>
    <p>User <code>zeetafin-ci-cd-bot</code> exists and has programmatic access keys generated.</p>
  </li>
  <li>
    <b>ECR Repositories Created</b>
    <p>Both <code>zeetafin-backend</code> and <code>zeetafin-frontend</code> are active in <code>us-east-1</code> with AES-256 encryption.</p>
  </li>
  <li>
    <b>GitHub Secrets Injected</b>
    <p>All 6 required secrets (<code>AWS_ACCESS_KEY_ID</code>, <code>AWS_SECRET_ACCESS_KEY</code>, <code>AWS_REGION</code>, <code>EC2_HOST</code>, <code>EC2_USERNAME</code>, <code>EC2_SSH_KEY</code>) are saved.</p>
  </li>
  <li>
    <b>Challenge Exercise</b>
    <p>Run <code>aws ecr describe-repositories --query "repositories[].repositoryUri"</code> and verify that both URIs follow the standard <code>&lt;account-id&gt;.dkr.ecr.us-east-1.amazonaws.com/&lt;name&gt;</code> syntax.</p>
  </li>
</ol>

<!-- SECTION 11 -->
<h2 id="next"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg></span>11. What Comes Next</h2>

<p>With our IAM permissions, ECR registries, and encrypted secrets established, we are ready for <strong>Part 2</strong>: Writing the automated GitHub Actions workflow file (<code>.github/workflows/deploy.yml</code>), configuring Docker Buildx layer caching, and pushing tagged container images on every code commit.</p>

<div class="pager">
  <span></span>
  <a class="r" href="part-2-github-actions-workflow-ci.html">
    <small>Next Chapter →</small>
    GitHub Actions CI Workflow &amp; Container Build Engine
  </a>
</div>

</article>
</div></div>

<footer><div class="wrap">ZeetaFin Cloud Architecture &middot; Phase 3 CI/CD Lab Series &middot; <a href="https://github.com/Devzane">GitHub</a></div></footer>

<script>
{COMMON_SCRIPT}
</script>
</body></html>
"""

if __name__ == "__main__":
    from build_all_labs import write_lab
    write_lab("part-1-aws-iam-ecr-github-secrets.html", get_part1_html())
