# Repository notes

- This is a small Python project; implementation modules and tests are under `src/`.
- Use Python 3.14 (`.python-version`; `pyproject.toml` requires `>=3.14`).
- pytest is the only declared development dependency (`pyproject.toml`); install it in the active Python environment if needed (`python -m pip install pytest`).
- Run tests from `src/` with `python -m pytest`; tests use top-level imports such as `from ostoskori import ...`.
- No project-specific lint or typecheck command is configured.
- Tests executed with uv run pytest
- Code of ostos.py and tuote.py should not be changed
- Tests should not be edited unless 
