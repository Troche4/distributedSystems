# Program designed to take in an XML file and translate it into quiz data for output in Python.
# Resources used: ElementTree API in Python libraries (docs.python.org)

import xml.etree.ElementTree as etree
import objects
import random


class InstructorXMLParser:

    def __init__(self, url=None):
        self.url = url

    def parse(self):
        url = self.url
        if url == None:
            url = input("Enter your xml file here, including its path: ")
        tree = etree.parse(url)  
        root = tree.getroot()
        quiz = objects.quiz()
        for child in root:
            if child.tag == "title":  
                quiz.addTitle(child.text)
            elif child.tag == "directions":  
                quiz.addDirections(child.text)
            elif child.tag == "question":  
                if child.attrib.get("type") in ["short-answer", "true-false", "multiple-choice"]: # question is MC, T/F, or short answer
                    mcQuestion = objects.MCQuestion(None, list())
                    if len(mcQuestion.options) > 0:
                        mcQuestion.options = list()
                    components = child.iter()
                    for element in components:
                        if element.tag == "prompt": 
                            mcQuestion.addPrompt(element.text)
                        elif element.tag == "option": 
                            mcQuestion.addOption(element.text)
                        elif element.tag == "answer":
                            mcQuestion.addOption(element.text)
                            mcQuestion.addAnswer(element.text)
                    quiz.addQuestion(mcQuestion)
                elif child.attrib.get("type") == "fill-in-blank": # question is fill-in-the-blank
                    FIBQuestion = objects.FillInBlankQuestion(None, None)
                    components = child.iter()
                    for element in components:
                        if element.tag == "before": 
                            FIBQuestion.addBefore(element.text)
                        elif element.tag == "after":  
                            FIBQuestion.addAfter(element.text)
                        elif element.tag == "answer":
                            FIBQuestion.addAnswer(element.text)
                    quiz.addQuestion(FIBQuestion)
                elif child.attrib.get("type") == "matching":  # question is matching
                    MatchQuestion = objects.MatchingQuestion(None, None, None, None)
                    components = child.iter()
                    for element in components:
                        if element.tag == "prompt":  
                            MatchQuestion.addPrompt(element.text)
                        elif element.tag == "set1":# group of elements in the left column that have to be assigned to set 2 (the keys)
                            set1 = str(element.text).split(" ")
                            random.shuffle(set1)
                            MatchQuestion.addSet1(set1)
                        elif element.tag == "set2":  # group of elements in the right column that have to be matched (the values)
                            set2 = str(element.text).split(" ")
                            random.shuffle(set2)
                            MatchQuestion.addSet2(set2)
                        elif element.tag == "answer": #group of elements that consist of the left column sorted according to the right (the answer)
                            answer = str(element.text).split(" ")
                            MatchQuestion.addAnswer(answer)
                    quiz.addQuestion(MatchQuestion)
        return quiz

if __name__ == "__main__":
    test = InstructorXMLParser("src/sampleQuiz.xml")
    quiz = test.parse()
    print(quiz.title + "\n")
    print(quiz.directions + "\n")
    for question in quiz.questions:
        if isinstance(question, objects.MCQuestion):
            print(question.prompt)
            for option in question.options:
                print(option)
        elif isinstance(question, objects.FillInBlankQuestion):
            print(question.before + "_______" + question.after)
        else:
            print(question.prompt)
            print(question.set1)
            print(question.set2)
        print("\n\n")