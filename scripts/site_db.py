import os
import glob
import json
from typing import *

class SiteDB:
    pages: List[Dict[AnyStr, AnyStr]] = []
    
    def __init__(self):
        #
        # Read each json files
        #
        site_info_files = glob.glob("./contents/**/*.json", recursive=True)
        for site_info_file in site_info_files:
            #
            # Load json file
            #
            site_info_dict = { }
            with open(site_info_file, "r") as f:
                site_info_dict = json.load(f)
            self.pages.append(site_info_dict)

    def get_page_by_name(self, name: str) -> Dict[AnyStr, AnyStr]: #):
        #
        # If the basename of "url" and "name" are equivalent, it must be the same
        #
        for page in self.pages:
            page_name = os.path.basename(page["url"])
            if page_name == name:
                return page
        return None

    def get_pages(self) -> List[Dict[AnyStr, AnyStr]]: #):
        return self.pages
