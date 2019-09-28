import os
import re
import datetime as dt
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
            print("\"{}\" will be replaced with \"{}\"".format(matched_value, (replace_to_value + "\n").splitlines()[0]))
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
            # Usage: <!--cprext load [the name of the parameter which you want to get]-->
            #
            return self.site_info[arg_list[1]]
        elif arg_list[0] == "load_original":
            #
            # Load Original command
            #
            # Usage: <!--cprext load_original [the name of the prameter which you want to get]-->
            #
            return self.originalParam[arg_list[1]]
        elif arg_list[0] == "link":
            #
            # Link command
            #
            # Usage: <!--cprext link [the basename of the url which you want to link]-->
            #
            return self.generate_internal_link(self.site_db.get_page_by_name(arg_list[1]))
        elif arg_list[0] == "list":
            #
            # List command
            #
            # Usage: <!--cprext list [the name of the tag, which will be used for filtering]-->
            #
            generated_text = ""
            for site in self.site_db.get_pages():
                if site["tag"] == arg_list[1]:
                    generated_text += self.generate_internal_link(site)
            return generated_text
        elif arg_list[0] == "order_by_date":
            #
            # Order by Date command
            #
            # Usage: <!--cprext order_by_date [contents count]-->
            #
            site_infos = self.site_db.get_pages()
            order_by = lambda sinfo : dt.date( \
                int(sinfo["lastdate"].split("-")[0]), \
                int(sinfo["lastdate"].split("-")[1]), \
                int(sinfo["lastdate"].split("-")[2]) \
            )
            site_infos = sorted(site_infos, key=order_by, reverse=True)
            generated_text = ""
            for i in range(int(arg_list[1])):
                if site_infos.__len__() > i:
                    generated_text += self.generate_internal_link(site_infos[i])
            return generated_text
        else:
            #
            # Not matched
            #
            raise NotImplementedError(arg)

    def generate_internal_link(self, link_to_info: Dict[AnyStr, AnyStr]) -> str: #):
        #
        # Format text with some parameters like this
        #
        fmt = \
        "<a href=\"{}\"><div class=\"mylink\">\n" \
        "   <img class=\"mylink_image\" alt=\"Link\" src=\"{}\" alt=\"Link\">\n" \
        "   <div class=\"mylink_content\">\n" \
        "       <p class=\"mylink_text\">{}</p>\n" \
        "       <p class=\"mylink_description\">{}</p>\n" \
        "   </div>\n" \
        "</div></a>\n"
        return fmt.format(link_to_info["url"], link_to_info["image"], link_to_info["title"], link_to_info["description"])
