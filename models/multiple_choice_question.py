'''Model for multiple choice question'''
from .question import Question
class MultipleChoiceQuestion(Question):
    '''Class for multiple choice question'''
    def __init__(self, body, answers, first_used, last_used, difficulty):
        super().__init__(body, first_used, last_used, difficulty)
        self.answers = answers

    def add_answer(self, answer):
        '''Adding a new answer'''
        self.answers.append(answer)

    def print(self):
        '''Printing question to the terminal'''
        print(self.body)
        for i in range(len(self.answers)):
            correct = ""
            if self.answers[i]["correct"]:
                correct = ", CORRECT"
            print(f'Answer {i+1}: {self.answers[i]["body"]}{correct}')

