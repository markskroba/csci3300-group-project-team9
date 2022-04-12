'''Model for fill in the blank question'''
from models.question import Question

class FillInQuestion(Question):
    '''
    Class for fill in the blank question
    body: String where "blanks" are denoted by multiple underscores '_'
    answers: List of strings of answers that correspond to blanks
    '''
    def __init__(self, body, when_used, difficulty, answers):
        super().__init__(body, when_used, difficulty)
        self.answers = answers
        self.type = "Fill In"

    def print(self):
        '''Prints the question (for non-GUI version)'''
        super().print()
        print("Question type: Fill in the blank question")
        print(f'Answers: {", ".join(self.answers)}')
        