#!/usr/bin/python3

import os
import glob
import json
import sitemap_generator as sg
import ogp_tag_creater as ogp

HEADER_HTML_PATH = "./header.html"
FOOTER_HTML_PATH = "./footer.html"

# Initalize sitemap generator
sitemap_generator = sg.SiteMapGenerator()

# Read header contents
header_contents = ""
with open(HEADER_HTML_PATH, "r") as f:
    header_contents = f.read()

# Read footer contents
footer_contents = ""
with open(FOOTER_HTML_PATH, "r") as f:
    footer_contents = f.read()

# Do to each files
pattern = glob.glob("./contents/**/*.html", recursive=True)
for file in pattern:

    print("Load html file: " + file)

    # Load a HTML file
    file_content = ''
    with open(file, "r") as f:
        file_content = f.read()

    # Get a setting file
    fileWithoutExtension = os.path.splitext(file)[0]
    settingFile = fileWithoutExtension + ".json"

    # Load a setting file
    settingData = { }
    with open(settingFile, "r") as f:
        settingData = json.load(f)

    # Get the path where it will be published
    publishFile = settingData["output_to"] + os.path.basename(file)

    # Add this to the consists of sitemap generator
    relative_path = "https://capra314cabra.github.io/" + os.path.basename(file)
    sitemap_generator.add(relative_path, settingData["lastdate"], settingData["priority"], settingData["bilingual"])

    # Concatenate header and footer
    file_content = header_contents + file_content + footer_contents

    # Add opg tags
    opg_tag_content = []
    opg_tag_list = ["title", "type", "url", "image", "description", "site_name"]
    for tag in opg_tag_list:
        opg_tag_content.append([tag, settingData[tag]])
    file_content = ogp.OGPTagCreater.replace(html_text=file_content, params=opg_tag_content)

    # Bake HTML file
    with open(publishFile, "w") as f:
        f.write(file_content)

    print("Finished")

print("Start baking sitemap.xml ...")

# Bake a sitemap.xml
sitemap_generator.bake()

print("Finished")