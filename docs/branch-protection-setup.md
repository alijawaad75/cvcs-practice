# Branch Protection Setup

Branch protection is a GitHub setting, so it cannot be fully enforced by committed project code alone.

## Recommended Rule

Branch name pattern:

```text
main
```

Enable:

- Require a pull request before merging
- Require approvals: 1
- Dismiss stale pull request approvals when new commits are pushed
- Require status checks to pass before merging
- Require branches to be up to date before merging
- Require conversation resolution before merging
- Block force pushes
- Block branch deletion

Required checks:

```text
Run automated tests
Analyze Python
```

## Manual Setup Path

```text
GitHub repo -> Settings -> Branches -> Add branch protection rule
```

