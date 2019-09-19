#!/usr/bin/python3

class OGPTagCreater:
    @staticmethod
    def replace(html_text, params):
        tags_location = "<!--importing ogp tags-->"
        ogp_tags = ""
        for param in params:
            [tag, val] = param
            ogp_tags += "<meta property=\"og:" + tag + "\" content=\"" + val + "\" />"
        return html_text.replace(tags_location, ogp_tags)
