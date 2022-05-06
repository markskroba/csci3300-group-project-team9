'''Starter Main Screen'''
import string
from subprocess import Popen

import PySimpleGUI as sg
from main_screen_wrapper import MainWrapper

wrapper = MainWrapper("data.json")

question_list_header = [
                    [sg.Text('Filter questions')],
                    [sg.InputText(key='-SEARCHTEXT-'), sg.Button("Search")],
                    [sg.Radio("Any","QTYPE", default=True),sg.Radio("Multiple Choice","QTYPE"), \
                        sg.Radio("Fill In","QTYPE"),sg.Radio("Short Answer","QTYPE")
                    ],
                    [sg.Spin(list(range(0,6)), initial_value=0, k='-DIFFICULTY-'), \
                        sg.CalendarButton("First Used Before", format="%m/%d/%Y", target="-FIRSTUSED-"),
                        sg.In(size=(10, 1), enable_events=True, key="-FIRSTUSED-"),
                        sg.CalendarButton("Last Used Before", format="%m/%d/%Y", target="-LASTUSED-"),
                        sg.In(size=(10, 1), enable_events=True, key="-LASTUSED-"),
                    ],
                    [sg.Text('_'  * 40)]
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
            " sed do labore et dolore magna aliqua.", size=(30,8), key='-ANSWER-')],
            [sg.Text("Difficulty:???", size = (10,1), key='-Q_DIFFICULTY-')]
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

    elif event == 'Search':
        criteria = []
        qtype = ['General', 'Multiple Choice', 'Fill In', 'Short Answer']
        for i in range(0,4):
            if values[i] is True:
                criteria.append(qtype[i])
        if values['-DIFFICULTY-'] != 0:
            criteria.append(values['-DIFFICULTY-'])
        else:
            criteria.append('')
        criteria.append(values['-FIRSTUSED-'])
        criteria.append(values['-LASTUSED-'])
        criteria.append(values['-SEARCHTEXT-'])

        filtered_buttons,clean_buttons = wrapper.filtered_buttons(criteria)
        for to_be_disabled in filtered_buttons:
            window[to_be_disabled].update(visible = False)
        for to_be_enabled in clean_buttons:
            window[to_be_enabled].update(visible = True)

    elif event not in('Search', 'Add a question', '-LASTUSED-', '-FIRSTUSED-'):
        details = wrapper.get_details(event.rstrip(string.digits))
        window["-TITLE-"].update(details[0])
        window["-QUESTION-"].update(details[0])
        window["-ANSWER-"].update(details[1])
        window["-Q_DIFFICULTY-"].update("Difficulty: " + str(details[2]))
    if PROCESS != -1 and PROCESS.poll() is not None:
        OPEN_THREAD = False

window.close()
