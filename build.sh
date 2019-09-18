#!/bin/bash

SCRIPT_FULL_PATH=`readlink -f $0`

runItems=("tsc" "./scripts/css_builder.py" "./scripts/html_builder.py" "./scripts/image_builder.py")

for script in ${runItems[@]}
do
    echo "Running $script ..."
    $script
    echo "Finished"
done