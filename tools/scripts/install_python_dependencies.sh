#!/bin/bash

# Fail immediately if any command exits with a non-zero status
set -e

echo "Making sure pip is up to date..."
pip install --upgrade pip

echo "Installing uv..."
pip install uv

echo "Installing main project dependencies..."
uv pip install -e '.[dev,docu]'
