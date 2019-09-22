#!/usr/bin/python3

class SiteMapGenerator:
    OUTPUT_PATH = "./publish/sitemap.xml"
    
    files = [ ]

    def __init__(self):
        pass

    def add(self, file_path, last_date, priority = 0.5, bilingual = []):
        self.files.append([file_path, last_date, priority, bilingual])

    def bake(self):
        with open(self.OUTPUT_PATH, "w") as f:
            f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
            f.write("<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\"\n")
            f.write("xmlns:xhtml=\"http://www.w3.org/1999/xhtml\">\n")
            
            for file in self.files:
                f.write("<url>\n")
                [file_path, last_date, priority, bilingual] = file
                f.write("\t<loc>" + file_path + "</loc>\n")
                f.write("\t<lastmod>" + last_date + "</lastmod>\n")
                f.write("\t<priority>" + str(priority) + "</priority>\n")
                for lang in bilingual:
                    f.write("\t\t<xhtml:link rel=\"alternate\"\n")
                    f.write("\t\threflang=\""+ lang["lang"] + "\"\n")
                    f.write("\t\thref=\""+ lang["link"] + "\"\n")
                    f.write("\t\t/>\n")
                f.write("</url>\n")

            f.write("</urlset>\n")

    def additionalAdd(self):
        # Add files here.
        pass