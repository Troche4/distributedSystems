class MCQuestion:

    def __init__(self, prompt=None, answer=None, options=list()):
        self.prompt = prompt
        self.answer = answer
        self.options = options
    
    def addPrompt(self, prompt):
        self.prompt = prompt

    def addOption(self, option):
        self.options.append(option)
    
    def addAnswer(self, answer):
        self.answer = answer