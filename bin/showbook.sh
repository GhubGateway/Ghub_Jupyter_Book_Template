#!/bin/sh

scriptDir=$(dirname $(readlink -f $0))

cd ${scriptDir}/../jupyter_book_contents/_build/html

python -m http.server --bind 127.0.0.1 8080
