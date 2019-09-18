#!/usr/bin/python3

class SiteMapGenerator:
    OUTPUT_PATH = "./publish/sitemap.xml"
    
    files = [ ]

    def __init__(self):
        pass

    def add(self, file_path, last_date, priority = 0.5):
        self.files.append([file_path, last_date, priority])

    def bake(self):
        with open(self.OUTPUT_PATH, "w") as f:
            f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
            f.write("<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">")
            
            for file in self.files:
                f.write("<url>")
                [file_path, last_date, priority] = file
                f.write("<loc>" + file_path + "</loc>")
                f.write("<lastmod>" + last_date + "</lastmod>")
                f.write("<priority>" + str(priority) + "</priority>")
                f.write("</url>")

            f.write("</urlset>")

    def additionalAdd(self):
        # Add files here.
        pass