'''Class that holds the wrapper methods for main screen'''
import PySimpleGUI as sg
from question_database_json import QuestionDatabaseJSON

class MainWrapper():
    '''Controller class for the main screen'''
    def __init__(self, data_location):
        self.database = QuestionDatabaseJSON(data_location)
        self.database.fetch_questions()

        self.question_list = []
        for x in self.database.questions:
            self.question_list.append(x)

    def get_details(self, event):
        '''This method takes in the list of questions from the database, searches the list for a specific question, 
        then returns the questions and answers. Can be expanded to include other properties such as date used and difficulty.'''
        for item in self.question_list:
            if event == item.body:
                return [item.body, item.answers]
        print("Error - question not in database")
        return []

    def format_answers(self, answer_list):
        '''The list of answers from each question needs to be formatted in a presentable way. 
            This takes the in that list the returns a string that starts with true/false attribute, then answer.'''
        formatted = ""
        for item in answer_list:
            formatted += str(item["correct"]) + ": " + item["body"] + "\n"
        return formatted

    def create_buttons(self, row_length):
        '''Takes in the list of questions from the database and creates PySimpleGUI buttons. Will construct them in rows of
            size row_length. This method returns a list of lists, where the inner lists are row of buttons.'''
        button_list = []
        row = []
        for question in self.question_list:
            if(len(row)>=row_length):
                button_list.append(row)
                row = []
            row.append(sg.Button(question.body))
        button_list.append(row)
        return button_list
