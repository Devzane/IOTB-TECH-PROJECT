#!/usr/bin/env python3
import os
from generate_labs import COMMON_CSS, COMMON_SCRIPT, generate_navbar

def get_part2_html():
    nav = generate_navbar(2)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>GitHub Actions CI &amp; Container Build Engine — ZeetaFin Phase 3 Lab Part 2</title>
<meta name="description" content="Part 2 of the ZeetaFin Phase 3 CI/CD Lab: build multi-stage Docker containers with Buildx caching and push immutable SHA-tagged artifacts to Amazon ECR.">
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

<h1>GitHub Actions CI Workflow &amp; Container Build Engine</h1>
<p class="dek">Constructing automated GitHub Actions workflows: Multi-stage Docker Buildx layer caching, AWS credentials configuration, immutable commit-SHA tagging, and publishing to Amazon ECR.</p>

<p class="meta">
  <span><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> Oct 2026</span>
  <span><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> ~50 min read</span>
  <span><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a4 4 0 0 0 5 5L21 12.6a2 2 0 0 1 0 2.8l-5.6 5.6a2 2 0 0 1-2.8 0L3 11.4a2 2 0 0 1 0-2.8L8.6 3a2 2 0 0 1 2.8 0z" transform="translate(0 0) scale(.9) translate(1.3 1.3)"/></svg> ~60 min hands-on</span>
  <span><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v16H6.5A2.5 2.5 0 0 0 4 21.5z"/><path d="M4 18.5A2.5 2.5 0 0 1 6.5 16H20"/></svg> GitHub Actions, Docker Buildx, Amazon ECR, BuildKit</span>
</p>

<div class="tools">
  <span class="tool">⚙️ GitHub Actions Workflow</span>
  <span class="tool">🐳 Docker Buildx &amp; GHA Cache</span>
  <span class="tool">🏷️ Git SHA Tagging Strategy</span>
  <span class="tool">📦 Amazon ECR Publishing</span>
</div>

<div class="hero-art">
<svg viewBox="0 0 1080 340" role="img" aria-label="GitHub Actions CI Build and Push Pipeline">
  <defs>
    <linearGradient id="g-stage" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#1e1b4b"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <marker id="arr-blue2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 1 L 10 5 L 0 9 z" fill="#818cf8"/></marker>
    <marker id="arr-green2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 1 L 10 5 L 0 9 z" fill="#34d3b4"/></marker>
  </defs>

  <rect x="30" y="30" width="1020" height="280" rx="16" fill="url(#g-stage)" stroke="#334155" stroke-width="2"/>
  <text x="50" y="65" fill="#f8fafc" font-family="Sora, sans-serif" font-size="15" font-weight="700">⚙️ Job: build-and-push (GitHub Actions ubuntu-latest)</text>

  <!-- Step 1: Checkout -->
  <rect x="50" y="90" width="170" height="180" rx="10" fill="#1e293b" stroke="#475569"/>
  <circle cx="75" cy="115" r="12" fill="#6366f1"/>
  <text x="71" y="120" fill="#fff" font-family="Sora, sans-serif" font-size="12" font-weight="700">1</text>
  <text x="95" y="120" fill="#f8fafc" font-family="Sora, sans-serif" font-size="13" font-weight="700">Checkout</text>
  <text x="65" y="150" fill="#94a3b8" font-family="JetBrains Mono, monospace" font-size="11">actions/checkout@v4</text>
  <text x="65" y="175" fill="#cbd5e1" font-family="DM Sans, sans-serif" font-size="12">Pulls repository source tree &amp; commit SHA</text>

  <!-- Step 2: Auth -->
  <rect x="250" y="90" width="190" height="180" rx="10" fill="#1e293b" stroke="#475569"/>
  <circle cx="275" cy="115" r="12" fill="#6366f1"/>
  <text x="271" y="120" fill="#fff" font-family="Sora, sans-serif" font-size="12" font-weight="700">2</text>
  <text x="295" y="120" fill="#f8fafc" font-family="Sora, sans-serif" font-size="13" font-weight="700">AWS Auth</text>
  <text x="265" y="150" fill="#818cf8" font-family="JetBrains Mono, monospace" font-size="11">configure-aws-cred</text>
  <text x="265" y="170" fill="#818cf8" font-family="JetBrains Mono, monospace" font-size="11">amazon-ecr-login</text>
  <text x="265" y="195" fill="#cbd5e1" font-family="DM Sans, sans-serif" font-size="12">Generates temporary Docker auth token</text>

  <!-- Step 3: Build & Cache -->
  <rect x="470" y="90" width="270" height="180" rx="10" fill="#1e293b" stroke="#6366f1"/>
  <circle cx="495" cy="115" r="12" fill="#0ea5e9"/>
  <text x="491" y="120" fill="#fff" font-family="Sora, sans-serif" font-size="12" font-weight="700">3</text>
  <text x="515" y="120" fill="#f8fafc" font-family="Sora, sans-serif" font-size="13" font-weight="700">Docker Buildx (Multi-Stage)</text>
  <rect x="485" y="140" width="240" height="40" rx="6" fill="#0f172a" stroke="#334155"/>
  <text x="495" y="165" fill="#38bdf8" font-family="JetBrains Mono, monospace" font-size="11">backend (NestJS 10)</text>
  <rect x="485" y="190" width="240" height="40" rx="6" fill="#0f172a" stroke="#334155"/>
  <text x="495" y="215" fill="#38bdf8" font-family="JetBrains Mono, monospace" font-size="11">frontend (Next.js 14)</text>
  <text x="485" y="250" fill="#a5b4fc" font-family="JetBrains Mono, monospace" font-size="10">cache-from: type=gha</text>

  <!-- Step 4: Push to ECR -->
  <rect x="770" y="90" width="250" height="180" rx="10" fill="#064e3b" stroke="#10b981"/>
  <circle cx="795" cy="115" r="12" fill="#10b981"/>
  <text x="791" y="120" fill="#fff" font-family="Sora, sans-serif" font-size="12" font-weight="700">4</text>
  <text x="815" y="120" fill="#ecfdf5" font-family="Sora, sans-serif" font-size="13" font-weight="700">Amazon ECR Registry</text>
  <text x="785" y="150" fill="#a7f3d0" font-family="JetBrains Mono, monospace" font-size="11">zeetafin-backend:${{SHA}}</text>
  <text x="785" y="170" fill="#a7f3d0" font-family="JetBrains Mono, monospace" font-size="11">zeetafin-backend:latest</text>
  <text x="785" y="200" fill="#6ee7b7" font-family="JetBrains Mono, monospace" font-size="11">zeetafin-frontend:${{SHA}}</text>
  <text x="785" y="220" fill="#6ee7b7" font-family="JetBrains Mono, monospace" font-size="11">zeetafin-frontend:latest</text>

  <!-- Connectors -->
  <line x1="220" y1="180" x2="250" y2="180" stroke="#818cf8" stroke-width="2.5" marker-end="url(#arr-blue2)"/>
  <line x1="440" y1="180" x2="470" y2="180" stroke="#818cf8" stroke-width="2.5" marker-end="url(#arr-blue2)"/>
  <line x1="740" y1="180" x2="770" y2="180" stroke="#34d3b4" stroke-width="2.5" marker-end="url(#arr-green2)"/>
</svg>
</div>

</div></header>

<div class="wrap"><div class="layout">

<!-- Table of Contents -->
<nav class="toc" aria-label="Table of Contents">
  <h2>Contents</h2>
  <ol>
    <li><a href="#overview">1. CI Objectives &amp; Principles</a></li>
    <li><a href="#triggers">2. Triggers &amp; Path Filtering</a></li>
    <li><a href="#concurrency">3. Concurrency Controls</a></li>
    <li><a href="#buildx">4. Docker Buildx &amp; GHA Cache</a></li>
    <li><a href="#aws-auth">5. ECR Auth in GitHub Actions</a></li>
    <li><a href="#tagging">6. Tagging: SHA vs. Latest</a></li>
    <li><a href="#workflow-file">7. Complete Workflow Manifest</a></li>
    <li><a href="#live-logs">8. Inspecting Build Execution</a></li>
    <li><a href="#ecr-verify">9. Validating Images in ECR</a></li>
    <li><a href="#troubleshooting">10. CI Troubleshooting</a></li>
    <li><a href="#checklist">11. Review Checklist</a></li>
    <li><a href="#next">12. What Comes Next</a></li>
  </ol>

  <div class="sidecard">
    <b>Lab Focus</b>
    <p>Automating Docker container builds, layer caching, and secure container image delivery to Amazon ECR on every git commit.</p>
  </div>
</nav>

<!-- Article Content -->
<article>

<!-- SECTION 1 -->
<h2 id="overview"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg></span>1. CI Objectives &amp; Core Principles</h2>

<p class="lead">Continuous Integration is the discipline of validating and packaging code on every merge so that deployment artifacts are always pre-built, tested, and ready for release. In Phase 3, our CI stage produces production container images and publishes them directly to Amazon ECR.</p>

<p>A production-ready CI pipeline adheres to four golden rules:</p>

<div class="cards">
  <div class="card" style="--c:#6366f1">
    <h4>1. Immutable Artifacts</h4>
    <p>Every single build produces an image tagged with the exact 40-character Git commit SHA. You can always trace a running container back to the exact commit that generated it.</p>
  </div>
  <div class="card" style="--c:#0ea5e9">
    <h4>2. Layer Caching</h4>
    <p>Builds must not compile dependencies from scratch on every run. GitHub Actions Buildx caching (<code>type=gha</code>) cuts build durations from minutes to seconds.</p>
  </div>
  <div class="card" style="--c:#f59e0b">
    <h4>3. Path Filtering</h4>
    <p>Commits modifying only documentation or Terraform manifests should never trigger resource-intensive Docker image builds.</p>
  </div>
  <div class="card" style="--c:#10b981">
    <h4>4. Clean Job Outputs</h4>
    <p>The build job passes the resolved registry URI and image tag downstream to the deployment job via <code>outputs</code>.</p>
  </div>
</div>

<!-- SECTION 2 -->
<h2 id="triggers"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg></span>2. Event Triggers &amp; Path Filtering</h2>

<p>Without path filters, updating a <code>README.md</code> or adding a diagram causes GitHub Actions to rebuild and push entire multi-hundred-megabyte Docker images to ECR. We enforce fine-grained triggers in <code>.github/workflows/deploy.yml</code>:</p>

<div class="code">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">.github/workflows/deploy.yml</span>
    <span class="tag">YAML</span>
    <button class="copy" type="button"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy</button>
  </div>
<pre><code><span class="k">on</span>:
  <span class="k">push</span>:
    <span class="k">branches</span>:
      - <span class="s2">main</span>
    <span class="k">paths</span>:
      - <span class="s2">'phase2/**'</span>
      - <span class="s2">'phase3/**'</span>
      - <span class="s2">'.github/workflows/**'</span>
      - <span class="s2">'Dockerfile'</span>
      - <span class="s2">'docker-compose*.yml'</span>
  <span class="k">workflow_dispatch</span>:
    <span class="k">inputs</span>:
      <span class="k">environment</span>:
        <span class="k">description</span>: <span class="s2">'Target deployment environment'</span>
        <span class="k">required</span>: <span class="n">true</span>
        <span class="k">default</span>: <span class="s2">'production'</span>
      <span class="k">tag_override</span>:
        <span class="k">description</span>: <span class="s2">'Custom tag override (optional)'</span>
        <span class="k">required</span>: <span class="n">false</span>
        <span class="k">default</span>: <span class="s2">''</span></code></pre>
</div>

<!-- SECTION 3 -->
<h2 id="concurrency"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></span>3. Concurrency &amp; Race Condition Prevention</h2>

<p>What happens if two developers push commits 10 seconds apart? Without concurrency control, both workflows run in parallel. A slower build from an earlier commit could deploy <em>after</em> the newer commit, reverting production to stale code.</p>

<p>We add a queue group so jobs execute serially:</p>

<div class="code">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">concurrency block</span>
    <span class="tag">YAML</span>
  </div>
<pre><code><span class="k">concurrency</span>:
  <span class="k">group</span>: <span class="s2">production-deployment</span>
  <span class="k">cancel-in-progress</span>: <span class="n">false</span></code></pre>
</div>

<p>Setting <code>cancel-in-progress: false</code> ensures every production rollout finishes cleanly before the next queued rollout begins.</p>

<!-- SECTION 4 -->
<h2 id="buildx"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"/><rect x="2" y="14" width="20" height="8" rx="2" ry="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/></svg></span>4. Docker Buildx &amp; GitHub Actions Layer Cache</h2>

<p>Docker Buildx leverages BuildKit under the hood. Standard Docker builds on CI throw away intermediate layer caches between runner runs. By setting <code>cache-from: type=gha</code> and <code>cache-to: type=gha,mode=max</code>, BuildKit persists unchanged <code>npm ci</code> layers inside GitHub's caching backend:</p>

<div class="code">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">build-push-action configuration</span>
    <span class="tag">YAML</span>
  </div>
<pre><code>- <span class="k">name</span>: <span class="s2">Set up Docker Buildx</span>
  <span class="k">uses</span>: <span class="s2">docker/setup-buildx-action@v3</span>

- <span class="k">name</span>: <span class="s2">Build &amp; Push Backend Image</span>
  <span class="k">uses</span>: <span class="s2">docker/build-push-action@v5</span>
  <span class="k">with</span>:
    <span class="k">context</span>: <span class="s2">./phase2/backend</span>
    <span class="k">file</span>: <span class="s2">./phase2/backend/Dockerfile</span>
    <span class="k">push</span>: <span class="n">true</span>
    <span class="k">tags</span>: <span class="s2">|
      ${{{{ steps.login-ecr.outputs.registry }}}}/zeetafin-backend:${{{{ steps.set-tag.outputs.tag }}}}
      ${{{{ steps.login-ecr.outputs.registry }}}}/zeetafin-backend:latest</span>
    <span class="k">cache-from</span>: <span class="s2">type=gha</span>
    <span class="k">cache-to</span>: <span class="s2">type=gha,mode=max</span></code></pre>
</div>

<!-- SECTION 5 -->
<h2 id="aws-auth"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg></span>5. Authenticating to Amazon ECR in CI</h2>

<p>Amazon ECR does not accept raw AWS Access Keys directly via <code>docker login</code>. ECR requires exchanging your IAM credentials for a short-lived authorization token (valid for 12 hours). The official AWS actions handle this handshake automatically:</p>

<div class="code">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">AWS Actions ECR Auth Step</span>
    <span class="tag">YAML</span>
  </div>
<pre><code>- <span class="k">name</span>: <span class="s2">Authenticate with AWS</span>
  <span class="k">uses</span>: <span class="s2">aws-actions/configure-aws-credentials@v4</span>
  <span class="k">with</span>:
    <span class="k">aws-access-key-id</span>: <span class="s2">${{{{ secrets.AWS_ACCESS_KEY_ID }}}}</span>
    <span class="k">aws-secret-access-key</span>: <span class="s2">${{{{ secrets.AWS_SECRET_ACCESS_KEY }}}}</span>
    <span class="k">aws-region</span>: <span class="s2">${{{{ secrets.AWS_REGION || 'us-east-1' }}}}</span>

- <span class="k">name</span>: <span class="s2">Log in to Amazon ECR</span>
  <span class="k">id</span>: <span class="s2">login-ecr</span>
  <span class="k">uses</span>: <span class="s2">aws-actions/amazon-ecr-login@v2</span></code></pre>
</div>

<p>Once <code>amazon-ecr-login</code> completes, <code>steps.login-ecr.outputs.registry</code> contains your full AWS account ECR URI (e.g. <code>123456789012.dkr.ecr.us-east-1.amazonaws.com</code>).</p>

<!-- SECTION 6 -->
<h2 id="tagging"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg></span>6. Dual Tagging: Commit SHA vs. Latest</h2>

<p>A classic DevOps anti-pattern is deploying solely with the <code>:latest</code> tag. If something breaks in production, what commit broke it? How do you roll back?</p>

<p>We implement a dual-tagging strategy:</p>
<ul>
  <li><code>:${{{{ github.sha }}}}</code>: The immutable release artifact. Never overwritten. Provides perfect traceability.</li>
  <li><code>:latest</code>: The rolling convenience tag. Updated on every successful build to point to the most recent mainline commit.</li>
</ul>

<!-- SECTION 7 -->
<h2 id="workflow-file"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg></span>7. The Build Job Manifest</h2>

<p>Here is the complete, isolated <code>build-and-push</code> job definition that powers the first stage of <code>.github/workflows/deploy.yml</code>:</p>

<div class="code">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">build-and-push Job Snippet</span>
    <span class="tag">YAML</span>
    <button class="copy" type="button"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy</button>
  </div>
<pre><code><span class="k">build-and-push</span>:
  <span class="k">name</span>: <span class="s2">Build &amp; Push Images to Amazon ECR</span>
  <span class="k">runs-on</span>: <span class="s2">ubuntu-latest</span>
  <span class="k">outputs</span>:
    <span class="k">ecr_registry</span>: <span class="s2">${{{{ steps.login-ecr.outputs.registry }}}}</span>
    <span class="k">image_tag</span>: <span class="s2">${{{{ steps.set-tag.outputs.tag }}}}</span>

  <span class="k">steps</span>:
    - <span class="k">name</span>: <span class="s2">Checkout Application Code</span>
      <span class="k">uses</span>: <span class="s2">actions/checkout@v4</span>

    - <span class="k">name</span>: <span class="s2">Set Image Tag</span>
      <span class="k">id</span>: <span class="s2">set-tag</span>
      <span class="k">run</span>: <span class="s2">|
        if [ -n "${{{{ github.event.inputs.tag_override }}}}" ]; then
          TAG="${{{{ github.event.inputs.tag_override }}}}"
        else
          TAG="${{{{ github.sha }}}}"
        fi
        echo "tag=${{TAG}}" &gt;&gt; "$GITHUB_OUTPUT"</span>

    - <span class="k">name</span>: <span class="s2">Set up Docker Buildx</span>
      <span class="k">uses</span>: <span class="s2">docker/setup-buildx-action@v3</span>

    - <span class="k">name</span>: <span class="s2">Authenticate with AWS</span>
      <span class="k">uses</span>: <span class="s2">aws-actions/configure-aws-credentials@v4</span>
      <span class="k">with</span>:
        <span class="k">aws-access-key-id</span>: <span class="s2">${{{{ secrets.AWS_ACCESS_KEY_ID }}}}</span>
        <span class="k">aws-secret-access-key</span>: <span class="s2">${{{{ secrets.AWS_SECRET_ACCESS_KEY }}}}</span>
        <span class="k">aws-region</span>: <span class="s2">${{{{ secrets.AWS_REGION || 'us-east-1' }}}}</span>

    - <span class="k">name</span>: <span class="s2">Log in to Amazon ECR</span>
      <span class="k">id</span>: <span class="s2">login-ecr</span>
      <span class="k">uses</span>: <span class="s2">aws-actions/amazon-ecr-login@v2</span>

    - <span class="k">name</span>: <span class="s2">Build &amp; Push Backend Image</span>
      <span class="k">uses</span>: <span class="s2">docker/build-push-action@v5</span>
      <span class="k">with</span>:
        <span class="k">context</span>: <span class="s2">./phase2/backend</span>
        <span class="k">file</span>: <span class="s2">./phase2/backend/Dockerfile</span>
        <span class="k">push</span>: <span class="n">true</span>
        <span class="k">tags</span>: <span class="s2">|
          ${{{{ steps.login-ecr.outputs.registry }}}}/zeetafin-backend:${{{{ steps.set-tag.outputs.tag }}}}
          ${{{{ steps.login-ecr.outputs.registry }}}}/zeetafin-backend:latest</span>
        <span class="k">cache-from</span>: <span class="s2">type=gha</span>
        <span class="k">cache-to</span>: <span class="s2">type=gha,mode=max</span>

    - <span class="k">name</span>: <span class="s2">Build &amp; Push Frontend Image</span>
      <span class="k">uses</span>: <span class="s2">docker/build-push-action@v5</span>
      <span class="k">with</span>:
        <span class="k">context</span>: <span class="s2">./phase2/frontend</span>
        <span class="k">file</span>: <span class="s2">./phase2/frontend/Dockerfile</span>
        <span class="k">build-args</span>: <span class="s2">|
          NEXT_PUBLIC_API_URL=http://${{{{ secrets.EC2_HOST }}}}:3001/api</span>
        <span class="k">push</span>: <span class="n">true</span>
        <span class="k">tags</span>: <span class="s2">|
          ${{{{ steps.login-ecr.outputs.registry }}}}/zeetafin-frontend:${{{{ steps.set-tag.outputs.tag }}}}
          ${{{{ steps.login-ecr.outputs.registry }}}}/zeetafin-frontend:latest</span>
        <span class="k">cache-from</span>: <span class="s2">type=gha</span>
        <span class="k">cache-to</span>: <span class="s2">type=gha,mode=max</span></code></pre>
</div>

<!-- SECTION 8 -->
<h2 id="live-logs"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/></svg></span>8. Inspecting Live Build Output &amp; Telemetry</h2>

<p>When you push code or trigger the pipeline, click into <strong>Actions &gt; ZeetaFin CI/CD Pipeline &gt; Build &amp; Push Images to Amazon ECR</strong> to view real-time compilation logs:</p>

<div class="term">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">GitHub Actions Runner Output (build-and-push)</span>
    <span class="tag ok">LOGS</span>
  </div>
<pre><code><span class="ok">✓</span> Checkout Application Code [1s]
<span class="ok">✓</span> Set Image Tag: 7c465625... [0s]
<span class="ok">✓</span> Set up Docker Buildx [3s]
<span class="ok">✓</span> Authenticate with AWS (us-east-1) [1s]
<span class="ok">✓</span> Log in to Amazon Elastic Container Registry [2s]
#1 [internal] load build definition from Dockerfile
#2 [internal] load metadata for docker.io/library/node:20-alpine
#3 [builder 1/4] COPY package*.json ./
#4 [builder 2/4] RUN npm ci
#5 [builder 3/4] COPY . .
#6 [builder 4/4] RUN npm run build
#7 exporting to image
#7 pushing layers to 123456789012.dkr.ecr.us-east-1.amazonaws.com/zeetafin-backend
<span class="ok">✓ Pushed: zeetafin-backend:7c465625...</span>
<span class="ok">✓ Pushed: zeetafin-backend:latest</span>
<span class="ok">✓ Pushed: zeetafin-frontend:7c465625...</span>
<span class="ok">✓ Pushed: zeetafin-frontend:latest</span></code></pre>
</div>

<!-- SECTION 9 -->
<h2 id="ecr-verify"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 14 10"/></svg></span>9. Validating Uploaded Images in AWS ECR</h2>

<p>Verify from your local terminal that both container images were received, tagged, and scanned by AWS:</p>

<div class="term">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">Terminal (AWS CLI)</span>
    <span class="tag">BASH</span>
    <button class="copy" type="button"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy</button>
  </div>
<pre><code><span class="p">$ </span>aws ecr list-images --repository-name zeetafin-backend --region us-east-1
<span class="p">$ </span>aws ecr list-images --repository-name zeetafin-frontend --region us-east-1</code></pre>
</div>

<p>Expected JSON response showing both the commit SHA and <code>latest</code> pointing to the same image digest:</p>
<div class="term">
  <div class="bar">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="fn">Output — list-images</span>
    <span class="tag exp">JSON</span>
  </div>
<pre><code>{{
    <span class="k">"imageIds"</span>: [
        {{
            <span class="k">"imageDigest"</span>: <span class="s2">"sha256:d8a9f3b17c802e9..."</span>,
            <span class="k">"imageTag"</span>: <span class="ok">"7c465625..."</span>
        }},
        {{
            <span class="k">"imageDigest"</span>: <span class="s2">"sha256:d8a9f3b17c802e9..."</span>,
            <span class="k">"imageTag"</span>: <span class="ok">"latest"</span>
        }}
    ]
}}</code></pre>
</div>

<!-- SECTION 10 -->
<h2 id="troubleshooting"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg></span>10. CI Troubleshooting Matrix</h2>

<div class="tbl">
  <table>
    <thead>
      <tr>
        <th>Failure Symptom</th>
        <th>Root Cause</th>
        <th>Solution</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>403 Forbidden: ecr:GetAuthorizationToken</code></td>
        <td>IAM bot user missing ECR authorization policy</td>
        <td>Attach <code>AmazonEC2ContainerRegistryPowerUser</code> to <code>zeetafin-ci-cd-bot</code>.</td>
      </tr>
      <tr>
        <td><code>npm ci: ELIFECYCLE out of memory</code></td>
        <td>Next.js production build exceeded runner RAM limit</td>
        <td>Verify <code>output: 'standalone'</code> in <code>next.config.js</code> and avoid compiling devDependencies.</td>
      </tr>
      <tr>
        <td>Pipeline does not trigger on commit</td>
        <td>Changed file path not matched by <code>paths:</code> filter</td>
        <td>Ensure modified files are within <code>phase2/</code> or <code>phase3/</code>, or trigger manually via <code>workflow_dispatch</code>.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- SECTION 11 -->
<h2 id="checklist"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg></span>11. Verification Checklist &amp; Challenge</h2>

<ol class="steps">
  <li>
    <b>Workflow File Active</b>
    <p><code>.github/workflows/deploy.yml</code> is committed to the <code>main</code> branch.</p>
  </li>
  <li>
    <b>Successful CI Run</b>
    <p>The <code>build-and-push</code> job finishes green in the GitHub Actions console.</p>
  </li>
  <li>
    <b>Dual Tags Verified in ECR</b>
    <p>Both <code>zeetafin-backend</code> and <code>zeetafin-frontend</code> display the current commit SHA and <code>latest</code> tags.</p>
  </li>
  <li>
    <b>Challenge Exercise</b>
    <p>Trigger a manual build via <code>workflow_dispatch</code> in GitHub Actions UI with <code>tag_override: v1.0.0-release</code>. Check ECR to confirm that this explicit tag was published.</p>
  </li>
</ol>

<!-- SECTION 12 -->
<h2 id="next"><span class="hi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg></span>12. What Comes Next</h2>

<p>Now that our container images are automatically built and published to Amazon ECR, we move to <strong>Part 3</strong>: Building the continuous deployment engine on EC2, executing remote SSH orchestration, and achieving graceful zero-downtime container replacement.</p>

<div class="pager">
  <a href="part-1-aws-iam-ecr-github-secrets.html">
    <small>← Previous Chapter</small>
    AWS IAM, ECR &amp; GitHub Secrets
  </a>
  <a class="r" href="part-3-ec2-remote-deployment-engine.html">
    <small>Next Chapter →</small>
    EC2 Remote Deployment &amp; Container Replacement Engine
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
    write_lab("part-2-github-actions-workflow-ci.html", get_part2_html())
