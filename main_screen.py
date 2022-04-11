'''Starter Main Screen'''
import PySimpleGUI as sg
import string

from subprocess import Popen, PIPE
from question_database_json import QuestionDatabaseJSON
from main_screen_wrapper import MainWrapper

wrapper = MainWrapper("data.json")

question_list_header = [
                        [sg.Text('Filter questions')],
                        [sg.InputText(), sg.Button("Search")]
                    ]

question_list_footer = [
                        [sg.Text('_'  * 40)],
                        [sg.Button('Add a question'), sg.Button('Cancel')]
                    ]

question_list_column = question_list_header + wrapper.create_buttons(3) + \
     question_list_footer

question_body_column = [
            [sg.Text("Question #", size=(20), font=(40), key = '-TITLE-')],
            [sg.Text("Q: Lorem ipsum dolor sit amet, consectetur adipiscing elit,"\
            " sed do eiusmod tempor incididunt ut labore et dolore magna aliqua?", size=(30,4), key='-QUESTION-')],
            [sg.Text("A: Lorem ipsum dolor sit amet, consectetur adipiscing elit,"\
            " sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", size=(30,8), key='-ANSWER-')]
]

layout = [
    [
        sg.Column(question_list_column),
        sg.VSeparator(),
        sg.Column(question_body_column),
    ]
]

window = sg.Window('Group 9', layout)
process = -1
open_thread = False

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    elif event == 'Add a question' and open_thread == False:
        process = Popen(['python', 'views//add_question_screen.py'])
        open_thread = True
    elif event not in('Search', 'Add a question'):
        details = wrapper.get_details(event.rstrip(string.digits))
        window["-TITLE-"].update(details[0])
        window["-QUESTION-"].update(details[0])
        window["-ANSWER-"].update(wrapper.format_answers(details[1]))
    if process != -1 and process.poll() is not None:
        open_thread = False

window.close()
