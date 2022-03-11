'''Controller'''
from prettytable import PrettyTable

from question_database_json import QuestionDatabaseJSON

class QuestionController():
    '''Controllers class for questions'''
    def __init__(self):
        self.questions = []
        self.database = QuestionDatabaseJSON("data.json")

    def add_question(self):
        '''Adding a question'''
        self.questions.append("question")
        print("adding a question")

    def print_questions(self):
        '''Printing all questions'''
        table = PrettyTable(["Number", "Question Body", "Question Type"])
        for count, question in enumerate(self.database.questions):
            table.add_row([count + 1, question.body, type(question).__name__])
        print(table)
        while True:
            try:
                i = input("Enter:\n0 to go back\nQuestion number to print that question: ")
                if int(i) <= len(self.database.questions) + 1 and int(i) > 0:
                    self.database.questions[int(i) - 1].print()
                elif int(i) == 0:
                    break
                else:
                    print("Wrong input")
            except ValueError():
                print("Wrong input")
