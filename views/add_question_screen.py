'''Window for adding questions'''
import PySimpleGUI as sg

get_question_body = [
    sg.Text("Question body: "),
    sg.Multiline(size=(50, 10), key="-BODY-"),
]

get_question_difficulty = [
    sg.Text("Question difficulty: "),
    sg.Spin(list(range(1,6)), initial_value=5, k='-DIFFICULTY-'),
]

get_dates = [
    [
        sg.Text("Date when the question was first used (leave empty for today): "),
        sg.CalendarButton("Date", format="%m/%d/%Y", target="-FIRSTUSED-"),
        sg.In(size=(10, 1), enable_events=True, key="-FIRSTUSED-"),
    ],
    [
        sg.Text("Date when the question was last used (leave empty for today): "),
        sg.CalendarButton("Date", format="%m/%d/%Y", target="-LASTUSED-"),
        sg.In(size=(10, 1), enable_events=True, key="-LASTUSED-"),
    ]
]

submit_button = [
    sg.Button(button_text="Submit", enable_events=True, key="-SUBMIT-")]

select_question_type = [
    sg.Text("Question type: "),
    sg.Combo(["Multiple Choice", "Short Answer", "Fill in the Blank"], key="-TYPE-"),
    sg.Button("Select", key="-TYPE SELECT-")
]

mc_frame = [sg.Frame("Properties",
    [[sg.Text("Multiple Choice Properties")]],
    key="-MC PROPS-", visible=False)]

fill_in_frame = [sg.Frame("Properties",
    [
        [
            sg.Text("Enter corresponding answers (as comma-separated list): "),
            sg.In(size=(20, 1), enable_events=True, key=""),
        ]
    ],
    key="-FILL IN PROPS-", visible=False)]

short_answer_frame = [sg.Frame("Properties",
    [
        [
            sg.Text("Enter word count for answers: "),
            sg.In(size=(5, 1), enable_events=True, key=""),
        ],
        [
            sg.Text("Enter points that should be addressed in answers (as comma-separated list): "),
            sg.In(size=(20, 1), enable_events=True, key=""),
        ]
    ],
    key="-SHORT ANSWER PROPS-", visible=False)]

inputs = sg.Column([
    get_dates[0],
    get_dates[1],
    get_question_difficulty,
    get_question_body,
    select_question_type,
    submit_button,
    mc_frame,
    fill_in_frame,
    short_answer_frame], element_justification="center", key="-COLUMN-")

layout = [[inputs]]

window = sg.Window("Add Question", layout)

while True:
    event, values = window.read()

    if event in ('Exit', sg.WIN_CLOSED):
        break
    if event == "-SUBMIT-":
        body = values["-BODY-"]
        difficulty = values["-DIFFICULTY-"]
        first_used = values["-FIRSTUSED-"]
        last_used = values["-LASTUSED-"]

        window["-ANSWERS-"].update(visible=False)

    if event == "-TYPE SELECT-" and values["-TYPE-"] != "":
        print(values["-TYPE-"])

        if values["-TYPE-"] == "Multiple Choice":
            window["-MC PROPS-"].update(visible=True)
            window["-FILL IN PROPS-"].update(visible=False)
            window["-SHORT ANSWER PROPS-"].update(visible=False)

        if values["-TYPE-"] == "Short Answer":
            window["-MC PROPS-"].update(visible=False)
            window["-FILL IN PROPS-"].update(visible=False)
            window["-SHORT ANSWER PROPS-"].update(visible=True)

        if values["-TYPE-"] == "Fill in the Blank":
            window["-MC PROPS-"].update(visible=False)
            window["-FILL IN PROPS-"].update(visible=True)
            window["-SHORT ANSWER PROPS-"].update(visible=False)

    # debug
    if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
        print(event)
