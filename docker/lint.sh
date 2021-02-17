#!/usr/bin/env bash

set -euxo pipefail

echo "Running linters and formatters..."

isort democritus_dates/ tests/

black democritus_dates/ tests/

pylint --fail-under 9 democritus_dates/*.py

mypy democritus_dates/ tests/

flake8 democritus_dates/ tests/

bandit democritus_dates/

# we run black again at the end to undo any odd changes made by any of the linters above (e.g. isort)
black democritus_dates/ tests/
