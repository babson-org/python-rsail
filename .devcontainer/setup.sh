#!/bin/bash
set -e

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python -m venv venv
fi

# Upgrade pip inside the venv
echo "Upgrading pip..."
venv/bin/python -m pip install --upgrade pip

# Install dependencies
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    venv/bin/pip install -r requirements.txt
else
    echo "No requirements.txt found, skipping..."
fi

# Git configuration for all users in container
echo "Configuring git..."
git config --global pull.rebase false

# Alias 1: First-time only, stitches histories together
git config --global alias.upstream "!git pull upstream main --allow-unrelated-histories --no-edit"



echo "? Setup complete!"


