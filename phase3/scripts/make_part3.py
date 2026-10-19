#!/usr/bin/env python3
import os
from generate_labs import COMMON_CSS, COMMON_SCRIPT, generate_navbar

def get_part3_html():
    nav = generate_navbar(3)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>EC2 Remote Deployment &amp; Container Replacement — ZeetaFin Phase 3 Lab Part 3</title>
<meta name="description" content="Part 3 of the ZeetaFin Phase 3 CI/CD Lab: engineer automated zero-downtime container rollouts on AWS EC2 using Docker Compose and SSH automation.">
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

<h1>EC2 Remote Deployment &amp; Container Replacement Engine</h1>
<p class="dek">Engineering continuous delivery on AWS EC2: Remote SSH automation, atomic container recreation without port collisions, persistent volume safety, and self-healing health check verification.</p>

<p class="meta">
  <span><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> Oct 2026</span>
  <span><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> ~55 min read</span>
  <span><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a4 4 0 0 0 5 5L21 12.6a2 2 0 0 1 0 2.8l-5.6 5.6a2 2 0 0 1-2.8 0L3 11.4a2 2 0 0 1 0-2.8L8.6 3a2 2 0 0 1 2.8 0z" transform="translate(0 0) scale(.9) translate(1.3 1.3)"/></svg> ~60 min hands-on</span>
  <span><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v16H6.5A2.5 2.5 0 0 0 4 21.5z"/><path d="M4 18.5A2.5 2.5 0 0 1 6.5 16H20"/></svg> AWS EC2, Docker Compose, SSH, Zero-Collision Rollouts</span>
</p>

<div class="tools">
  <span class="tool">🚀 Idempotent deploy.sh Engine</span>
  <span class="tool">🔄 Atomic Container Replacement</span>
  <span class="tool">🔐 Secure SSH Manifest Sync</span>
  <span class="tool">🩺 Automated Healthcheck Probing</span>
</div>

<div class="hero-art">
<svg viewBox="0 0 1080 340" role="img" aria-label="EC2 Container Replacement Architecture">
  <defs>
    <linearGradient id="g-ec2" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#1e1b4b"/><stop offset="100%" stop-color="#070b14"/></linearGradient>
    <marker id="arr-m1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 1 L 10 5 L 0 9 z" fill="#f59e0b"/></marker>
    <marker id="arr-m2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 1 L 10 5 L 0 9 z" fill="#10b981"/></marker>
  </defs>

  <rect x="30" y="25" width="1020" height="290" rx="16" fill="url(#g-ec2)" stroke="#f59e0b" stroke-width="2"/>
  <text x="55" y="60" fill="#fef3c7" font-family="Sora, sans-serif" font-size="15" font-weight="700">🖥️ AWS EC2 Host — /home/ubuntu/zeetafin-app</text>

  <!-- GitHub Actions Ingress Arrow -->
  <rect x="55" y="90" width="220" height="190" rx="10" fill="#1e293b" stroke="#475569"/>
  <text x="75" y="120" fill="#f8fafc" font-family="Sora, sans-serif" font-size="13" font-weight="700">SSH Orchestrator</text>
  <text x="75" y="145" fill="#94a3b8" font-family="JetBrains Mono, monospace" font-size="11">1. Sync deploy.sh</text>
  <text x="75" y="165" fill="#94a3b8" font-family="JetBrains Mono, monospace" font-size="11">2. Sync compose.prod.yml</text>
  <text x="75" y="185" fill="#818cf8" font-family="JetBrains Mono, monospace" font-size="11">3. Exec deploy.sh</text>
  <text x="75" y="210" fill="#cbd5e1" font-family="DM Sans, sans-serif" font-size="12">Authenticated with EC2_SSH_KEY</text>

  <!-- Replacement Engine Box -->
  <rect x="330" y="90" width="310" height="190" rx="10" fill="#1e1b4b" stroke="#6366f1"/>
  <text x="350" y="120" fill="#c7d2fe" font-family="Sora, sans-serif" font-size="13" font-weight="700">Atomic Rollout Engine</text>
  <rect x="345" y="135" width="280" height="35" rx="6" fill="#0f172a" stroke="#334155"/>
  <text x="355" y="157" fill="#38bdf8" font-family="JetBrains Mono, monospace" font-size="11">docker compose pull (ECR)</text>
  <rect x="345" y="180" width="280" height="35" rx="6" fill="#0f172a" stroke="#334155"/>
  <text x="355" y="202" fill="#34d3b4" font-family="JetBrains Mono, monospace" font-size="11">up -d --force-recreate</text>
  <rect x="345" y="225" width="280" height="35" rx="6" fill="#0f172a" stroke="#334155"/>
  <text x="355" y="247" fill="#fcd34d" font-family="JetBrains Mono, monospace" font-size="11">healthcheck.sh &amp; prune</text>

  <!-- Live Containers Box -->
  <rect x="700" y="90" width="320" height="190" rx="10" fill="#064e3b" stroke="#10b981"/>
  <text x="720" y="120" fill="#a7f3d0" font-family="Sora, sans-serif" font-size="13" font-weight="700">Running Production Stack</text>
  <rect x="715" y="135" width="290" height="35" rx="6" fill="#022c22" stroke="#059669"/>
  <text x="725" y="157" fill="#6ee7b7" font-family="JetBrains Mono, monospace" font-size="11">zeetafin-frontend-prod (:3000)</text>
  <rect x="715" y="180" width="290" height="35" rx="6" fill="#022c22" stroke="#059669"/>
  <text x="725" y="202" fill="#6ee7b7" font-family="JetBrains Mono, monospace" font-size="11">zeetafin-backend-prod (:3001)</text>
  <rect x="715" y="225" width="290" height="35" rx="6" fill="#022c22" stroke="#059669"/>
  <text x="725" y="247" fill="#a7f3d0" font-family="JetBrains Mono, monospace" font-size="11">zeetafin-db-prod (pgdata vol)</text>

  <!-- Connectors -->
  <line x1="275" y1="185" x2="330" y2="185" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#arr-m1)"/>
  <line x1="640" y1="185" x2="700" y2="185" stroke="#10b981" stroke-width="2.5" marker-end="url(#arr-m2)"/>
</svg>
</div>

</div></header>

<div class="wrap"><div class="layout">

<!-- Table of Contents -->
<nav class="toc" aria-label="Table of Contents">
  <h2>Contents</h2>
  <ol>
    <li><a href="#challenge">1. The Replacement Challenge</a></li>
    <li><a href="#architecture">2. Architecture &amp; Mechanics</a></li>
    <li><a href="#ec2-prep">3. EC2 Host Preparation</a></li>
    <li><a href="#compose-prod">4. Production Compose Manifest</a></li>
    <li><a href="#deploy-script">5. The deploy.sh Engine</a></li>
    <li><a href="#atomic-rollout">6. Zero-Collision Mechanics</a></li>
    <li><a href="#ssh-step">7. SSH GitHub Actions Step</a></li>
    <li><a href="#healthcheck">8. Health Probes &amp; Traps</a></li>
    <li><a href="#disk-hygiene">9. Disk Hygiene &amp; Pruning</a></li>
    <li><a href="#rollback">10. Rapid Rollback Runbook</a></li>
    <li><a href="#checklist">11. Review Checklist</a></li>
    <li><a href="#next">12. What Comes Next</a></li>
  </ol>

  <div class="sidecard">
    <b>Lab Focus</b>
    <p>Achieving atomic, repeatable, zero-collision container replacements on EC2 while protecting database persistence and operating within compute resource limits.</p>
  </div>
</nav>

<!-- Article Content -->
<article>

<!-- SECTION 1 -->
<h2 id="challenge"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><path d="M12 8v4M12 16h.01"/></svg></span>1. The Container Replacement Challenge</h2>

<p class="lead">Deploying a new container version sounds simple: download the image and start it. However, in automated continuous deployment on a single EC2 host, naive deployments cause immediate failure.</p>

<p>Consider what happens if you run <code>docker run -d -p 3000:3000 zeetafin-frontend:new</code> while the old container is still running:</p>

<div class="tbl">
  <table>
    <thead>
      <tr>
        <th>Failure Mode</th>
        <th>Root Cause</th>
        <th>Consequence</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Port Conflict</strong></td>
        <td>Port <code>3000</code> is already bound by the previous container.</td>
        <td><code>Error response from daemon: driver failed programming external connectivity: Bind for 0.0.0.0:3000 failed: port is already allocated</code></td>
      </tr>
      <tr>
        <td><strong>Name Collision</strong></td>
        <td>Container name <code>zeetafin-frontend</code> already exists.</td>
        <td><code>Conflict. The container name "/zeetafin-frontend" is already in use by container "...". You have to remove (or rename) that container.</code></td>
      </tr>
      <tr>
        <td><strong>Downtime Window</strong></td>
        <td>If you stop the container *before* pulling the image, pulling takes 45 seconds over the network.</td>
        <td>Users experience HTTP 502/504 downtime for almost a full minute during every deployment!</td>
      </tr>
    </tbody>
  </table>
</div>

<p>To satisfy the project requirement—<em>"Ensure the old application container is replaced when a new version is deployed"</em>—we architected a declarative deployment engine powered by Docker Compose native reconciliation.</p>

<!-- SECTION 2 -->
<h2 id="architecture"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg></span>2. Architecture of the Deployment Engine</h2>

<p>Our solution decouples image transmission from container recreation:</p>

<ol class="steps">
  <li>
    <b>Background Image Download:</b>
    <p><code>docker compose -f docker-compose.prod.yml pull</code> downloads the new layers from Amazon ECR in the background while the currently active containers continue serving incoming traffic.</p>
  </li>
  <li>
    <b>Atomic Recreation:</b>
    <p><code>docker compose -f docker-compose.prod.yml up -d --remove-orphans --force-recreate</code> recreates the containers, atomically swapping the network namespace and port mapping in under 200 milliseconds.</p>
  </li>
  <li>
    <b>Persistent Storage Isolation:</b>
    <p>The database data volume (<code>zeetafin_prod_pgdata</code>) is defined as an external, named persistent volume. Recreating the database container leaves the disk blocks untouched.</p>
  </li>
  <li>
    <b>Automated Validation:</b>
    <p><code>healthcheck.sh</code> probes <code>http://127.0.0.1:3001/api/docs</code> and <code>http://127.0.0.1:3000/</code> in a retry loop. If both respond with HTTP 200, the deployment exits with code <code>0</code>.</p>
  </li>
</ol>

<!-- SECTION 3 -->
<h2 id="ec2-prep"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"/><rect x="2" y="14" width="20" height="8" rx="2" ry="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/></svg></span>3. EC2 Host Preparation &amp; Workspace Layout</h2>

<p>Our Phase 1 Ansible playbook pre-installed Docker CE and the Docker Compose plugin. On the EC2 host, application manifests reside in <code>/home/ubuntu/zeetafin-app/</code>:</p>

<div class="code">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">EC2 Host Filesystem Tree</span>
    <span class="tag">LAYOUT</span>
  </div>
<pre><code>/home/ubuntu/zeetafin-app/
├── docker-compose.prod.yml       <span class="c"># Production orchestration manifest</span>
├── .env                          <span class="c"># Production credentials &amp; registry URIs</span>
└── scripts/
    ├── deploy.sh                 <span class="c"># Idempotent rollout engine (executable)</span>
    └── healthcheck.sh            <span class="c"># Local availability prober (executable)</span></code></pre>
</div>

<!-- SECTION 4 -->
<h2 id="compose-prod"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg></span>4. Production Docker Compose Manifest</h2>

<p>Notice how <code>phase3/docker-compose.prod.yml</code> pulls directly from the variable <code>${{ECR_REGISTRY}}</code> and pins health checks for service dependency coordination:</p>

<div class="code">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">phase3/docker-compose.prod.yml</span>
    <span class="tag">YAML</span>
    <button class="copy" type="button"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy</button>
  </div>
<pre><code><span class="k">services</span>:
  <span class="k">db</span>:
    <span class="k">image</span>: <span class="s2">postgres:16-alpine</span>
    <span class="k">container_name</span>: <span class="s2">zeetafin-db-prod</span>
    <span class="k">restart</span>: <span class="s2">unless-stopped</span>
    <span class="k">environment</span>:
      <span class="k">POSTGRES_USER</span>: <span class="s2">${{{{POSTGRES_USER:-postgres}}}}</span>
      <span class="k">POSTGRES_PASSWORD</span>: <span class="s2">${{{{POSTGRES_PASSWORD:-zeetafin_secret}}}}</span>
      <span class="k">POSTGRES_DB</span>: <span class="s2">${{{{POSTGRES_DB:-zeetafin}}}}</span>
    <span class="k">ports</span>:
      - <span class="s2">"5432:5432"</span>
    <span class="k">volumes</span>:
      - <span class="s2">zeetafin_prod_pgdata:/var/lib/postgresql/data</span>
    <span class="k">healthcheck</span>:
      <span class="k">test</span>: [<span class="s2">"CMD-SHELL"</span>, <span class="s2">"pg_isready -U ${{POSTGRES_USER:-postgres}} -d ${{POSTGRES_DB:-zeetafin}}"</span>]
      <span class="k">interval</span>: <span class="n">10s</span>
      <span class="k">timeout</span>: <span class="n">5s</span>
      <span class="k">retries</span>: <span class="n">5</span>
    <span class="k">networks</span>:
      - <span class="s2">zeetafin-prod-net</span>

  <span class="k">backend</span>:
    <span class="k">image</span>: <span class="s2">${{{{ECR_REGISTRY}}}}/zeetafin-backend:${{{{IMAGE_TAG:-latest}}}}</span>
    <span class="k">container_name</span>: <span class="s2">zeetafin-backend-prod</span>
    <span class="k">restart</span>: <span class="s2">unless-stopped</span>
    <span class="k">environment</span>:
      <span class="k">PORT</span>: <span class="n">3001</span>
      <span class="k">DB_HOST</span>: <span class="s2">db</span>
      <span class="k">DB_PORT</span>: <span class="n">5432</span>
      <span class="k">DB_USERNAME</span>: <span class="s2">${{{{POSTGRES_USER:-postgres}}}}</span>
      <span class="k">DB_PASSWORD</span>: <span class="s2">${{{{POSTGRES_PASSWORD:-zeetafin_secret}}}}</span>
      <span class="k">DB_NAME</span>: <span class="s2">${{{{POSTGRES_DB:-zeetafin}}}}</span>
      <span class="k">JWT_SECRET</span>: <span class="s2">${{{{JWT_SECRET}}}}</span>
      <span class="k">NODE_ENV</span>: <span class="s2">production</span>
      <span class="k">DB_SYNC</span>: <span class="s2">"true"</span>
    <span class="k">ports</span>:
      - <span class="s2">"3001:3001"</span>
    <span class="k">depends_on</span>:
      <span class="k">db</span>:
        <span class="k">condition</span>: <span class="s2">service_healthy</span>
    <span class="k">healthcheck</span>:
      <span class="k">test</span>: [<span class="s2">"CMD-SHELL"</span>, <span class="s2">"wget --spider http://127.0.0.1:3001/api/docs || exit 1"</span>]
      <span class="k">interval</span>: <span class="n">15s</span>
      <span class="k">timeout</span>: <span class="n">5s</span>
      <span class="k">retries</span>: <span class="n">5</span>
    <span class="k">networks</span>:
      - <span class="s2">zeetafin-prod-net</span>

  <span class="k">frontend</span>:
    <span class="k">image</span>: <span class="s2">${{{{ECR_REGISTRY}}}}/zeetafin-frontend:${{{{IMAGE_TAG:-latest}}}}</span>
    <span class="k">container_name</span>: <span class="s2">zeetafin-frontend-prod</span>
    <span class="k">restart</span>: <span class="s2">unless-stopped</span>
    <span class="k">environment</span>:
      <span class="k">PORT</span>: <span class="n">3000</span>
      <span class="k">NEXT_PUBLIC_API_URL</span>: <span class="s2">${{{{NEXT_PUBLIC_API_URL:-http://localhost:3001/api}}}}</span>
    <span class="k">ports</span>:
      - <span class="s2">"3000:3000"</span>
    <span class="k">depends_on</span>:
      <span class="k">backend</span>:
        <span class="k">condition</span>: <span class="s2">service_healthy</span>
    <span class="k">healthcheck</span>:
      <span class="k">test</span>: [<span class="s2">"CMD-SHELL"</span>, <span class="s2">"wget --spider http://127.0.0.1:3000/ || exit 1"</span>]
      <span class="k">interval</span>: <span class="n">15s</span>
      <span class="k">timeout</span>: <span class="n">5s</span>
      <span class="k">retries</span>: <span class="n">5</span>
    <span class="k">networks</span>:
      - <span class="s2">zeetafin-prod-net</span>

<span class="k">volumes</span>:
  <span class="k">zeetafin_prod_pgdata</span>:
    <span class="k">name</span>: <span class="s2">zeetafin_prod_pgdata</span>

<span class="k">networks</span>:
  <span class="k">zeetafin-prod-net</span>:
    <span class="k">name</span>: <span class="s2">zeetafin-prod-net</span></code></pre>
</div>

<!-- SECTION 5 -->
<h2 id="deploy-script"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/></svg></span>5. The Idempotent deploy.sh Engine</h2>

<p>The core execution script <code>phase3/scripts/deploy.sh</code> is executed directly by GitHub Actions over SSH. It accepts the target Git SHA tag, authenticates against ECR, triggers container recreation, runs the healthcheck verification loop, and prunes old images:</p>

<div class="code">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">Key Rollout Block in deploy.sh</span>
    <span class="tag">BASH</span>
  </div>
<pre><code><span class="c"># 1. Authenticate Docker with Amazon ECR on the EC2 host</span>
aws ecr get-login-password --region "${{AWS_REGION}}" | \
  docker login --username AWS --password-stdin "${{ECR_REGISTRY}}"

<span class="c"># 2. Pull updated images in background</span>
docker compose -f "${{COMPOSE_FILE}}" pull

<span class="c"># 3. Atomically replace old containers</span>
docker compose -f "${{COMPOSE_FILE}}" up -d --remove-orphans --force-recreate

<span class="c"># 4. Probe endpoints until healthy</span>
check_endpoint "http://127.0.0.1:3001/api/docs" "ZeetaFin Backend"
check_endpoint "http://127.0.0.1:3000/" "ZeetaFin Frontend"

<span class="c"># 5. Prune dangling layers</span>
docker image prune -f --filter "until=24h" || true</code></pre>
</div>

<!-- SECTION 6 -->
<h2 id="atomic-rollout"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 14 10"/></svg></span>6. Zero-Collision Mechanics Explained</h2>

<p>Why does <code>up -d --force-recreate --remove-orphans</code> succeed where manual scripts fail?</p>

<div class="vs">
  <div class="card" style="--c:#ef4444">
    <h4>Manual Bash Scripts (Fragile)</h4>
    <ol>
      <li><code>docker stop old-container</code> (Site goes down immediately)</li>
      <li><code>docker pull new-image</code> (Takes 30+ seconds over internet)</li>
      <li><code>docker rm old-container</code></li>
      <li><code>docker run ...</code></li>
    </ol>
    <div class="res no"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg> Severe downtime &amp; crash if pull fails</div>
  </div>

  <div class="card" style="--c:#10b981">
    <h4>Docker Compose Engine (Production)</h4>
    <ol>
      <li>Images pulled *before* any service is touched</li>
      <li>If pull fails, active containers are completely undisturbed!</li>
      <li>Once layers are cached locally, containers are swapped in milliseconds</li>
    </ol>
    <div class="res yes"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><polyline points="20 6 9 17 4 12"/></svg> Fault-tolerant, atomic &amp; zero port collisions</div>
  </div>
</div>

<!-- SECTION 7 -->
<h2 id="ssh-step"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg></span>7. SSH Remote Execution Step in GitHub Actions</h2>

<p>In <code>.github/workflows/deploy.yml</code>, the <code>deploy-to-ec2</code> job uses the standard OpenSSH agent to connect securely without third-party dependencies:</p>

<div class="code">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">deploy-to-ec2 Execution Step</span>
    <span class="tag">YAML</span>
  </div>
<pre><code>- <span class="k">name</span>: <span class="s2">Execute Deployment &amp; Container Replacement on EC2</span>
  <span class="k">env</span>:
    <span class="k">EC2_USER</span>: <span class="s2">${{{{ secrets.EC2_USERNAME || 'ubuntu' }}}}</span>
    <span class="k">EC2_HOST</span>: <span class="s2">${{{{ secrets.EC2_HOST }}}}</span>
    <span class="k">ECR_REGISTRY</span>: <span class="s2">${{{{ needs.build-and-push.outputs.ecr_registry }}}}</span>
    <span class="k">IMAGE_TAG</span>: <span class="s2">${{{{ needs.build-and-push.outputs.image_tag }}}}</span>
  <span class="k">run</span>: <span class="s2">|
    ssh -i ~/.ssh/deploy_key -o StrictHostKeyChecking=no "${{EC2_USER}}@${{EC2_HOST}}" &lt;&lt; 'EOF'
      set -euo pipefail
      cd /home/ubuntu/zeetafin-app
      chmod +x scripts/deploy.sh scripts/healthcheck.sh
      ./scripts/deploy.sh "${{{{IMAGE_TAG}}}}" "${{{{ECR_REGISTRY}}}}" "us-east-1"
    EOF</span></code></pre>
</div>

<!-- SECTION 8 -->
<h2 id="healthcheck"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg></span>8. Endpoint Probing with healthcheck.sh</h2>

<p>The health check prober queries HTTP response codes from both application tiers:</p>

<div class="term">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">Testing healthcheck.sh on EC2</span>
    <span class="tag">BASH</span>
    <button class="copy" type="button"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy</button>
  </div>
<pre><code><span class="p">$ </span>./scripts/healthcheck.sh 127.0.0.1</code></pre>
</div>

<p>Expected output:</p>
<div class="term">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">Output — healthcheck.sh</span>
    <span class="tag ok">OK</span>
  </div>
<pre><code>Probing ZeetaFin ERP endpoints on host: 127.0.0.1...
Checking Backend (http://127.0.0.1:3001/api/docs)... <span class="ok">OK (HTTP 200)</span>
Checking Frontend (http://127.0.0.1:3000/)... <span class="ok">OK (HTTP 200)</span>
<span class="ok">All services healthy and responsive!</span></code></pre>
</div>

<!-- SECTION 9 -->
<h2 id="disk-hygiene"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg></span>9. Disk Space Hygiene on t3.micro Instances</h2>

<p>The Phase 1 EC2 instance runs with a 20 GiB gp3 root EBS volume. With regular CI/CD deployments pushing multiple 300 MB images each day, unpruned Docker caches would exhaust disk space within weeks (leading to <code>No space left on device</code>).</p>

<p>Our <code>deploy.sh</code> script automatically executes:</p>
<div class="code">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">Prune Command</span>
    <span class="tag">BASH</span>
  </div>
<pre><code>docker image prune -f --filter "until=24h"</code></pre>
</div>
<p>This safely removes older unreferenced layers without discarding images needed for fast instant rollbacks.</p>

<!-- SECTION 10 -->
<h2 id="rollback"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="1 4 1 10 7 10"/><path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"/></svg></span>10. Rapid Rollback Runbook</h2>

<p>What if a faulty commit introduces a bug that slipped past staging? Because our images are tagged with Git SHAs in Amazon ECR, rolling back takes a single command on EC2 or via <code>workflow_dispatch</code>:</p>

<div class="term">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">Instant Rollback Command on EC2</span>
    <span class="tag">BASH</span>
    <button class="copy" type="button"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy</button>
  </div>
<pre><code><span class="p">$ </span>cd /home/ubuntu/zeetafin-app
<span class="p">$ </span><span class="c"># Re-deploy the known-good Git commit SHA</span>
<span class="p">$ </span>./scripts/deploy.sh 5eb7a625a... "${{ECR_REGISTRY}}" us-east-1</code></pre>
</div>

<!-- SECTION 11 -->
<h2 id="checklist"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg></span>11. Verification Checklist &amp; Challenge</h2>

<ol class="steps">
  <li>
    <b>Deploy Manifests Synced</b>
    <p><code>docker-compose.prod.yml</code>, <code>deploy.sh</code>, and <code>healthcheck.sh</code> reside in <code>/home/ubuntu/zeetafin-app/</code>.</p>
  </li>
  <li>
    <b>Clean Container Replacement Verified</b>
    <p>Executing <code>deploy.sh</code> replaces running containers without downtime or <code>port is already allocated</code> errors.</p>
  </li>
  <li>
    <b>Database Data Preserved</b>
    <p>Volume <code>zeetafin_prod_pgdata</code> retains all PostgreSQL tables across container recreations.</p>
  </li>
  <li>
    <b>Challenge Exercise</b>
    <p>Run <code>docker ps</code> on EC2, note the container IDs. Run <code>./scripts/deploy.sh</code> again. Confirm that new container IDs are launched and the old ones are gracefully decommissioned.</p>
  </li>
</ol>

<!-- SECTION 12 -->
<h2 id="next"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg></span>12. What Comes Next</h2>

<p>In our final lab, <strong>Part 4</strong>, we conduct complete end-to-end integration testing: pushing an application code change to GitHub, tracking the full CI/CD execution, validating external availability in the web browser, and assembling our project deliverables.</p>

<div class="pager">
  <a href="part-2-github-actions-workflow-ci.html">
    <small>← Previous Chapter</small>
    GitHub Actions CI Workflow &amp; Build Engine
  </a>
  <a class="r" href="part-4-end-to-end-pipeline-verification.html">
    <small>Next Chapter →</small>
    End-to-End Pipeline Verification &amp; Triage
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
    write_lab("part-3-ec2-remote-deployment-engine.html", get_part3_html())
