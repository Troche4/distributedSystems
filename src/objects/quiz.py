#Author: Trey Roche
#Class file for a quiz containing a title, directions, and list of questions (which may vary in type)

class quiz:

    def __init__(self, title=None, directions=None, questions=list()):
        self.title = title
        self.directions = directions
        self.questions = questions
    
    def addQuestion(self, question):
        self.questions.append(question)
    
    def addTitle(self, title):
        self.title = title

    def addDirections(self, directions):
        self.directions = directions