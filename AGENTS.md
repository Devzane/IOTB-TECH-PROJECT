# Development & Git Guidelines

## Git Commit Rules
When committing changes in this repository:
- **Strictly Atomic & Granular Commits**: Every commit must represent exactly one logical change (a single feature, bugfix, refactor, config update, or documentation addition). Never bundle unrelated modifications into a single commit.
- **Workflow**:
  1. Inspect status with `git status` / `git diff`.
  2. Group modified files by single responsibility.
  3. Verify that no secrets, credentials, environment keys, private keys (`.pem`, `.key`, `phase1-key`), or local state files (`*.tfvars`, `*.tfstate`, `hosts.ini`) are staged.
  4. Stage and commit each group separately with Conventional Commits syntax (`feat:`, `chore:`, `fix:`, `docs:`, `refactor:`).
  5. Commit prerequisites/dependencies before dependent code.
  6. Push only once all atomic commits are prepared.
