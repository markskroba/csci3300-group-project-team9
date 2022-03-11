'''Controller'''
from prettytable import PrettyTable
from datetime import datetime

from question_database_json import QuestionDatabaseJSON

class QuestionController():
    '''Controllers class for questions'''
    def __init__(self):
        self.database = QuestionDatabaseJSON("data.json")

    def add_question(self):
        '''Adding a question'''

        while True:
            question_type_i = input("Select question type:\n1 for multiple choice question\n2 for fill in the blank question\n3 for short answer question\n0 to quit: ")
            if question_type_i not in ["1","2","3", "Q"]:
                print("Wrong input")
                continue
            if question_type_i == "Q":
                continue
            body = input("Enter your question: ")
            # getting dates
            while True:
                try:
                    first_used_i = input("When was this question first used? (month-day-year) (ENTER for now):")
                    if first_used_i == "":
                        first_used = int(datetime.today().timestamp())
                    else:
                        month, day, year = first_used_i.split("-")
                        first_used = int(datetime(int(year), int(month), int(day)).timestamp())

                    break
                except ValueError:
                    print("Wrong input")
                    continue
            while True:
                try:
                    last_used_i = input("When was this question last used? (month-day-year) (ENTER for now):")
                    if last_used_i == "":
                        last_used = int(datetime.today().timestamp())
                    else:
                        month, day, year = last_used_i.split("-")
                        last_used = int(datetime(int(year), int(month), int(day)).timestamp())
                    break
                except ValueError:
                    print("Wrong input")
                    continue
            # getting question arguments
            if question_type_i == "1":
                pass
            elif question_type_i == "2":
                pass
            elif question_type_i == "3":
                pass

            

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
