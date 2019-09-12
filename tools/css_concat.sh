#!/bin/bash

SCRIPT_FULL_PATH=`readlink -f $0`
STYLE_SHEET_PATH="../homepage-min.css"

pushd `dirname $SCRIPT_FULL_PATH` > /dev/null
    pushd "../style" > /dev/null
        cat /dev/null > "$STYLE_SHEET_PATH"
        for css_file in ./*.css
        do
            cat $css_file >> "$STYLE_SHEET_PATH"
            echo "Appended $css_file"
        done
    popd > /dev/null
popd > /dev/null
