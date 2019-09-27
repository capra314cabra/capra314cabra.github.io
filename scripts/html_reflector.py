import os
import re
from typing import *

from site_db import SiteDB

class HTMLReflector:
    content: AnyStr = None
    pattern = None
    site_info: Dict[AnyStr, AnyStr] = { }
    site_db: SiteDB = None
    originalParam: Dict[AnyStr, AnyStr] = { }

    def __init__(self, content: AnyStr, site_info: Dict[AnyStr, AnyStr], site_db: SiteDB):
        self.content = content
        self.pattern = re.compile(".*?(<!--cprext (.*)-->).*")
        self.site_info = site_info
        self.site_db = site_db

    def add_original_param(self, name: AnyStr, value: AnyStr):
        #
        # Append the param
        #
        self.originalParam[name] = value

    def reflect_all(self) -> str: #):
        #
        # Get text generated
        #
        return self.reflect_lines(self.content)

    def reflect_lines(self, content: AnyStr) -> AnyStr: #):
        #
        # Run reflect() to each lines
        #
        new_val = ""
        for val in content.splitlines():
            new_val += self.reflect(val) + "\n"
        return new_val

    def reflect(self, content: AnyStr) -> AnyStr: #):
        #
        # Check whether it contains cprext command or not
        #
        result = self.pattern.match(content)
        if result:
            #
            # This value should be formated like this: <!--cprext hoge huga-->
            #
            matched_value = result.group(1)
            #
            # This value should be formated like this: hoge huga
            #
            matched_arg = result.group(2)
            #
            # Run as args given
            #
            replace_to_value = self.calc(matched_arg)
            #
            # Replace old with text generated
            #
            print("\"{}\" will be replaced with \"{}\"".format(matched_value, replace_to_value))
            new_val = content.replace(matched_value, replace_to_value)

            return self.reflect_lines(new_val)
        else:
            return content

    def calc(self, arg: AnyStr) -> AnyStr: #):
        arg_list = arg.split(" ")
        if arg_list[0] == "load":
            #
            # Load command
            #
            return self.site_info[arg_list[1]]
        elif arg_list[0] == "load_original":
            #
            # Load Original command
            #
            return self.originalParam[arg_list[1]]
        elif arg_list[0] == "link":
            #
            # Link command
            #
            fmt = \
            "<a href=\"{}\"><div class=\"mylink\">\n" \
            "<img class=\"mylink_image\" alt=\"Link\" src=\"{}\" alt=\"Link\">\n" \
            "<p class=\"mylink_text\">{}</p>\n" \
            "</div></a>"
            link_to_info = self.site_db.get_page_by_name(arg_list[1])
            return fmt.format(link_to_info["url"], link_to_info["image"], link_to_info["title"])
        else:
            raise NotImplementedError(arg)
