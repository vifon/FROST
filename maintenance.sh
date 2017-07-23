#!/bin/bash
set -eu

find * -type d |
    while read
    do
        if [ ! -e "$REPLY/.gitkeep" ]; then
            echo "Creating $REPLY/.gitkeep"
            touch "$REPLY/.gitkeep"
        fi
    done
