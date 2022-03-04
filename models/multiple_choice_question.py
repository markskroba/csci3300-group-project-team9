'''Model for multiple choice question'''
from question import Question
class MultipleChoiceQuestion(Question):
    '''Class for multiple choice question'''
    def __init__(self, body, answers, when_used, difficulty):
        super().__init__(body, when_used, difficulty)
        self.answers = answers

    def add_answer(self, answer):
        '''Adding a new answer'''
        self.answers.append(answer)

    def print(self):
        '''Printing question to the terminal'''
        print(self.body)
        for count, answer in enumerate(self.answers):
            correct = ""
            if answer["correct"]:
                correct = ", CORRECT"
            print(f'Answer {count+1}: {answer["body"]}{correct}')
