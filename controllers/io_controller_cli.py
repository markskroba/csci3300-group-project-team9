'''Controller'''
from datetime import datetime
from prettytable import PrettyTable

class IOControllerCLI():
    '''Class for taking input from CLI'''

    def get_question_type(self):
        '''Get a question type to determine what type-specific arguments will be needed'''
        question_type = input("""Select question type:
1 for multiple choice question
2 for fill in the blank question
3 for short answer question
0 to quit: """)

        return question_type

    def get_body(self):
        '''Get body of a question'''
        i = input("Enter your question: ")
        return i

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
                self.show_error_message("Wrong input")
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
                self.show_error_message("Wrong input")
                continue

        when_used = {"first_used": first_used, "last_used": last_used}
        return when_used

    def get_difficulty(self):
        '''Get difficulty of question'''
        difficulty = input("Enter you question's difficulty, from 1 to 5: ")
        return difficulty

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

        return max_word_count, key_points

    def get_question_number(self):
        '''Get number of question that should be printed'''
        i = input("Enter:\n0 to go back\nQuestion number to print that question: ")
        return i

    def print_all_question(self, questions):
        '''Output all saved questions'''
        table = PrettyTable(["Number", "Question Body", "Question Type"])
        for count, question in enumerate(questions):
            table.add_row([count + 1, question.body, type(question).__name__])
        print(table)

    def print_question(self, questions, i):
        '''Output specific question based on its number in the table'''
        questions[int(i) - 1].print()

    def show_error_message(self, text):
        '''Output error message when needed'''
        print(text)