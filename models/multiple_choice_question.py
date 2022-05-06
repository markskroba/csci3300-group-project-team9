'''Model for multiple choice question'''
from models.question import Question
class MultipleChoiceQuestion(Question):
    '''
    Class for multiple choice question
    answers: List of objects with two properties:
        body: Text of an answers,
        correct: Boolean determining whether that answer was correct
    '''
    def __init__(self, body, when_used, difficulty, answers):
        super().__init__(body, when_used, difficulty)
        self.answers = answers
        self.type = "Multiple Choice"

    def add_answer(self, answer):
        '''Adding a new answer'''
        self.answers.append(answer)

    def print(self):
        '''Printing question to the terminal'''
        super().print()
        print("Question type: Multiple Choice")

        for counter, answer in enumerate(self.answers):
            correct = ""
            if answer["correct"]:
                correct = ", CORRECT"
            print(f'Answer {counter+1}: {answer["body"]}{correct}')

    def get_formatted_answers(self):
        '''This formats the answers of the question in a way that works well with the main \
            screen'''
        formatted = ""
        for item in self.answers:
            formatted += str(item["correct"]) + ": " + item["body"] + "\n"
        return formatted + "\n"