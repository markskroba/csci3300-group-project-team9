''''Starter Main Screen'''
import string
import PySimpleGUI as sg

from question_database_json import QuestionDatabaseJSON
from main_screen_wrapper import get_details, format_answers, create_buttons

database = QuestionDatabaseJSON("data.json")
database.fetch_questions()

question_list = []
for x in database.questions:
    question_list.append(x)

question_list_header = [
                        [sg.Text('Some text')],
                        [sg.InputText(), sg.Button("Search")]
                    ]

question_list_footer = [
                        [sg.Text('_'  * 40)],
                        [sg.Button('Add a question'), sg.Button('Cancel')]
                    ]

question_list_column = question_list_header + create_buttons(question_list,3) + question_list_footer

question_body_column = [
            [sg.Text("Question #", size=(20), font=(40), key = '-TITLE-')],
            [sg.Text("Q: Lorem ipsum dolor sit amet, consectetur adipiscing elit,"\
            " sed do eiusmod tempor et dolore magna aliqua?", size=(30,6), key='-QUESTION-')],
            [sg.Text("A: Lorem ipsum dolor sit amet, consectetur adipiscing elit,"\
            " sed do eiusmod tempor et dolore magna aliqua.", size=(30,6), key='-ANSWER-')]
]

layout = [
    [
        sg.Column(question_list_column),
        sg.VSeparator(),
        sg.Column(question_body_column),
    ]
]

window = sg.Window('Group 9', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if event not in('Search', 'Add a question'):
        details = get_details(question_list, event.rstrip(string.digits))
        window["-TITLE-"].update(details[0])
        window["-QUESTION-"].update(details[0])
        window["-ANSWER-"].update(format_answers(details[1]))

window.close()
