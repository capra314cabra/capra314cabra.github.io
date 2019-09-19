#!/bin/bash

#
# Run tasks
#

runItems=("tsc" "./scripts/css_builder.py" "./scripts/html_builder.py" "./scripts/image_builder.py")

for script in ${runItems[@]}
do
    echo "Running $script ..."
    $script
    echo "Finished"
done

#
# Additional tasks
#

cp ./googlec0a860b5fd253174.html ./publish/googlec0a860b5fd253174.html