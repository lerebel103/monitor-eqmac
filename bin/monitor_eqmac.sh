#!/bin/sh

DIR="$( cd "$( dirname "$0" )" && pwd )"

# Check if the base directory is here or in the parent directory
BASE_DIR="$DIR"
if [ -e "$DIR"/../main.py ]; then
    BASE_DIR="$DIR/.."
fi

. "$BASE_DIR"/.venv/bin/activate
python3 "$BASE_DIR"/main.py "$@"

