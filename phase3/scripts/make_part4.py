#!/usr/bin/env python3
import os
from generate_labs import COMMON_CSS, COMMON_SCRIPT, generate_navbar

def get_part4_html():
    nav = generate_navbar(4)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>End-to-End Pipeline Verification &amp; Triage — ZeetaFin Phase 3 Lab Part 4</title>
<meta name="description" content="Part 4 of the ZeetaFin Phase 3 CI/CD Lab: execute end-to-end integration tests, verify browser accessibility, drill failure scenarios, and assemble deliverables.">
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

<h1>End-to-End Pipeline Verification &amp; Incident Triage</h1>
<p class="dek">Closing the continuous delivery loop: Simulating real-world application code releases, real-time workflow tracing, live browser verification, failure injection drills, and project deliverables packaging.</p>

<p class="meta">
  <span><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> Oct 2026</span>
  <span><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> ~50 min read</span>
  <span><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a4 4 0 0 0 5 5L21 12.6a2 2 0 0 1 0 2.8l-5.6 5.6a2 2 0 0 1-2.8 0L3 11.4a2 2 0 0 1 0-2.8L8.6 3a2 2 0 0 1 2.8 0z" transform="translate(0 0) scale(.9) translate(1.3 1.3)"/></svg> ~60 min hands-on</span>
  <span><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v16H6.5A2.5 2.5 0 0 0 4 21.5z"/><path d="M4 18.5A2.5 2.5 0 0 1 6.5 16H20"/></svg> End-to-End Testing, Smoke Checks, Triage, Deliverables</span>
</p>

<div class="tools">
  <span class="tool">🔄 Push-to-Deploy Lifecycle</span>
  <span class="tool">🌐 Live Browser Verification</span>
  <span class="tool">🚨 Fault Injection Drills</span>
  <span class="tool">📑 Submission Deliverables</span>
</div>

<div class="hero-art">
<svg viewBox="0 0 1080 340" role="img" aria-label="End-to-End Automated Pipeline Workflow">
  <defs>
    <linearGradient id="g-flow" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#022c22"/><stop offset="100%" stop-color="#070b14"/></linearGradient>
    <marker id="arr-f1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 1 L 10 5 L 0 9 z" fill="#34d3b4"/></marker>
  </defs>

  <rect x="30" y="25" width="1020" height="290" rx="16" fill="url(#g-flow)" stroke="#10b981" stroke-width="2"/>
  <text x="55" y="60" fill="#a7f3d0" font-family="Sora, sans-serif" font-size="15" font-weight="700">🔁 The Complete Developer-to-Production Pipeline</text>

  <!-- Node 1: Dev Push -->
  <rect x="55" y="90" width="160" height="180" rx="10" fill="#1e293b" stroke="#334155"/>
  <circle cx="75" cy="115" r="12" fill="#6366f1"/>
  <text x="71" y="120" fill="#fff" font-family="Sora, sans-serif" font-size="12" font-weight="700">1</text>
  <text x="95" y="120" fill="#f8fafc" font-family="Sora, sans-serif" font-size="13" font-weight="700">Developer</text>
  <text x="70" y="150" fill="#818cf8" font-family="JetBrains Mono, monospace" font-size="11">git push</text>
  <text x="70" y="170" fill="#cbd5e1" font-family="DM Sans, sans-serif" font-size="12">Pushes code change to GitHub main branch</text>

  <!-- Node 2: GitHub Actions -->
  <rect x="250" y="90" width="200" height="180" rx="10" fill="#1e293b" stroke="#334155"/>
  <circle cx="270" cy="115" r="12" fill="#0ea5e9"/>
  <text x="266" y="120" fill="#fff" font-family="Sora, sans-serif" font-size="12" font-weight="700">2</text>
  <text x="290" y="120" fill="#f8fafc" font-family="Sora, sans-serif" font-size="13" font-weight="700">GitHub Actions</text>
  <text x="265" y="150" fill="#38bdf8" font-family="JetBrains Mono, monospace" font-size="11">Build &amp; Push ECR</text>
  <text x="265" y="170" fill="#38bdf8" font-family="JetBrains Mono, monospace" font-size="11">SSH to EC2 Host</text>
  <text x="265" y="195" fill="#cbd5e1" font-family="DM Sans, sans-serif" font-size="12">Executes build, auth, and remote deployment</text>

  <!-- Node 3: EC2 Deployment -->
  <rect x="485" y="90" width="240" height="180" rx="10" fill="#1e293b" stroke="#334155"/>
  <circle cx="505" cy="115" r="12" fill="#f59e0b"/>
  <text x="501" y="120" fill="#fff" font-family="Sora, sans-serif" font-size="12" font-weight="700">3</text>
  <text x="525" y="120" fill="#f8fafc" font-family="Sora, sans-serif" font-size="13" font-weight="700">AWS EC2 Server</text>
  <text x="500" y="150" fill="#fcd34d" font-family="JetBrains Mono, monospace" font-size="11">docker compose pull</text>
  <text x="500" y="170" fill="#fcd34d" font-family="JetBrains Mono, monospace" font-size="11">up -d --force-recreate</text>
  <text x="500" y="195" fill="#cbd5e1" font-family="DM Sans, sans-serif" font-size="12">Replaces old containers with zero port conflict</text>

  <!-- Node 4: Browser Verification -->
  <rect x="760" y="90" width="260" height="180" rx="10" fill="#064e3b" stroke="#10b981"/>
  <circle cx="780" cy="115" r="12" fill="#10b981"/>
  <text x="776" y="120" fill="#fff" font-family="Sora, sans-serif" font-size="12" font-weight="700">4</text>
  <text x="800" y="120" fill="#ecfdf5" font-family="Sora, sans-serif" font-size="13" font-weight="700">Live Application</text>
  <text x="775" y="150" fill="#6ee7b7" font-family="JetBrains Mono, monospace" font-size="11">UI: :3000 (Next.js)</text>
  <text x="775" y="170" fill="#6ee7b7" font-family="JetBrains Mono, monospace" font-size="11">API: :3001 (NestJS)</text>
  <text x="775" y="195" fill="#a7f3d0" font-family="DM Sans, sans-serif" font-size="12">External healthcheck succeeds (HTTP 200)</text>

  <!-- Connectors -->
  <line x1="215" y1="180" x2="250" y2="180" stroke="#34d3b4" stroke-width="2.5" marker-end="url(#arr-f1)"/>
  <line x1="450" y1="180" x2="485" y2="180" stroke="#34d3b4" stroke-width="2.5" marker-end="url(#arr-f1)"/>
  <line x1="725" y1="180" x2="760" y2="180" stroke="#34d3b4" stroke-width="2.5" marker-end="url(#arr-f1)"/>
</svg>
</div>

</div></header>

<div class="wrap"><div class="layout">

<!-- Table of Contents -->
<nav class="toc" aria-label="Table of Contents">
  <h2>Contents</h2>
  <ol>
    <li><a href="#lifecycle">1. Lifecycle Overview</a></li>
    <li><a href="#code-change">2. Simulating Code Update</a></li>
    <li><a href="#git-push">3. Triggering the Rollout</a></li>
    <li><a href="#trace-workflow">4. Tracing Workflow Logs</a></li>
    <li><a href="#ec2-status">5. Inspecting EC2 State</a></li>
    <li><a href="#external-smoke">6. External Smoke Testing</a></li>
    <li><a href="#browser-ui">7. Browser UI Verification</a></li>
    <li><a href="#failure-drills">8. Fault Injection Drills</a></li>
    <li><a href="#deliverables">9. Submission Deliverables</a></li>
    <li><a href="#retrospective">10. Project Retrospective</a></li>
  </ol>

  <div class="sidecard">
    <b>Lab Focus</b>
    <p>Validating the complete autonomous deployment lifecycle, drilling failure modes, and gathering the required evidence for project submission.</p>
  </div>
</nav>

<!-- Article Content -->
<article>

<!-- SECTION 1 -->
<h2 id="lifecycle"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg></span>1. Lifecycle Overview</h2>

<p class="lead">The ultimate benchmark of an enterprise DevOps engineer is an autonomous delivery system that requires zero manual SSH intervention during standard releases. In this final lab, we test the entire pipeline from git commit to live browser verification.</p>

<div class="callout ok">
  <svg viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
  <div>
    <b class="t">Success Criteria Definition</b>
    <p>A successful project demonstrates that when a fellow pushes an application update to GitHub, GitHub Actions automatically builds the new image, pushes it to ECR, and deploys the updated application to EC2 with zero manual commands.</p>
  </div>
</div>

<!-- SECTION 2 -->
<h2 id="code-change"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg></span>2. Simulating a Real Application Update</h2>

<p>To demonstrate continuous deployment in action, we make a visible update to the ZeetaFin ERP header or backend version endpoint:</p>

<div class="code">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">phase2/frontend/app/page.tsx (Snippet)</span>
    <span class="tag">TSX</span>
  </div>
<pre><code><span class="c">// Add a release badge to the main dashboard hero</span>
&lt;<span class="k">div</span> <span class="n">className</span>=<span class="s2">"inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 text-emerald-400 text-xs font-mono mb-4 border border-emerald-500/20"</span>&gt;
  &lt;<span class="k">span</span> <span class="n">className</span>=<span class="s2">"w-2 h-2 rounded-full bg-emerald-400 animate-pulse"</span> /&gt;
  Release v1.1.0 &middot; Automated CI/CD Active
&lt;/<span class="k">div</span>&gt;</code></pre>
</div>

<!-- SECTION 3 -->
<h2 id="git-push"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="16 16 12 12 8 16"/><line x1="12" y1="12" x2="12" y2="21"/><path d="M20.39 18.39A5 5 0 0 0 18 9h-1.26A8 8 0 1 0 3 16.3"/></svg></span>3. Committing and Pushing to GitHub</h2>

<p>Following our strict repository commit rules, inspect the diff and make a granular, atomic commit:</p>

<div class="term">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">Terminal (Local Developer Machine)</span>
    <span class="tag">BASH</span>
    <button class="copy" type="button"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy</button>
  </div>
<pre><code><span class="p">$ </span>git status
<span class="p">$ </span>git diff phase2/frontend/app/page.tsx
<span class="p">$ </span>git add phase2/frontend/app/page.tsx
<span class="p">$ </span>git commit -m "feat(ui): add automated release badge to dashboard"
<span class="p">$ </span>git push origin main</code></pre>
</div>

<!-- SECTION 4 -->
<h2 id="trace-workflow"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg></span>4. Tracing Real-Time Workflow Logs</h2>

<p>Navigate to <strong>GitHub &gt; Actions</strong> and watch the execution unfold. The pipeline progresses through both stages:</p>

<ol class="steps">
  <li>
    <b>Job 1: Build &amp; Push Images to Amazon ECR</b>
    <p>Docker Buildx compiles the Next.js standalone bundle and pushes tags <code>zeetafin-frontend:&lt;commit-sha&gt;</code> and <code>zeetafin-frontend:latest</code>.</p>
  </li>
  <li>
    <b>Job 2: Deploy to AWS EC2 Infrastructure</b>
    <p>GitHub Actions establishes an SSH connection, copies the production manifests, and runs <code>deploy.sh</code>.</p>
  </li>
  <li>
    <b>Automated External Availability Smoke Check</b>
    <p>The runner sends an HTTP GET request to <code>http://${{{{ secrets.EC2_HOST }}}}:3000</code> and verifies an immediate HTTP 200 OK.</p>
  </li>
</ol>

<!-- SECTION 5 -->
<h2 id="ec2-status"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"/><rect x="2" y="14" width="20" height="8" rx="2" ry="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/></svg></span>5. Inspecting Deployed Containers on EC2</h2>

<p>SSH into your EC2 instance using the Phase 1 key and check the running services:</p>

<div class="term">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">Terminal (SSH to EC2 Host)</span>
    <span class="tag">BASH</span>
    <button class="copy" type="button"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy</button>
  </div>
<pre><code><span class="p">$ </span>ssh -i phase1-key.pem ubuntu@&lt;EC2_PUBLIC_IP&gt;
<span class="p">$ </span>cd /home/ubuntu/zeetafin-app
<span class="p">$ </span>docker compose -f docker-compose.prod.yml ps</code></pre>
</div>

<p>Expected output showing all 3 services healthy and active:</p>
<div class="term">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">Output — docker compose ps</span>
    <span class="tag ok">RUNNING</span>
  </div>
<pre><code>NAME                     IMAGE                                                  COMMAND                  SERVICE    CREATED          STATUS                    PORTS
zeetafin-backend-prod    123456789012.dkr.ecr.us-east-1.amazonaws.com/...      "docker-entrypoint.s…"   backend    2 minutes ago    <span class="ok">Up 2 minutes (healthy)</span>    0.0.0.0:3001->3001/tcp
zeetafin-db-prod         postgres:16-alpine                                     "docker-entrypoint.s…"   db         10 minutes ago   <span class="ok">Up 10 minutes (healthy)</span>   0.0.0.0:5432->5432/tcp
zeetafin-frontend-prod   123456789012.dkr.ecr.us-east-1.amazonaws.com/...      "docker-entrypoint.s…"   frontend   2 minutes ago    <span class="ok">Up 2 minutes (healthy)</span>    0.0.0.0:3000->3000/tcp</code></pre>
</div>

<!-- SECTION 6 -->
<h2 id="external-smoke"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/></svg></span>6. External Smoke Testing with curl</h2>

<p>From your local laptop terminal, probe the public EC2 IP address:</p>

<div class="term">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">Terminal (Local Laptop)</span>
    <span class="tag">BASH</span>
    <button class="copy" type="button"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy</button>
  </div>
<pre><code><span class="p">$ </span>curl -I "http://&lt;EC2_PUBLIC_IP&gt;:3000"
<span class="p">$ </span>curl -I "http://&lt;EC2_PUBLIC_IP&gt;:3001/api/docs"</code></pre>
</div>

<p>Both endpoints must return <code>HTTP/1.1 200 OK</code>.</p>

<!-- SECTION 7 -->
<h2 id="browser-ui"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><polygon points="10 8 16 12 10 16 10 8"/></svg></span>7. Live Browser Verification</h2>

<p>Open your browser and navigate to:</p>
<ul>
  <li><strong>ZeetaFin ERP Frontend:</strong> <code>http://&lt;EC2_PUBLIC_IP&gt;:3000</code></li>
  <li><strong>Swagger REST API Documentation:</strong> <code>http://&lt;EC2_PUBLIC_IP&gt;:3001/api/docs</code></li>
</ul>

<p>Verify that your new update (e.g. the Release v1.1.0 badge) renders immediately in the browser without having had to restart any servers by hand.</p>

<!-- SECTION 8 -->
<h2 id="failure-drills"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polygon points="7.86 2 16.14 2 22 7.86 22 16.14 16.14 22 7.86 22 2 16.14 2 7.86 7.86 2"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg></span>8. Failure Scenarios &amp; Incident Drills</h2>

<p>High-performing DevOps engineers test failure paths just as thoroughly as happy paths. Here is how our architecture responds to common incidents:</p>

<div class="tbl">
  <table>
    <thead>
      <tr>
        <th>Incident Drill</th>
        <th>Pipeline Response</th>
        <th>Production Safety Guarantee</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Syntax error in TypeScript code</strong></td>
        <td><code>npm run build</code> fails inside Docker Buildx during Job 1.</td>
        <td><strong>EC2 is never touched!</strong> The existing production application continues running unaffected.</td>
      </tr>
      <tr>
        <td><strong>EC2 SSH port closed by mistake</strong></td>
        <td>Job 2 fails during SSH connection timeout.</td>
        <td>GitHub Actions alerts operator; image is safely preserved in ECR.</td>
      </tr>
      <tr>
        <td><strong>Database container crash</strong></td>
        <td>Docker healthcheck detects failure; dependent containers restart automatically via <code>restart: unless-stopped</code>.</td>
        <td>Data is persisted on EBS volume <code>zeetafin_prod_pgdata</code>.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- SECTION 9 -->
<h2 id="deliverables"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg></span>9. Fellow Submission Deliverables</h2>

<p>To successfully complete Phase 3, gather the following 8 required deliverables:</p>

<div class="cards">
  <div class="card" style="--c:#6366f1">
    <h4>1. GitHub Repository</h4>
    <p>Public or shared repository containing complete Phase 1, Phase 2, and Phase 3 code.</p>
  </div>
  <div class="card" style="--c:#0ea5e9">
    <h4>2. Dockerfiles</h4>
    <p>Multi-stage production Dockerfiles for both backend and frontend.</p>
  </div>
  <div class="card" style="--c:#f59e0b">
    <h4>3. Workflow File</h4>
    <p><code>.github/workflows/deploy.yml</code> with build, push, deploy, and verify jobs.</p>
  </div>
  <div class="card" style="--c:#10b981">
    <h4>4. ECR Repository</h4>
    <p>AWS ECR console screenshot showing tagged container images.</p>
  </div>
  <div class="card" style="--c:#8b5cf6">
    <h4>5. EC2 Deployment</h4>
    <p>EC2 terminal screenshot showing <code>docker compose ps</code> with all healthy containers.</p>
  </div>
  <div class="card" style="--c:#ec4899">
    <h4>6. GitHub Secrets</h4>
    <p>Screenshot of repository Secrets settings demonstrating proper naming.</p>
  </div>
  <div class="card" style="--c:#3b82f6">
    <h4>7. Comprehensive README</h4>
    <p><code>phase3/README.md</code> with architecture, setup, and troubleshooting documentation.</p>
  </div>
  <div class="card" style="--c:#14b8a6">
    <h4>8. Live Application Proof</h4>
    <p>Browser screenshot displaying the active ZeetaFin Web UI running on the EC2 public IP.</p>
  </div>
</div>

<!-- SECTION 10 -->
<h2 id="retrospective"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg></span>10. Project Retrospective &amp; Conclusion</h2>

<p>Congratulations! Across Phases 1, 2, and 3, you have engineered a complete, production-grade cloud infrastructure and continuous delivery platform:</p>

<ul>
  <li><strong>Phase 1:</strong> Provisioned an isolated AWS VPC, hardened public subnet, IMDSv2-enforced EC2 instance with Terraform, and configured Docker CE with an idempotent Ansible playbook.</li>
  <li><strong>Phase 2:</strong> Architected multi-stage Dockerfiles, optimized image sizes down to minimal Alpine footprints, and orchestrated multi-tier local stacks with Docker Compose.</li>
  <li><strong>Phase 3:</strong> Automated end-to-end continuous delivery with GitHub Actions, Amazon ECR registries, secure SSH remote execution, atomic container rollouts, and automated health checks.</li>
</ul>

<div class="callout ok">
  <svg viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
  <div>
    <b class="t">Phase 3 Complete!</b>
    <p>Your CI/CD pipeline is now fully active, secure, and production ready.</p>
  </div>
</div>

<div class="pager">
  <a href="part-3-ec2-remote-deployment-engine.html">
    <small>← Previous Chapter</small>
    EC2 Remote Deployment &amp; Container Replacement Engine
  </a>
  <a class="r" href="part-1-aws-iam-ecr-github-secrets.html">
    <small>Restart Series ↺</small>
    Back to Part 1: IAM, ECR &amp; Secrets
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
    write_lab("part-4-end-to-end-pipeline-verification.html", get_part4_html())
