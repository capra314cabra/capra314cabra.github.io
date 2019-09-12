#!/bin/bash

SCRIPT_FULL_PATH=`readlink -f $0`

runItems=("tsc" "./tools/css_concat.sh")

for script in ${runItems[@]}
do
    echo "Running $script ..."
    $script
    echo "Finished"
done