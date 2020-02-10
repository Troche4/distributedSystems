#Author: Trey Roche
#Class file for a matching question containing a prompt, two sets of terms to match, and an answer 
#Answer format is the first set, sorted to line up with the second set. 
#EX:
#   Set1   Set2     Answer
#   blue   rojo     red   
#   green  azul     blue
#   red    verde    green

class MatchingQuestion:

    def __init__(self, set1=None, set2=None, prompt=None, answer=None):
        self.prompt = prompt
        self.set1 = set1
        self.set2 = set2
    
    def addSet1(self, set1):
        self.set1 = set1

    def addSet2(self, set2):
        self.set2 = set2

    def addPrompt(self, prompt):
        self.prompt = prompt

    def addAnswer(self, answer):
        self.answer = answer
        #list of strings that are from set1, sorted according to set2.