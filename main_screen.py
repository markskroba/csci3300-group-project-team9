'''Starter Main Screen'''
import string
from subprocess import Popen

import PySimpleGUI as sg
from main_screen_wrapper import MainWrapper, format_answers

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
            " sed do labore et dolore magna aliqua?", size=(30,4), key='-QUESTION-')],
            [sg.Text("A: Lorem ipsum dolor sit amet, consectetur adipiscing elit,"\
            " sed do labore et dolore magna aliqua.", size=(30,8), key='-ANSWER-')]
]

layout = [
    [
        sg.Column(question_list_column),
        sg.VSeparator(),
        sg.Column(question_body_column),
    ]
]

window = sg.Window('Group 9', layout)
PROCESS = -1
OPEN_THREAD = False

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if event == 'Add a question' and OPEN_THREAD is False:
        # pylint: disable=consider-using-with
        PROCESS = Popen(['python', 'views//add_question_screen.py'])
        OPEN_THREAD = True
    elif event not in('Search', 'Add a question'):
        details = wrapper.get_details(event.rstrip(string.digits))
        window["-TITLE-"].update(details[0])
        window["-QUESTION-"].update(details[0])
        window["-ANSWER-"].update(format_answers(details[1]))
    if PROCESS != -1 and PROCESS.poll() is not None:
        OPEN_THREAD = False

window.close()
