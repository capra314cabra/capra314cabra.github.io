#!/bin/bash

#
# Predefined
#

taskColor="\e[44m"
runTask() {
    if [ $taskColor = "\e[44m" ]
    then
        taskColor="\e[42m"
    else
        taskColor="\e[44m"
    fi
    echo -e "$taskColor Running\e[m $1..."
    $1
    echo -e "$taskColor Finished\e[m $1"
}

#
# Add permissions
#

# None

#
# Build tasks
#

runTask "tsc"
runTask "python3 ./scripts/css_builder.py"
runTask "python3 ./scripts/html_builder.py"
runTask "python3 ./scripts/image_builder.py"

#
# Additional tasks
#

cp ./googlec0a860b5fd253174.html ./publish/googlec0a860b5fd253174.html