#!/bin/bash
set -e

# Create Python virtual environment if missing
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python -m venv venv
fi

# Upgrade pip inside the venv
echo "Upgrading pip..."
venv/bin/python -m pip install --upgrade pip

# Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    venv/bin/pip install -r requirements.txt
else
    echo "No requirements.txt found, skipping..."
fi

# Git configuration
echo "Configuring git..."
git config --global pull.rebase false

# ------------------------------------------------------------
# Alias 1: First-time only — stitches histories together
# ------------------------------------------------------------
git config --global alias.upstream-once "!git pull upstream main --allow-unrelated-histories --no-edit"

# ------------------------------------------------------------
# Alias 2: Safe weekly update — preserves student copies
# ------------------------------------------------------------
git config --global alias.upstream-save '!f() { \
  git fetch upstream main && \
  git merge --no-edit upstream/main || true; \
  for f in $(git diff --name-only --diff-filter=U); do \
    git show :2:$f > "${f}.studentcopy"; \
    git checkout --theirs -- "$f"; \
    git add "$f" "${f}.studentcopy"; \
  done; \
  if [ -n "$(git diff --cached --name-only)" ]; then \
    git commit -m "Merge upstream/main, preserving student copies"; \
    echo "Your copy was saved as *.studentcopy. Edit as needed and rename to restore."; \
    echo "If you still see merge conflicts, rerun: git upstream-save until you see 'Already up to date.'"; \
  fi; \
}; f'

# ------------------------------------------------------------
# Alias 3: Bulletproof full class update — includes .devcontainer & .vscode
# ------------------------------------------------------------
git config --global alias.update-class '!f() { \
  echo "Fetching latest class repo updates..."; \
  git fetch upstream main; \
  echo "Restoring .devcontainer and .vscode folders..."; \
  git restore --source=upstream/main --staged --worktree -- .devcontainer .vscode || true; \
  echo "Merging code updates safely..."; \
  git merge --no-edit upstream/main || true; \
  for f in $(git diff --name-only --diff-filter=U); do \
    git show :2:$f > "${f}.studentcopy"; \
    git checkout --theirs -- "$f"; \
    git add "$f" "${f}.studentcopy"; \
  done; \
  if [ -n "$(git diff --cached --name-only)" ]; then \
    git commit -m "Merge upstream/main (preserved student copies)"; \
  fi; \
  echo "? Update complete! Any conflicts were saved as *.studentcopy."; \
  echo "?? Next: Rebuild your container (Full) from the Command Palette."; \
}; f'

echo "? Setup complete!"
echo "?? First time only: git upstream-once"
echo "?? Weekly updates: git upstream-save"
echo "?? Full environment + code sync: git update-class"

