import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = PROJECT_ROOT / "reports"


def run_pytest():
    start = time.perf_counter()
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
    process = subprocess.run(
        [sys.executable, "-m", "pytest", "tests", "-q", "-p", "no:cacheprovider"],
        cwd=PROJECT_ROOT,
        env=env,
        text=True,
        capture_output=True,
    )
    duration = round(time.perf_counter() - start, 4)
    return process, duration


def write_reports(process, duration):
    REPORTS_DIR.mkdir(exist_ok=True)
    result = {
        "measured_at": datetime.now().isoformat(timespec="seconds"),
        "duration_seconds": duration,
        "exit_code": process.returncode,
        "stdout": process.stdout.strip(),
        "stderr": process.stderr.strip(),
        "maintainability_notes": [
            "Phone rule lives in config/rules.py",
            "Shared valid and invalid examples live in test_data/test_data.py",
            "API test uses an in-memory database so tests stay fast and isolated",
            "Model test checks behavior ranges instead of fragile exact internals",
            "Playwright test verifies the frontend form can book through the backend API",
        ],
    }

    (REPORTS_DIR / "test_run_result.json").write_text(json.dumps(result, indent=2), encoding="utf-8")

    status = "PASS" if process.returncode == 0 else "FAIL"
    markdown = f"""# Automated Test Maintainability Report

## Test Result

| Metric | Value |
| --- | --- |
| Status | {status} |
| Duration | {duration} seconds |
| Command | `{sys.executable} -m pytest tests -q -p no:cacheprovider` |

## Pytest Output

```text
{process.stdout.strip()}
```

## Maintainability Improvement

- Phone number rule is centralized in `config/rules.py`.
- Test examples are centralized in `test_data/test_data.py`.
- When the phone rule changes, update rule config plus shared examples first.
- API tests use an in-memory database, avoiding slow or flaky file writes.
- Model tests verify expected behavior instead of overfitting to implementation details.
- Playwright verifies the user-facing appointment form against the backend API.

## Observation Workflow

1. Change `PHONE_PATTERN` and `PHONE_EXAMPLE` in `config/rules.py`.
2. Update invalid/valid examples in `test_data/test_data.py`.
3. Run `py -3 scripts/measure_tests.py`.
4. Compare the new duration and failing/passing tests in this report.
"""
    (REPORTS_DIR / "maintainability_report.md").write_text(markdown, encoding="utf-8")


def main():
    process, duration = run_pytest()
    write_reports(process, duration)
    print(process.stdout)
    print(f"Duration: {duration} seconds")
    print(f"Report: {REPORTS_DIR / 'maintainability_report.md'}")
    return process.returncode


if __name__ == "__main__":
    raise SystemExit(main())
