'''
Main file
'''
from controllers.question_controller import QuestionController

controller = QuestionController()
while True:
    i = input("Enter: \n1 to add a question\n2 to view added questions\nQ to exit: ")

    if i == "1":
        # logic for adding a question
        controller.add_question()
    elif i == "2":
        # logic for printing all questions
        controller.print_questions()
    elif i == "Q":
        break
    else:
        print("Wrong input")
