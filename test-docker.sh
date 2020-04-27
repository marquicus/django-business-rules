#!/usr/bin/env bash
set -e

./build.sh

docker build -t maciejpolanczyk/dbr-e2e -f tests/e2e/Dockerfile .
docker run -it maciejpolanczyk/dbr-e2e python3 manage.py test
