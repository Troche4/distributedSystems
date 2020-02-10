# Program designed to take in an XML file and translate it into response data for output in Python.
# Resources used: ElementTree API in Python libraries (docs.python.org)

import xml.etree.ElementTree as etree
import objects

class StudentXMLParser:

    def __init__(self, url=None):
        self.url = url

    def parse(self):
        url = self.url
        if url == None:
            url = input("Enter your xml file here, including its path: ")
        tree = etree.parse(url)
        root = tree.getroot()
        response = objects.response()
        for child in root:
            if child.tag == "name":
                response.addName(child.text)
            elif child.tag == "answer":
                response.addAnswer(child.text)
        return response
    
if __name__ == "__main__":
    test = StudentXMLParser("src/sampleResponse.xml")
    response = test.parse()
    for ans in response.answers:
        print(ans)