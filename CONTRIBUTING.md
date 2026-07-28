# Contributing

Thanks for your interest in contributing to **Physics Lab Simulations**! Contributions of all kinds are 
welcome - bug reports, new simulations, translation fixes, documentation, and tooling improvements.

## Ways to contribute

- **Report a bug or request a feature** - open an issue describing the problem or idea.
- **Add or improve a simulation** - see "Adding a simulation" below.
- **Improve translations** - the app is bilingual (English/Spanish); refinements are welcome.
- **Documentation** - improvements to the docs or README.

## Development setup

The project uses [Pixi](https://pixi.sh) to manage its environment.

```bash
git clone https://github.com/amorenobr/Lab_Simulations_Python.git
cd Lab_Simulations_Python
pixi install
pixi run pre-commit install	# enable local lint/format on commit
```

## Common tasks

```bash
pixi run app		# launch the app locally
pixi run test		# run the tests
pixi run cov		# tests with a coverage report
pixi run lint		# lint with Ruff
pixi run fmt		# format with Ruff
pixi run typecheck	# type-check with mypy
pixi run docs		# build the documentation
```

## Code quality

Every push and pull request runs CI, which must pass before merging:

- **Ruff** - linting and formatting
- **mypy** - type checking
- **pytest** - tests (with coverage)

Please run `pixi run lint`, `pixi run fmt`, `pixi run typecheck`, and `pixi run test` locally before opening a
pull request. Pre-commit runs Ruff on each commit automatically.

## Adding a simulation

Each simulation follows the same structure. To add one called `X`:

1. **Physics** - add `src/lab_simulations_python/X.py` with the calculation function(s), and a test in
`tests/test_X.py`.
2. **Page** - add `pages/N_X.py` (a **Streamlit** page). Call `language_selector()` and wrap every user facing
string in `t(...)`.
3. **Translations** - add the `X_*` keys to both the `en` and `es` dictionaries in
`src/lab_simulations_python/i18n.py`, plus a `nav_X` key and a `page_link` entry in `language_selector`. Both
languages must stay in sync, this is enforced by `tests/test_i18n.py`.
4. **Docs and listings** - document the module in `docs/source/api.rst`, add a section to `docs/source/index.rst`, and
add a bullet to the landing page and the README.
5. **Deployment** - add the new page and module to the `files` map in `index.html`.

## Translations

All user facing text lives in the `TRANSLATIONS` dictionary in `src/lab_simulations_python/i18n.py`, keyed by
language. Every key must exist in both English and Spanish, checked automatically by `tests/test_i18n.py`.

## Pull requests

1. Create a branch from `main`.
2. Keep commits focused; ensure `pixi run test`, `pixi run lint`, and `pixi run typecheck` pass.
3. Open a pull request describing the change, and make sure CI is green.

## Code of conduct

Please be respectful and constructive. This project follows the spirit of the [Contributor Covenant](https://www.contributor-covenant.org/).
