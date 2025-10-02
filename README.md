
Math 6310 — Intro to Data Science
=================================

This repository contains course assets, homework assignments, reports, and supporting scripts for Math 6310 — Introduction to Data Science.

Repository layout (top-level)
-----------------------------

- `apps/` — small Python application(s) used for demos or homework (example: `apps/homework.py`).
- `latex/` — LaTeX source files for homework and questions (`homework1.tex`, `homework2.tex`, `questions.tex`).
- `notebooks/` — Jupyter notebooks used for analysis and exploration.
- `reports/` — compiled PDFs for the homeworks (`homework1.pdf`, `homework2.pdf`).
- `templates/` — small HTML/Jinja templates used for generating reports or webpages.
- `build.py` — helper script to build or compile assets (project-specific build tasks).
- `demo.sh` — small demo script (may call `build.py` or other helpers).
- `pyproject.toml` — Python project metadata and dependencies.
- `shell.nix` — Nix development environment (if you use Nix)
- `LICENSE` — project license.

Quick start
-----------

Choose one of the following workflows depending on your setup.

1) Run with your system Python

- Install a modern Python (3.10+ recommended).
- Create a virtualenv and install dependencies if needed (see `pyproject.toml` for hints).
- Run small demos or scripts directly. For example:

```bash
# run the demo script (may require dependencies)
python build.py
# or
python apps/homework.py
```

2) Use the provided Nix environment (if you use Nix)

```bash
# enter the shell defined by shell.nix
nix develop
# then run build or demos as above
python build.py
```

3) Build LaTeX PDFs manually

If you prefer to build LaTeX directly, you can compile the sources in `latex/`:

```bash
pdflatex -output-directory=reports latex/homework1.tex
pdflatex -output-directory=reports latex/homework2.tex
```

Notes and tips
--------------

- Pre-built PDFs for submitted homeworks are stored in `reports/` (useful for quick viewing).
- If `build.py` or `demo.sh` exist, they may automate building PDFs, running notebooks, or packaging assets — try those first.
- Jupyter notebooks are under `notebooks/`; open them with JupyterLab or nbviewer if you want to explore interactive content.

Contributions and edits
-----------------------

This repository is primarily a course asset collection. If you'd like to suggest improvements or corrections, open an issue or submit a pull request with a clear description of the change and any supporting files.

License
-------

See the `LICENSE` file at the repository root for license terms.

Contact
-------

For questions about course content or repository layout, contact the repository owner or the course instructor (see course materials for contact details).

Acknowledgements
----------------

This repo was created to collect and distribute course materials for Math 6310 — Intro to Data Science.
