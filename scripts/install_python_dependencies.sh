#!/bin/bash

# Fail immediately if any command exits with a non-zero status
set -e

echo "Initializing submodules..."
git submodule update --init --recursive

echo "Making sure pip is up to date..."
pip install --upgrade pip

echo "Installing uv..."
pip install uv

echo "Installing main project dependencies..."
uv pip install -e '.[dev,docu,jupy]'

echo "Installing submodule dependencies..."
SUBMODULE_PATH="bam_masterdata/dependencies/openbisschema"

if [ -d "$SUBMODULE_PATH" ]; then
    pushd "$SUBMODULE_PATH" > /dev/null
    uv pip install -e '.[test,doc]'
    popd > /dev/null
else
    echo "Submodule path $SUBMODULE_PATH does not exist. Initialization may have failed."
    exit 1
fi

echo "All dependencies installed successfully."
