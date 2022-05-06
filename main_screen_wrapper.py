'''Class that holds the wrapper methods for main screen'''
from datetime import datetime
import PySimpleGUI as sg
from question_database_json import QuestionDatabaseJSON

class MainWrapper():
    '''Controller class for the main screen'''
    def __init__(self, data_location):
        self.database = QuestionDatabaseJSON(data_location)
        self.question_list = []
        for item in self.database.questions:
            self.question_list.append(item)

    def get_details(self, event):
        '''This method takes in the list of questions from the database,
            searches the list for a specific question, then returns the
            questions and answers. Can be expanded to include other
            properties such as date used and difficulty.'''
        for item in self.question_list:
            if event == item.body:
                return [item.body, item.get_formatted_answers(), item.difficulty, item.type]
        print("Error - question not in database")
        return []

    def create_buttons(self, row_length):
        '''Takes in the list of questions from the database and
            creates PySimpleGUI buttons. Will construct them in rows of
            size row_length. This method returns a list of lists,
            where the inner lists are row of buttons.'''
        button_list = []
        row = []
        for question in self.question_list:
            if len(row)>=row_length:
                button_list.append(row)
                row = []
            row.append(sg.Button(question.body))
        button_list.append(row)
        return button_list

    def filtered_buttons(self, criteria):
        '''Takes in a list of criteria, and returns list of questions that DONT fit that criteria.
            To be used in main_screen to disable buttons that are in this list.'''
        filtered = []
        clean = []
        for question in self.question_list:
            if criteria != []:
                if criteria[0] not in (question.type, '', 'General'):
                    filtered.append(question.body)
                elif criteria[1] not in (question.difficulty, ''):
                    filtered.append(question.body)
                elif criteria[2] not in (''):
                    if int(datetime.strptime(criteria[2], "%m/%d/%Y").timestamp()) \
                         < question.first_used:
                        filtered.append(question.body)
                elif criteria[3] not in (question.last_used, ''):
                    if int(datetime.strptime(criteria[3], "%m/%d/%Y").timestamp()) \
                        < question.last_used:
                        filtered.append(question.body)
                elif criteria[4] not in (''):
                    if question.body is not None \
                        and criteria[4].lower() not in question.body.lower():
                        filtered.append(question.body)
                else:
                    clean.append(question.body)
        return filtered,clean
        