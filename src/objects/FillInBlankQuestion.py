#Author: Trey Roche
#Class file for a fill-in-the-blank question containing a sentence with a blank in it and an answer.

class FillInBlankQuestion:

    def __init__(self, before=None, after=None, answer=None):
        self.before = before
        self.after = after
        self.answer = answer
    
    def addBefore(self, before):
        self.before = before

    def addAfter(self, after):
        self.after = after    

    def addAnswer(self, answer):
        self.answer = answer
    