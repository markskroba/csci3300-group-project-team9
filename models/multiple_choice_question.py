from .question import *
class MultipleChoiceQuestion(Question):
    def __init__(self, body, answers, first_used, last_used, difficulty):
        super().__init__(body, first_used, last_used, difficulty)
        self.answers = answers

    def add_answer(self, answer):
        self.answers.append(answer)

    def print(self):
        print(self.body)

        for i in range(len(self.answers)):
            
            correct = ""
            if self.answers[i]["correct"]:
                correct = ", CORRECT"
            print(f'Answer {i+1}: {self.answers[i]["body"]}{correct}')


    