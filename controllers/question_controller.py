'''Controller'''
class QuestionController():
    '''Controllers class for questions'''
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        '''Adding a question'''
        self.questions.append(question)
        print("adding a question")

    def print_questions(self):
        '''Printing all questions'''
        print(self.questions)
        print("printing all questions")
