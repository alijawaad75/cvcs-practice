# GitHub Packages Plan

This project does not need package publishing yet because it is a small learning app.

Use GitHub Packages when a folder becomes reusable across projects.

Good future package candidates:

- `appointment_validation`
- `appointment_test_helpers`
- `attendance_prediction_demo`

Suggested publishing flow later:

```text
Tag release
  -> Run tests
  -> Build Python package
  -> Publish to GitHub Packages
```

