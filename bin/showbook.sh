#!/bin/sh

scriptDir=$(dirname $(readlink -f $0))

cd ${scriptDir}/../jupyter-book-build-dir/_build/html

python -m http.server --bind 127.0.0.1 8080
