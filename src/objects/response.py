#Author: Trey Roche
#Class file for a quiz response containing a list of responses as strings.

class response:

    def __init__(self, answers=list(), name=None):
        self.answers = answers
    
    def addAnswer(self, answer):
        self.answers.append(answer)

    def addName(self, name):
        self.name = name