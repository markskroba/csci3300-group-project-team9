'''Controller'''
from prettytable import PrettyTable

from question_database_json import QuestionDatabaseJSON

from models.multiple_choice_question import MultipleChoiceQuestion
from models.short_answer_question import ShortAnswerQuestion
from models.fill_in_question import FillInQuestion

from controllers.input_controller_cli import IOControllerCLI 

class QuestionController():
    '''Controllers class for questions'''
    def __init__(self):
        self.database = QuestionDatabaseJSON("data.json")
        self.input_controller = IOControllerCLI()

    def add_question(self):
        '''Adding a question'''

        while True:
            question_type_i = self.input_controller.get_question_type()

            if question_type_i not in ["1","2","3","0"]:
                print("Wrong input")
                continue
            if question_type_i == "0":
                break
            body = self.input_controller.get_body()
            # getting dates
            when_used = self.input_controller.get_dates()
            # getting difficulty
            while True:
                difficulty = self.input_controller.get_difficulty()
                if difficulty in ["1", "2", "3", "4", "5"]:
                    difficulty = int(difficulty)
                else:
                    print("Wrong input")
                    continue
                break

            # getting question arguments
            if question_type_i == "1":
                # multiple choice
                answers = self.input_controller.get_multiple_choice_answers()
                question = MultipleChoiceQuestion(body, when_used, difficulty, answers)
                self.database.submit_question(question)

            elif question_type_i == "2":
                # fill in the blank
                answers = self.input_controller.get_fill_in_answers()
                question = FillInQuestion(body, when_used, difficulty, answers)
                self.database.submit_question(question)

            elif question_type_i == "3":
                # short answer
                max_word_count, key_points = self.input_controller.get_short_answer_properties()
                question = ShortAnswerQuestion(body,
                when_used,
                difficulty,
                {"max_word_count": max_word_count, "key_points": key_points})
                self.database.submit_question(question)



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
