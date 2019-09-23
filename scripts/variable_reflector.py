class VariableReflector:
    html_text = ""

    def __init__(self, html_text):
        self.html_text = html_text

    def setParam(self, param_name, param_value):
        replace_text = "<!--importing " + param_name + "-->"
        self.html_text = self.html_text.replace(replace_text, param_value)

    def getHTMLText(self):
        return self.html_text