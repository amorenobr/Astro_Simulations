# Astronomy Simulations

Interactive simulations built with Python and Streamlit for exploring
core concepts in astronomy. Adjust physical parameters with sliders and 
watch the results update in real time. Available in **English and Spanish** with a 
one-click language toggle.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/amorenobr/Astro_Simulations/actions/workflows/ci.yml/badge.svg)](https://github.com/amorenobr/Astro_Simulations/actions/workflows/ci.yml)

- 🚀 **Live app:** https://amorenobr.github.io/Astro_Simulations/
- 📖 **Documentation:** https://amorenobr.github.io/Astro_Simulations/docs/

## Simulations

- **Kepler's Laws** - Explore an elliptical orbit set by its semi-major axis and eccentricity, and see Kepler's
three laws: the ellipse shape, the perihelion-to-aphelion speed ratio, and the period-size relation T² = a³.
- **Planck Spectrum** - See how a blackbody's radiation depends on temperature: the spectrum's peak shifts toward
the blue as it heats up (Wien's law) and the total power grows as T⁴ (Stefan-Boltzmann law).

## Getting Started

This project uses [Pixi](https://pixi.sh) to manage its environment and dependencies.

### Install

```bash
git clone https://github.com/amorenobr/Astro_Simulations.git
cd Astro_Simulations
pixi install
```

### Run the app

```bash
pixi run streamlit run Simulations.py
```

Then open the URL shown in the terminal.

## Development

Common tasks are defined as [Pixi tasks](https://pixi.sh):

```bash
pixi run app		# launch the app
pixi run test		# run the tests
pixi run cov		# tests with a coverage report
pixi run lint		# lint with Ruff
pixi run fmt		# format with Ruff
pixi run typecheck	# type-check with mypy
pixi run docs		# build the Sphinx docs (output in docs/build/html)
```

Every push and pull request runs CI (lint, format check, type check, and tests). Locally, Ruff also runs on
each commit via pre-commit. Enable it once after cloning:

```bash
pixi run pre-commit install
```

## Project Structure

```
Astro_Simulations/
├── Simulations.py                  # Streamlit landing page
├── pages/                          # One file per simulation
├── src/astro_simulations/          # Astronomy modules + i18n
├── tests/                          # Pytest suite
├── docs/                           # Sphinx documentation
└── index.html                      # stlite (WebAssembly) build for GitHub Pages
```

## Tech Stack

- [Streamlit](https://streamlit.io) / [stlite](https://github.com/whitphx/stlite) — user interface
- [NumPy](https://numpy.org) — numerical computation
- [Plotly](https://plotly.com/python/) — interactive plots
- [Sphinx](https://www.sphinx-doc.org) — documentation
- [Pixi](https://pixi.sh) — environment management
- [Ruff](https://docs.astral.sh/ruff/) — linting and formatting
- [mypy](https://www.mypy-lang.org/) — static type checking
- [GitHub Actions](https://github.com/features/actions) — CI/CD (tests, linting, deployment)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Alexander Moreno Briceño - Universidad Antonio Nariño
