#!/usr/bin/env bash
set -e

rm -rf build dist *.egg-info
python setup.py sdist
python setup.py bdist_wheel
