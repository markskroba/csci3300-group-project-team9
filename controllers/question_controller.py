'''Controller'''
from datetime import datetime
from prettytable import PrettyTable

from question_database_json import QuestionDatabaseJSON

from models.multiple_choice_question import MultipleChoiceQuestion
from models.short_answer_question import ShortAnswerQuestion
from models.fill_in_question import FillInQuestion

class QuestionController():
    '''Controllers class for questions'''
    def __init__(self):
        self.database = QuestionDatabaseJSON("data.json")
        self.methods_used = 0

    def get_dates(self):
        '''Get first used and last used dates for specific question'''
        while True:
            try:
                first_used_i = input("""When was this question first used?
(month-day-year) (ENTER for now):""")
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
                last_used_i = input("""When was this question last used?
(month-day-year) (ENTER for now):""")
                if last_used_i == "":
                    last_used = int(datetime.today().timestamp())
                else:
                    month, day, year = last_used_i.split("-")
                    last_used = int(datetime(int(year), int(month), int(day)).timestamp())
                break
            except ValueError:
                print("Wrong input")
                continue

        when_used = {"first_used": first_used, "last_used": last_used}
        self.methods_used += 1
        return when_used

    def get_multiple_choice_answers(self):
        '''Get answers for multiple choice question'''
        answers = []
        print("You will now enter answers for your multiple choice question")
        answer_counter = 0
        while True:
            answer_body = input(f'Enter answer #{answer_counter}: ')
            answer_correct = bool(input("""Is this answer true or false?
Enter 1 for true and anything else (like 0) for false: """) == "1")

            answers.append({"body": answer_body, "correct": answer_correct})
            answer_counter += 1
            i = input("Enter 1 if you want to add one more answer: ")
            if i != "1":
                break
        self.methods_used += 1
        return answers

    def get_fill_in_answers(self):
        '''Get answers for fill in the blank question'''
        answers = []
        answer_counter = 0
        print("You will now enter answers for your fill in the blank question")
        while True:
            answer_body = input(f'Enter answer #{answer_counter}: ')
            answers.append(answer_body)

            i = input("Enter 1 if you want to add one more answer: ")
            if i != "1":
                break
        self.methods_used += 1
        return answers

    def get_short_answer_properties(self):
        '''Get maximum word count for an answer and key points for it'''
        while True:
            max_word_count = input("Enter the max word count for the answer: ")
            try:
                max_word_count = int(max_word_count)
                break
            except TypeError:
                print("Wrong input")
                continue
        print("You will now enter key points that should be addressed in a correct answer")
        key_points = []
        while True:
            key_point = input("""Enter one key point
or 0 if you don't want to enter any more: """)
            if key_point != "0":
                key_points.append(key_point)
            else:
                break

        self.methods_used += 1
        return max_word_count, key_points

    def add_question(self):
        '''Adding a question'''

        while True:
            question_type_i = input("""Select question type:
1 for multiple choice question
2 for fill in the blank question
3 for short answer question
0 to quit: """)
            if question_type_i not in ["1","2","3","0"]:
                print("Wrong input")
                continue
            if question_type_i == "0":
                break
            body = input("Enter your question: ")
            # getting dates
            when_used = self.get_dates()
            # getting difficulty
            while True:
                difficulty = input("Enter you question's difficulty, from 1 to 5: ")
                if difficulty in ["1", "2", "3", "4", "5"]:
                    difficulty = int(difficulty)
                else:
                    print("Wrong input")
                    continue
                break

            # getting question arguments
            if question_type_i == "1":
                # multiple choice
                answers = self.get_multiple_choice_answers()
                question = MultipleChoiceQuestion(body, when_used, difficulty, answers)
                self.database.submit_question(question)

            elif question_type_i == "2":
                # fill in the blank
                answers = self.get_fill_in_answers()
                question = FillInQuestion(body, when_used, difficulty, answers)
                self.database.submit_question(question)

            elif question_type_i == "3":
                # short answer
                max_word_count, key_points = self.get_short_answer_properties()
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
