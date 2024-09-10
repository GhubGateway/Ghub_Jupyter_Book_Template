#!/bin/sh

scriptDir=$(dirname $(readlink -f $0))

cd ${scriptDir}/../template_jupyter_book/_build/html

python -m http.server --bind 127.0.0.1 8080
