'''Controller'''
from question_database_json import QuestionDatabaseJSON

from models.multiple_choice_question import MultipleChoiceQuestion
from models.short_answer_question import ShortAnswerQuestion
from models.fill_in_question import FillInQuestion

from controllers.io_controller_cli import IOControllerCLI

class QuestionController():
    '''Controllers class for questions'''
    def __init__(self):
        self.database = QuestionDatabaseJSON("data.json")
        self.io_controller = IOControllerCLI()

    def add_question(self):
        '''Adding a question'''

        while True:
            question_type_i = self.io_controller.get_question_type()

            if question_type_i not in ["1","2","3","0"]:
                self.io_controller.show_error_message("Wrong input")
                continue
            if question_type_i == "0":
                break
            body = self.io_controller.get_body()
            # getting dates
            when_used = self.io_controller.get_dates()
            # getting difficulty
            while True:
                difficulty = self.io_controller.get_difficulty()
                if difficulty in ["1", "2", "3", "4", "5"]:
                    difficulty = int(difficulty)
                else:
                    self.io_controller.show_error_message("Wrong input")
                    continue
                break

            # getting question arguments
            if question_type_i == "1":
                # multiple choice
                answers = self.io_controller.get_multiple_choice_answers()
                question = MultipleChoiceQuestion(body, when_used, difficulty, answers)
                self.database.submit_question(question)

            elif question_type_i == "2":
                # fill in the blank
                answers = self.io_controller.get_fill_in_answers()
                question = FillInQuestion(body, when_used, difficulty, answers)
                self.database.submit_question(question)

            elif question_type_i == "3":
                # short answer
                max_word_count, key_points = self.io_controller.get_short_answer_properties()
                question = ShortAnswerQuestion(body,
                when_used,
                difficulty,
                {"max_word_count": max_word_count, "key_points": key_points})
                self.database.submit_question(question)



    def print_questions(self):
        '''Printing all questions'''
        self.io_controller.print_all_question(self.database.questions)
        while True:
            try:
                i = self.io_controller.get_question_number()
                if int(i) <= len(self.database.questions) + 1 and int(i) > 0:
                    self.io_controller.print_specific_question(self.database.questions, i)
                elif int(i) == 0:
                    break
                else:
                    self.io_controller.show_error_message("Wrong input")
            except ValueError():
                self.io_controller.show_error_message("Wrong input")
