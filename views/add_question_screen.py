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

inputs = sg.Column([
    get_dates[0],
    get_dates[1],
    get_question_difficulty,
    get_question_body, submit_button], element_justification="center")
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
