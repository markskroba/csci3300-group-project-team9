'''
Main file
'''
while True:
    i = input("Enter: \n1 to add a question\n2 to view added questions\nQ to exit: ")

    if i == "1":
        questionType = input("Enter: \n1 for Multiple choice\n2 for Fill in the blank\n3 for Short answer or \n4 for Essay: ")
        if questionType == "1":
            # logic for multiple choice question
            pass
        elif questionType == "2":
            # logic for fill in the blank question
            pass
        elif questionType == "3":
            # logic for short answer question
            pass
        elif questionType == "4":
            # logic for essay question
            pass
        else:
            print("Wrong input")
        pass
    elif i == "2":
        # logic for printing all questions
        pass
    elif i == "Q":
        break
    else:
        print("Wrong input")
