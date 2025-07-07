@echo off
echo Installing uv...
python -m pip install --upgrade uv || exit /b

echo Installing dependencies with uv...
python -m uv pip install -e ".[dev,docu]" || exit /b

echo Done!