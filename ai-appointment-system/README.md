# AI Appointment System

Beginner-friendly AI/ML project for learning automated test maintainability.

## What It Contains

| Part | Kaam |
| --- | --- |
| Frontend | Patient appointment form fill karta hai |
| Backend API | Data receive karta hai |
| Validation | Phone, name, age check hota hai |
| ML Model | Predict karta hai patient appointment attend karega ya nahi |
| Database | Patient record JSONL file mein save hota hai |
| Automated Tests | Check karte hain system sahi kaam kar raha hai |

## Run Tests

```powershell
cd D:\DDP_calculate\ai-appointment-system
py -3 -m pytest tests -q -p no:cacheprovider
```

This command runs:

- Validation tests
- Backend API tests
- Model prediction tests
- Playwright browser test for the appointment form

Install Playwright locally once before running the browser test:

```powershell
cd D:\DDP_calculate\ai-appointment-system
py -3 -m pip install -r requirements-dev.txt
py -3 -m playwright install chromium
```

## Watch Playwright Work

To see Playwright open a real browser and fill the appointment form:

```powershell
cd D:\DDP_calculate\ai-appointment-system
py -3 scripts\demo_playwright_visible.py
```

Git Bash:

```bash
cd /d/DDP_calculate/ai-appointment-system
py -3 scripts/demo_playwright_visible.py
```

## Measure Time And Build Report

```powershell
cd D:\DDP_calculate\ai-appointment-system
py -3 scripts\measure_tests.py
```

Report files:

- `reports/maintainability_report.md`
- `reports/test_run_result.json`

## Run Backend API

```powershell
cd D:\DDP_calculate\ai-appointment-system
py -3 backend\app.py
```

Then open `frontend/appointment_form.html` in a browser.

## Maintainability Experiment

1. AI/ML project banao.
2. Automated tests likho.
3. Phone number rule change karo in `config/rules.py`.
4. Tests update karo in `test_data/test_data.py`.
5. Time measure karo using `scripts/measure_tests.py`.
6. Report banao in `reports/maintainability_report.md`.
7. Improve karo by removing duplicated test data.
8. Dobara change karke observe karo.

## AI Agent Session

For GitHub/Codex/Copilot agent sessions, use `AGENTS.md` as the project guide.
It defines the safest workflow, maintainability rules, and required verification commands.

## Professional GitHub Setup

This repo includes CI/CD, CODEOWNERS, issue templates, security scanning workflows,
release automation, and self-hosted runner examples.

Start here:

- `docs/github-professional-setup.md`
