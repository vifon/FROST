#!/bin/bash
set -eu

ARGS=""
while getopts "q" ARG; do
    case "$ARG" in
        q)
            ARGS+=" --quiet"
        ;;
        '?')
        ;;
    esac
done
shift $((OPTIND-1))

find * -name "*$1*" -type f -exec ./show.py $ARGS '{}' '+'
