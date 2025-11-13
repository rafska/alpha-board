#!/usr/bin/env bash

curl -LsSf https://astral.sh/uv/0.9.5/install.sh | sh

uv sync

# shellcheck disable=SC1091
source .venv/bin/activate

pre-commit install