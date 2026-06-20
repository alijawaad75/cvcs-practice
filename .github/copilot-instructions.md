# Repository Agent Instructions

The main maintained project in this repository is `ai-appointment-system`.

For any change inside `ai-appointment-system`, follow:

- `ai-appointment-system/AGENTS.md`

Minimum verification:

```powershell
cd ai-appointment-system
py -3 -m pip install -r requirements-dev.txt
py -3 -m playwright install chromium
py -3 -m pytest tests -q -p no:cacheprovider
```

For maintainability/reporting changes, also run:

```powershell
py -3 scripts\measure_tests.py
```

Keep unrelated repository files untouched unless the task explicitly asks for them.
