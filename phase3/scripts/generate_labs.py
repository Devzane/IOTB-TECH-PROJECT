#!/usr/bin/env python3
"""
ZeetaFin Phase 3 Lab Series Generator
Generates high-fidelity, interactive, pedagogical HTML labs for Phase 3 CI/CD.
Aesthetic standards match Phase 1 and Phase 2 (Sora, DM Sans, JetBrains Mono, Dark/Light mode,
Mermaid/SVG diagrams, click-to-copy buttons, and terminal outputs).
"""

import os
import sys

COMMON_CSS = """
:root{
  --bg:#f8fafc; --surface:#ffffff; --surface-2:#f1f5f9; --ink:#0f172a; --ink-2:#334155; --muted:#64748b; --line:#e2e8f0;
  --c1:#6366f1; --c2:#0ea5e9; --c3:#f59e0b; --c4:#10b981; --c5:#8b5cf6; --c6:#ec4899;
  --accent:#4f46e5; --accent-ink:#4338ca; --accent-soft:#eef2ff;
  --mint:#10b981; --mint-soft:#ecfdf5; --amber:#f59e0b; --amber-soft:#fffbeb; --rose:#ef4444; --rose-soft:#fef2f2;
  --night:#0a0f1d; --night-2:#11192e; --night-line:#1e293b; --night-ink:#f8fafc; --night-muted:#94a3b8;
  --sans:"DM Sans","Helvetica Neue",Arial,sans-serif; --head:"Sora","DM Sans",Arial,sans-serif; --mono:"JetBrains Mono",ui-monospace,Menlo,Consolas,monospace;
  --shadow:0 1px 3px rgba(15,23,42,.08),0 10px 30px rgba(15,23,42,.04);
}
@media (prefers-color-scheme:dark){
  :root{
    --bg:#070b14; --surface:#0e1526; --surface-2:#141f38; --ink:#f8fafc; --ink-2:#cbd5e1; --muted:#8899b5; --line:#1d2945;
    --accent:#818cf8; --accent-ink:#a5b4fc; --accent-soft:#182042;
    --mint:#34d3b4; --mint-soft:#062d25; --amber:#fbbf24; --amber-soft:#332205; --rose:#f87171; --rose-soft:#341318;
    --shadow:0 1px 3px rgba(0,0,0,.5),0 14px 40px rgba(0,0,0,.45);
  }
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:radial-gradient(900px 500px at 100% 0,color-mix(in srgb,var(--c1) 8%,transparent),transparent 70%),radial-gradient(800px 500px at 0 30%,color-mix(in srgb,var(--c2) 7%,transparent),transparent 70%),var(--bg);color:var(--ink-2);font-family:var(--sans);font-size:18px;line-height:1.72;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
a{color:var(--accent-ink);text-underline-offset:3px}
:focus-visible{outline:3px solid var(--accent);outline-offset:2px;border-radius:4px}
.wrap{max-width:1200px;margin:0 auto;padding:0 28px}
.progress{position:fixed;inset:0 0 auto 0;height:5px;z-index:50;background:transparent}
.progress i{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--c1),var(--c2),var(--c4),var(--c3),var(--c6))}

/* Hero */
.hero{background:var(--night);color:var(--night-ink);position:relative;overflow:hidden;isolation:isolate}
.hero::before{content:"";position:absolute;inset:0;z-index:-1;background:radial-gradient(750px 380px at 90% -10%,rgba(99,102,241,.65),transparent 62%),radial-gradient(650px 380px at 10% 110%,rgba(14,165,233,.45),transparent 62%),radial-gradient(rgba(255,255,255,.07) 1px,transparent 1.2px) 0 0/26px 26px}
.hero .wrap{padding-top:44px;padding-bottom:44px}
.sbar{display:flex;gap:8px;margin:0 0 30px;overflow-x:auto;padding-bottom:4px;scrollbar-width:none}
.sbar::-webkit-scrollbar{display:none}
@media (min-width:900px){.sbar{flex-wrap:wrap;overflow:visible}}
.sbar .p{display:inline-flex;align-items:center;gap:9px;flex:none;padding:6px 14px 6px 6px;border-radius:99px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.16);color:#cbd5e1;text-decoration:none;font:600 13px var(--head);transition:all .18s}
.sbar .p i{width:24px;height:24px;border-radius:50%;background:var(--c);color:#fff;display:grid;place-items:center;font-style:normal;font-size:12px}
.sbar .p:hover{background:rgba(255,255,255,.14);color:#fff}
.sbar .p.on{background:#fff;color:#0a0f1d;border-color:#fff}

h1{font-family:var(--head);font-weight:800;font-size:clamp(34px,5vw,60px);line-height:1.08;letter-spacing:-.035em;margin:0;max-width:20ch;color:#fff}
.dek{font-size:clamp(18px,2vw,22px);line-height:1.55;color:#cbd5e1;max-width:58ch;margin:20px 0 0}
.meta{display:flex;flex-wrap:wrap;gap:8px 22px;margin:24px 0 0;font-family:var(--head);font-size:13.5px;color:var(--night-muted)}
.meta span{display:inline-flex;gap:8px;align-items:center}
.tools{display:flex;flex-wrap:wrap;gap:10px;margin:22px 0 0}
.tool{display:inline-flex;align-items:center;gap:8px;padding:7px 14px;border-radius:12px;background:rgba(255,255,255,.09);border:1px solid rgba(255,255,255,.18);color:#fff;font:600 13.5px var(--head)}
.hero-art{margin-top:34px;border:1px solid rgba(255,255,255,.2);border-radius:24px;background:linear-gradient(180deg,rgba(255,255,255,.08),rgba(255,255,255,.02));padding:16px;box-shadow:0 30px 80px rgba(0,0,0,.4);backdrop-filter:blur(4px)}
.hero-art>svg{display:block;width:100%;height:auto}

/* Layout */
.layout{display:grid;grid-template-columns:220px minmax(0,1fr);gap:64px;align-items:start;padding-top:56px}
nav.toc{position:sticky;top:24px;font-family:var(--head);font-size:13.5px;max-height:calc(100vh - 48px);overflow:auto}
nav.toc h2{font-size:12px;font-weight:700;color:var(--muted);margin:0 0 12px;letter-spacing:.04em;text-transform:uppercase}
nav.toc ol{list-style:none;margin:0;padding:0;border-left:1.5px solid var(--line)}
nav.toc a{display:block;padding:6px 0 6px 16px;margin-left:-1.5px;border-left:1.5px solid transparent;color:var(--muted);text-decoration:none;line-height:1.35;transition:color .15s}
nav.toc a:hover{color:var(--ink)}
nav.toc a.on{color:var(--accent);border-left-color:var(--accent);font-weight:700}
nav.toc li.sub a{padding-left:30px;font-size:12.5px}
.sidecard{margin-top:26px;padding:16px;border:1px solid var(--line);border-radius:14px;background:var(--surface);font-size:13px;line-height:1.5;color:var(--muted);box-shadow:var(--shadow)}
.sidecard b{display:block;color:var(--ink);font-family:var(--head);font-size:13.5px;margin-bottom:4px}

article{min-width:0;max-width:780px}
article h2{font-family:var(--head);font-weight:700;font-size:clamp(28px,3.4vw,38px);line-height:1.18;letter-spacing:-.025em;margin:88px 0 16px;color:var(--ink);scroll-margin-top:20px;display:flex;gap:14px;align-items:center;padding-bottom:14px;border-bottom:2px solid var(--line)}
article h2 .hi{width:48px;height:48px;border-radius:14px;background:var(--hc,var(--c1));color:#fff;display:grid;place-items:center;flex:none;box-shadow:0 8px 20px color-mix(in srgb,var(--hc,var(--c1)) 35%,transparent)}
article h2 .hi svg{width:26px;height:26px;stroke-width:2}
article h2:first-child{margin-top:0}
article h2:nth-of-type(6n+1){--hc:var(--c1)}article h2:nth-of-type(6n+2){--hc:var(--c2)}article h2:nth-of-type(6n+3){--hc:var(--c4)}article h2:nth-of-type(6n+4){--hc:var(--c3)}article h2:nth-of-type(6n+5){--hc:var(--c5)}article h2:nth-of-type(6n+6){--hc:var(--c6)}

article h3{font-family:var(--head);font-weight:700;font-size:21px;line-height:1.3;margin:48px 0 10px;color:var(--ink);scroll-margin-top:20px;letter-spacing:-.01em;background:linear-gradient(90deg,color-mix(in srgb,var(--c1) 12%,transparent),transparent 85%);border-left:6px solid var(--c1);padding:12px 18px;border-radius:0 14px 14px 0}
article p{margin:0 0 1.15em}
article ul,article ol{padding-left:1.3em;margin:0 0 1.25em}
article li{margin:.4em 0}
article strong,article b{color:var(--ink);font-weight:700}
code{font-family:var(--mono);font-size:.84em;background:color-mix(in srgb,var(--c1) 12%,transparent);color:var(--accent-ink);padding:.12em .45em;border-radius:6px;font-weight:500}
.lead{font-size:1.15em;color:var(--ink);line-height:1.68}

/* Code & Term */
.code,.term{margin:24px 0 28px;border-radius:16px;overflow:hidden;background:var(--night);border:1px solid #223055;box-shadow:0 14px 40px rgba(10,15,29,.25)}
.bar{display:flex;align-items:center;gap:10px;padding:10px 16px;background:linear-gradient(180deg,#152042,#0d152d);border-bottom:1px solid #1f2c4e;font-family:var(--mono);font-size:12.5px;color:#8f9cb8}
.bar .dots{display:flex;gap:6px}.bar .dots i{width:10px;height:10px;border-radius:50%;display:block}
.bar .dots i:nth-child(1){background:#ff5f57}.bar .dots i:nth-child(2){background:#febc2e}.bar .dots i:nth-child(3){background:#28c840}
.bar .fn{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-weight:500}
.bar .tag{font-family:var(--head);font-size:11px;font-weight:600;padding:2px 8px;border-radius:99px;background:#1a2750;color:#a5b4fc}
.copy{all:unset;cursor:pointer;display:inline-flex;gap:6px;align-items:center;font-family:var(--head);font-size:12px;color:#a5b4fc;padding:4px 9px;border-radius:7px;border:1px solid #273766;transition:all .15s}
.copy:hover{background:#1a2750;color:#fff}.copy.copied{color:#34d3b4;border-color:#34d3b4;background:rgba(52,211,180,.1)}
.copy svg{width:13px;height:13px;fill:none;stroke:currentColor;stroke-width:2}
pre{margin:0;font-family:var(--mono);font-size:14px;line-height:1.68;color:#dce5f8;padding:16px 18px;overflow-x:auto;tab-size:2}
pre code{background:none;color:inherit;padding:0;font-size:inherit}
.k{color:#818cf8;font-weight:600}.s2{color:#6ee7b7}.c{color:#64748b;font-style:italic}.n{color:#fcd34d}.p{color:#94a3b8;user-select:none}
.ok{color:#34d3b4}.bad{color:#f87171}.dim{color:#64748b}.b{font-weight:700;color:#fff}.warn{color:#fbbf24}

/* Callouts */
.callout{display:flex;gap:14px;padding:18px 20px;border-radius:16px;margin:28px 0;border-left-width:6px;border-left-style:solid;box-shadow:var(--shadow);font-size:16px;line-height:1.62;color:var(--ink-2)}
.callout>svg{width:32px;height:32px;padding:6px;border-radius:50%;color:#fff;margin-top:2px;flex:none;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.callout b.t{display:block;font-family:var(--head);color:var(--ink);margin-bottom:3px;font-weight:700}
.callout p{margin:0 0 .5em}.callout p:last-child{margin:0}
.callout.info{background:var(--accent-soft);border-left-color:var(--accent)}.callout.info>svg{background:var(--accent)}
.callout.warn{background:var(--amber-soft);border-left-color:var(--amber)}.callout.warn>svg{background:var(--amber)}
.callout.ok{background:var(--mint-soft);border-left-color:var(--mint)}.callout.ok>svg{background:var(--mint)}
.callout.bad{background:var(--rose-soft);border-left-color:var(--rose)}.callout.bad>svg{background:var(--rose)}

/* Tables */
.tbl{overflow-x:auto;margin:24px 0 28px;border:1px solid color-mix(in srgb,var(--c1) 22%,var(--line));border-radius:16px;background:var(--surface);box-shadow:var(--shadow)}
table{border-collapse:collapse;width:100%;font-size:15px;font-family:var(--sans)}
th,td{text-align:left;padding:12px 18px;border-bottom:1px solid var(--line);vertical-align:top;line-height:1.55}
tr:last-child td{border-bottom:0}
th{font-family:var(--head);font-weight:700;font-size:13.5px;color:var(--accent-ink);background:color-mix(in srgb,var(--c1) 14%,var(--surface));border-bottom:2px solid color-mix(in srgb,var(--c1) 32%,var(--line))}
tr:nth-child(even) td{background:color-mix(in srgb,var(--surface-2) 65%,var(--surface))}
td:first-child{color:var(--ink);font-weight:600;border-right:1px solid var(--line)}

/* Details */
details{background:var(--surface);border:1px solid var(--line);border-radius:16px;margin:24px 0;padding:0 20px;box-shadow:var(--shadow);border-left:5px solid var(--c2)}
details summary{font-family:var(--head);font-weight:700;font-size:16px;cursor:pointer;padding:16px 0;color:var(--ink);list-style:none;display:flex;gap:10px;align-items:center}
details summary::-webkit-details-marker{display:none}
details summary::after{content:"";margin-left:auto;width:8px;height:8px;border-right:2px solid var(--muted);border-bottom:2px solid var(--muted);transform:rotate(45deg);transition:transform .2s}
details[open] summary::after{transform:rotate(-135deg)}
details[open] summary{border-bottom:1px solid var(--line);margin-bottom:14px}
details p:last-child{margin-bottom:16px}

/* Steps */
.steps{list-style:none;padding:0;margin:28px 0;counter-reset:s}
.steps>li{counter-increment:s;position:relative;padding:0 0 28px 58px;margin:0}
.steps>li::before{content:counter(s);position:absolute;left:0;top:0;width:38px;height:38px;border-radius:50%;background:var(--ink);color:var(--surface);font-family:var(--head);font-weight:700;font-size:15px;display:grid;place-items:center}
.steps>li::after{content:"";position:absolute;left:18.5px;top:44px;bottom:6px;width:1.5px;background:var(--line)}
.steps>li:last-child{padding-bottom:0}.steps>li:last-child::after{display:none}
.steps>li>b:first-child{display:block;font-family:var(--head);font-size:17px;color:var(--ink);margin:6px 0 4px}

/* Cards & Grid */
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;margin:26px 0}
.card{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:18px 16px 16px;box-shadow:var(--shadow);border-top:4px solid var(--c)}
.card h4{margin:0 0 4px;font-family:var(--head);font-size:16px;color:var(--ink);font-weight:700}
.card p{margin:0;font-size:14.5px;line-height:1.52;color:var(--muted)}

/* Pager */
.pager{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:60px 0 0}
.pager a{display:block;border:1px solid var(--line);background:var(--surface);border-radius:14px;padding:16px 20px;text-decoration:none;color:var(--ink);box-shadow:var(--shadow);font-family:var(--head);font-weight:700;transition:border-color .15s}
.pager a small{display:block;font-weight:500;color:var(--muted);font-size:12.5px;margin-bottom:4px}
.pager a:hover{border-color:var(--accent)}.pager .r{text-align:right}
footer{margin-top:80px;border-top:1px solid var(--line);padding:32px 0 64px;font-family:var(--head);font-size:14px;color:var(--muted)}

@media(max-width:960px){
  .layout{grid-template-columns:1fr;gap:0;padding-top:34px}
  nav.toc{position:static;max-height:none;margin-bottom:30px}
  nav.toc ol{display:flex;flex-wrap:wrap;gap:2px 16px;border:0}
  nav.toc a,nav.toc li.sub a{padding:4px 0;border:0;margin:0}
  nav.toc li.sub,.sidecard{display:none}
}
@media(max-width:600px){body{font-size:17px}.wrap{padding:0 18px}pre{font-size:12.5px}article h2 .hi{display:none}.pager{grid-template-columns:1fr}}
"""

COMMON_SCRIPT = """
const bar = document.querySelector('.progress i');
window.addEventListener('scroll', () => {
  const h = document.documentElement;
  bar.style.width = ((h.scrollTop) / (h.scrollHeight - h.clientHeight) * 100) + '%';
});

const links = [...document.querySelectorAll('nav.toc a')];
const obs = new IntersectionObserver(es => {
  es.forEach(e => {
    if (e.isIntersecting) {
      links.forEach(l => l.classList.remove('on'));
      const a = links.find(l => l.getAttribute('href') === '#' + e.target.id);
      if (a) a.classList.add('on');
    }
  });
}, { rootMargin: '-20% 0px -70% 0px' });
document.querySelectorAll('article h2[id], article h3[id]').forEach(h => obs.observe(h));

document.querySelectorAll('.copy').forEach(btn => {
  btn.addEventListener('click', () => {
    const parent = btn.closest('.code, .term');
    const target = parent ? parent.querySelector('pre code, pre') : null;
    if (target) {
      navigator.clipboard.writeText(target.innerText).then(() => {
        const orig = btn.innerHTML;
        btn.innerHTML = `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Copied!`;
        btn.classList.add('copied');
        setTimeout(() => {
          btn.innerHTML = orig;
          btn.classList.remove('copied');
        }, 2000);
      });
    }
  });
});
"""

def generate_navbar(active_idx):
    chapters = [
        ("part-1-aws-iam-ecr-github-secrets.html", "#6366f1", "1", "IAM, ECR & Secrets"),
        ("part-2-github-actions-workflow-ci.html", "#0ea5e9", "2", "GitHub Actions CI"),
        ("part-3-ec2-remote-deployment-engine.html", "#f59e0b", "3", "EC2 CD & Rollout"),
        ("part-4-end-to-end-pipeline-verification.html", "#10b981", "4", "Verification & Triage")
    ]
    html = '<nav class="sbar" aria-label="Lab chapters">\n'
    for i, (url, color, num, title) in enumerate(chapters, 1):
        is_on = " on" if i == active_idx else ""
        current = ' aria-current="page"' if i == active_idx else ""
        html += f'  <a class="p{is_on}" href="{url}" style="--c:{color}"{current}><i>{num}</i><span>{title}</span></a>\n'
    html += '</nav>'
    return html

print("Generating Phase 3 Lab Series...")
