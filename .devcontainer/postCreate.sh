#!/usr/bin/env bash
set -eux

# Create venv if missing
if [ ! -d venv ]; then
  python3 -m venv --without-pip venv
  curl -sS https://bootstrap.pypa.io/get-pip.py | venv/bin/python
fi

# Upgrade pip and install requirements
venv/bin/python -m pip install --upgrade pip
if [ -f requirements.txt ]; then
  venv/bin/pip install -r requirements.txt
fi

# Always install nbstripout inside venv
venv/bin/pip install nbstripout
venv/bin/python -m ipykernel install --user --name=venv --display-name "Python (venv)"

# Register nbstripout filter only if inside a Git repo
if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Installing nbstripout Git filter locally..."
  echo "*.ipynb filter=nbstripout" > .gitattributes

  # Explicitly configure Git to use venv's Python for nbstripout
  git config filter.nbstripout.clean "venv/bin/python -m nbstripout"
  git config filter.nbstripout.smudge "venv/bin/python -m nbstripout"
fi

# Mark workspace as safe
if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git config --global --add safe.directory /workspaces/*
fi

# Optional custom setup
if [ -f .devcontainer/setup.sh ]; then
  bash .devcontainer/setup.sh
fi
