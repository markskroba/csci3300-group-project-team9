'''Starter Main Screen'''
import string
from subprocess import Popen

from datetime import datetime
import PySimpleGUI as sg
from main_screen_wrapper import MainWrapper, format_answers
from question_database_json import QuestionDatabaseJSON

wrapper = MainWrapper("data.json")

question_list_header = [
                    [sg.Text('Filter questions')],
                    [sg.InputText(), sg.Button("Search")],
                    [sg.Radio("Any","QTYPE", default=True),sg.Radio("Multiple Choice","QTYPE"), \
                        sg.Radio("Fill In","QTYPE"),sg.Radio("Short Answer","QTYPE")
                    ],
                    [sg.Spin(list(range(0,6)), initial_value=3, k='-DIFFICULTY-'), \
                        sg.CalendarButton("First Used", format="%m/%d/%Y", target="-FIRSTUSED-"),
                        sg.In(size=(10, 1), enable_events=True, key="-FIRSTUSED-"),
                        sg.CalendarButton("Last Used", format="%m/%d/%Y", target="-LASTUSED-"),
                        sg.In(size=(10, 1), enable_events=True, key="-LASTUSED-"),
                    ],
                    [sg.Text('_'  * 40)]
                ]

question_list_footer = [
                        [sg.Text('_'  * 40)],
                        [sg.Button('Add a question'), sg.Button('Cancel')]
                    ]

# question_list_column = question_list_header + wrapper.create_buttons(3) + \
#      question_list_footer
db = QuestionDatabaseJSON("data.json")
question_titles = [q.body for q in db.questions]
question_list_column = question_list_header + [[
    sg.Listbox(question_titles, size=(50,5), enable_events=True, key="-QLIST-")
]] + question_list_footer

mc_frame = [sg.Frame("Properties",
    [
        [
            sg.Text("Answer 1:"),
            sg.In(size=(20, 1), enable_events=True, key="-MCANSWER1-"),
            sg.Checkbox(text="Correct?", key="-MCANSWER1CORRECT-")
        ],
        [
            sg.Text("Answer 2:"),
            sg.In(size=(20, 1), enable_events=True, key="-MCANSWER2-"),
            sg.Checkbox(text="Correct?", key="-MCANSWER2CORRECT-")
        ],
        [
            sg.Text("Answer 3:"),
            sg.In(size=(20, 1), enable_events=True, key="-MCANSWER3-"),
            sg.Checkbox(text="Correct?", key="-MCANSWER3CORRECT-")
        ],
        [
            sg.Text("Answer 4:"),
            sg.In(size=(20, 1), enable_events=True, key="-MCANSWER4-"),
            sg.Checkbox(text="Correct?", key="-MCANSWER4CORRECT-")
        ]
    ],
    key="-MC PROPS-", visible=False)]

fill_in_frame = [sg.Frame("Properties",
    [
        [
            sg.Text("", enable_events=True, key="-FILLINANSWERS-"),
        ]
    ],
    key="-FILL IN PROPS-", visible=False)]

short_answer_frame = [sg.Frame("Properties",
    [
        [
            sg.Text("", enable_events=True, key="-WORDCOUNT-"),
        ],
        [
            sg.Text("", enable_events=True, key="-KEYPOINTS-"),
        ]
    ],
    key="-SHORT ANSWER PROPS-", visible=False)]


question_body_column = [[sg.Text("Question #", size=(20), font=(40), key = '-TITLE-')],
            [sg.Text("", key='-QUESTION-', size=(20,2))],
            [sg.Text("", key="-Q_FIRST_USED-")],
            [sg.Text("", key="-Q_LAST_USED-")],
            [sg.Text("Difficulty:???", size = (10,1), key='-Q_DIFFICULTY-')],
            mc_frame,
            fill_in_frame,
            short_answer_frame]


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
        for i in range(1,5):
            if values[i] is True:
                criteria.append(qtype[i-1])
        if values['-DIFFICULTY-'] != 0:
            criteria.append(values['-DIFFICULTY-'])
        else:
            criteria.append('')
        criteria.append(values['-FIRSTUSED-'])
        criteria.append(values['-LASTUSED-'])

        filtered_buttons,clean_buttons = wrapper.filtered_buttons(criteria)
        for to_be_disabled in filtered_buttons:
            window[to_be_disabled].update(visible = False)
        for to_be_enabled in clean_buttons:
            window[to_be_enabled].update(visible = True)

    elif event == "-QLIST-":
        for q in db.questions:
            if q.body == values["-QLIST-"][0]:
                print(q)

                window["-QUESTION-"].update(q.body)
                window["-Q_DIFFICULTY-"].update(f'Difficulty: {q.difficulty}')
                window["-Q_FIRST_USED-"].update(
                    f'Question first added: {datetime.fromtimestamp(q.first_used).strftime("%b %d, %Y")}')
                window["-Q_LAST_USED-"].update(
                    f'Question first added: {datetime.fromtimestamp(q.last_used).strftime("%b %d, %Y")}')

                # displaying answers
                if q.type == "Short Answer":
                    window["-MC PROPS-"].update(visible=False)
                    window["-FILL IN PROPS-"].update(visible=False)
                    window["-SHORT ANSWER PROPS-"].update(visible=True)

                    window["-WORDCOUNT-"].update(f'Word count: {q.max_word_count}')
                    window["-KEYPOINTS-"].update(f'Key points to address: {", ".join(q.key_points)}')
                elif q.type == "Fill In":
                    window["-MC PROPS-"].update(visible=False)
                    window["-FILL IN PROPS-"].update(visible=True)
                    window["-SHORT ANSWER PROPS-"].update(visible=False)

                    window["-FILLINANSWERS-"].update(f'Answers: {", ".join(q.answers)}')
                elif q.type == "Multiple Choice":
                    window["-MC PROPS-"].update(visible=True)
                    window["-FILL IN PROPS-"].update(visible=False)
                    window["-SHORT ANSWER PROPS-"].update(visible=False)


    elif event not in('Search', 'Add a question', '-LASTUSED-', '-FIRSTUSED-'):
        details = wrapper.get_details(event.rstrip(string.digits))
        window["-TITLE-"].update(details[0])
        window["-QUESTION-"].update(details[0])
        window["-Q_DIFFICULTY-"].update("Difficulty: " + str(details[2]))
    if PROCESS != -1 and PROCESS.poll() is not None:
        OPEN_THREAD = False

window.close()
