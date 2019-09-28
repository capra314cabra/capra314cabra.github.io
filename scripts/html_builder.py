import os
import glob
import json
import sitemap_generator as sg
from html_reflector import HTMLReflector
import site_db as db

TEMPLATE_HTML_PATH = "./template.html"

#
# Initalize sitemap generator
#
sitemap_generator = sg.SiteMapGenerator()
site_db = db.SiteDB()

#
# Read template contents
#
template_content = ""
with open(TEMPLATE_HTML_PATH, "r") as f:
    template_content = f.read()
#
# Do to each files
#
pattern = glob.glob("./contents/**/*.html", recursive=True)
for file in pattern:

    print("Load html file: " + file)

    #
    # Load a HTML file
    #
    file_content = ''
    with open(file, "r") as f:
        file_content = f.read()
    #
    # Load site data
    #
    file_name = os.path.basename(file)
    site_data = site_db.get_page_by_name(file_name)
    #
    # Get the path where it will be published
    #
    publishFile = site_data["output_to"] + os.path.basename(file)
    #
    # Add this to the consists of sitemap generator
    #
    sitemap_generator.add(site_data["url"], site_data["lastdate"], site_data["priority"], site_data["bilingual"])
    #
    # Initialize Variable Reflector
    #
    ref = HTMLReflector(template_content, site_info=site_data, site_db=site_db)
    #
    # Concatenate header and footer
    #
    ref.add_original_param("main_contents", file_content)
    #
    # Bake HTML file
    #
    file_content = ref.reflect_all()
    with open(publishFile, "w") as f:
        f.write(file_content)

    print("Finished")

print("Start baking sitemap.xml ...")

#
# Bake a sitemap.xml
#
sitemap_generator.bake()

print("Finished")