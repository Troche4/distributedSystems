# Author: Trey Roche
# Program designed to take in an XML file and translate it into data for output in Python.
# Resources used: ElementTree API in Python libraries (docs.python.org)

import xml.etree.ElementTree as etree
import random


class XMLParser:

    def __init__(self, url=None):
        self.url = url

    def parse(self):
        if self.url == None:
            url = input("Enter your xml file here, including its path: ")
        tree = etree.parse(url)  # get XMl file
        root = tree.getroot()
        q_counter = 0  # question counting variable
        print("\n\n")

        for child in root:
            if child.tag == "title":  # found a <title> tag
                print(child.text, "\n\n")
            elif child.tag == "directions":  # found a <directions> tag
                print("Directions:", child.text, "\n\n")
            elif child.tag == "question":  # found a <question> tag
                q_counter += 1
                # question is MC, T/F, or short answer
                if child.attrib.get("type") in ["short-answer", "true-false", "multiple-choice"]:
                    components = child.iter()
                    for element in components:
                        if element.tag == "prompt":  # question text
                            print(q_counter, ":", element.text, "\n")
                        elif element.tag == "option":  # option for the user to select as an answer
                            print(element.text)
                        else:  # question component cannot be identified
                            print(element.text)
                    print("\n\n")
                # question is fill-in-the-blank
                elif child.attrib.get("type") == "fill-in-blank":
                    components = child.iter()
                    combinedStr = str()  # for building one output string with the blanks embedded
                    for element in components:
                        # element is part of the sentence
                        if element.tag in ["before", "after"]:
                            combinedStr += str(element.text)
                        elif element.tag == "blank":  # element is left blank for the user to fill in
                            combinedStr += ("_" * 10)
                        else:  # question component cannot be identified
                            combinedStr += str(element.text)
                    print(q_counter, ":", combinedStr)
                    print("\n\n")
                elif child.attrib.get("type") == "matching":  # question is matching
                    components = child.iter()
                    for element in components:
                        if element.tag == "prompt":  # question text
                            print(q_counter, ":", element.text, "\n")
                        # group of elements in the left column that have to be assigned to set 2 (the keys)
                        elif element.tag == "set1":
                            # catching text as a list for output
                            set1 = str(element.text).split(" ")
                        # group of elements in the right column that have to be matched (the values)
                        elif element.tag == "set2":
                            # catching text as a list for output
                            set2 = str(element.text).split(" ")
                        else:  # question component cannot be identified
                            print(element.text)
                    random.shuffle(set1)
                    random.shuffle(set2)
                    maxSize = max([len(set1), len(set2)])
                    for i in range(0, maxSize):
                        if i >= len(set1):
                            print("\t", set2[i], "\n")
                        elif i >= len(set2):
                            print(set1[i], "\n")
                        else:
                            print(set1[i], "\t", set2[i], "\n")
                    print("\n\n")
                else:  # question has no type
                    print("QUESTION TYPE NOT SPECIFIED")
                    print(
                        "Question types supported: matching, fill-in-blank, true-false, multiple-choice, short-answer", "\n")
            else:  # element is not a recognized tag
                print("ELEMENT NOT RECOGNIZED: ", child.tag, "\n")


if __name__ == "main":
    parse()


test = XMLParser()
test.parse()