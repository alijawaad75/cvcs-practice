# AI Appointment System Agent Guide

Use this guide for every AI-agent session that changes `ai-appointment-system`.

## Project Goal

This is a beginner-friendly AI/ML appointment demo focused on automated test maintainability.

The system includes:

- Frontend appointment form
- Backend appointment API
- Name, age, and phone validation
- Deterministic ML-like attendance prediction
- JSONL appointment persistence
- Automated tests, Playwright browser coverage, and a maintainability report

## Session Workflow

1. Read this file first.
2. Inspect only the files relevant to the requested change.
3. Keep business rules centralized in `config/rules.py`.
4. Keep reusable test examples in `test_data/test_data.py`.
5. Add or update focused tests for every behavior change.
6. Run the local test command before finishing.
7. If the change affects the maintainability experiment, run the report command too.
8. Summarize changed files, test result, and any known limitation.

## Commands

Run from `ai-appointment-system`:

```powershell
py -3 -m pytest tests -q -p no:cacheprovider
```

Install browser test dependencies when needed:

```powershell
py -3 -m pip install -r requirements-dev.txt
py -3 -m playwright install chromium
```

Generate the maintainability report:

```powershell
py -3 scripts\measure_tests.py
```

Run the backend API:

```powershell
py -3 backend\app.py
```

## Maintainability Rules

- Do not duplicate the phone regex inside tests.
- Change phone behavior through `config/rules.py`.
- Update shared valid and invalid examples in `test_data/test_data.py`.
- Keep API tests isolated with an in-memory database.
- Keep model tests behavior-based, not tied to private implementation details.
- Keep Playwright tests focused on real user flows, not visual styling.
- Prefer small, readable Python functions over new dependencies.

## CI/CD

GitHub Actions workflow:

- `.github/workflows/ai-appointment-system-ci.yml`

It runs on changes to this project and uploads:

- `reports/maintainability_report.md`
- `reports/test_run_result.json`

Do not mark a GitHub task complete until local tests pass or the blocker is clearly reported.
