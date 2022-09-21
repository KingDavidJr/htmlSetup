import os.path

htmlCode = """<!DOCTYPE html>

<html lang = "en">
    <head>
        <meta charset = "utf-8">
        <title>[Enter Title]</title>
    </head>
        <body>
        </body>
<html>
"""


class startHTML:
    def __init__(self, fileName: str, pathName: str):
        self.fileName = fileName
        self.pathName = pathName

    def createHTML(self):
        completeFileName = os.path.join(self.pathName, self.fileName + ".html")
        # fileName = f"{self.fileName}.html"
        with open(completeFileName, 'w') as f:
            f.write(htmlCode)
            f.close()


save_path = "/Users/davidamedeka/Desktop"

name_of_file: str = input("Enter name of file: ")

start = startHTML(fileName=name_of_file, pathName=save_path)
start.createHTML()
