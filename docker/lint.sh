#!/usr/bin/env bash

set -euxo pipefail

echo "Running linters and formatters..."

black democritus_dates/ tests/

pylint --fail-under 9 democritus_dates/*.py

mypy democritus_dates/ tests/

isort democritus_dates/ tests/

flake8 democritus_dates/ tests/

bandit democritus_dates/
