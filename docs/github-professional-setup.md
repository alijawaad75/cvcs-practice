# GitHub Professional Setup For AI Appointment System

This repo now includes practical setup for the 10 expert GitHub practices.

## 1. GitHub Actions CI/CD

Implemented:

- `.github/workflows/ai-appointment-system-ci.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/dependency-review.yml`
- `.github/workflows/release.yml`

CI flow:

```text
Push Code
  -> Run Pytest and Playwright
  -> Generate Maintainability Report
  -> Upload Report Artifact
```

## 2. Branch Protection Rules

This needs GitHub repository settings.

Recommended settings for `main`:

- Require a pull request before merging
- Require approvals: 1
- Require status checks to pass
- Required check: `Run automated tests`
- Require branches to be up to date before merging
- Do not allow force pushes
- Do not allow deletions

GitHub path:

```text
Repository -> Settings -> Branches -> Add branch protection rule -> main
```

## 3. CODEOWNERS

Implemented:

- `.github/CODEOWNERS`

This automatically requests review from the listed owner when important project files change.

## 4. GitHub Projects

Use the template:

- `docs/project-board-template.md`

Recommended columns:

```text
Todo -> In Progress -> Review -> Done
```

## 5. Issue Templates

Implemented:

- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/pull_request_template.md`

## 6. GitHub Security Scanning

Implemented files:

- `.github/dependabot.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/dependency-review.yml`
- `.github/SECURITY.md`

Also enable these in GitHub settings:

- Dependabot alerts
- Dependabot security updates
- Secret scanning
- Code scanning alerts

## 7. GitHub Packages

For this beginner Python project, GitHub Packages is documented but not published automatically yet.

Use it later when you extract reusable code into a package, for example:

- validation package
- reusable test helpers
- appointment SDK

## 8. GitHub Releases

Implemented:

- `.github/workflows/release.yml`

Create a release by pushing a tag:

```bash
git tag v1.0.0
git push origin v1.0.0
```

## 9. Self Hosted Runners

Implemented example:

- `.github/workflows/self-hosted-ai-runner-example.yml`

Use this later for:

- GPU testing
- private server testing
- faster local builds
- internal network access

## 10. Monorepo Architecture

Current repo is already moving toward monorepo style:

```text
repo/
  .github/
  ai-appointment-system/
    backend/
    frontend/
    tests/
    config/
    scripts/
    reports/
  docs/
```

Keep future apps as separate top-level folders instead of mixing files into root.

