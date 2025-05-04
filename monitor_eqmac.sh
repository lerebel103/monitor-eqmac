#!/bin/sh

DIR="$( cd "$( dirname "$0" )" && pwd )"

. "$DIR"/.venv/bin/activate
python3 "$DIR"/main.py "$@"

