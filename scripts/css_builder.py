#!/usr/bin/python3

import glob

OUTPUT_TO = "./publish/homepage-min.css"

files = glob.glob("./style/**/*.css", recursive=True)
file_contents = ""

for file in files:
    print("Found css: " + file)

    with open(file, "r") as f:
        file_contents += f.read()

print("Outputing...")

with open(OUTPUT_TO, "w") as f:
    f.write(file_contents)

print("Finished")
