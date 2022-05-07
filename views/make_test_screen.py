'''Window for making tests out of saved questions'''
import PySimpleGUI as sg
from question_database_json import QuestionDatabaseJSON

db = QuestionDatabaseJSON("data.json")

saved_questions = db.questions
saved_question_titles = [x.body for x in saved_questions]
selected_questions = []
selected_questions_titles = [x.body for x in selected_questions]

note = [
    [sg.Text("NOTE: Make new test")],
    [sg.Text(
"""Pick questions that you previously saved to be a part of this new test.
Before adding, you will be able to preview them""",
size=(44, 3))],
]

header_preview = [
        [sg.Text("Question body", font=(40))],
        [sg.Text("Question type")],
        [sg.Text("Question difficulty")]
]

listboxes = [
    sg.Listbox(saved_question_titles,
        size=(50,10),
        enable_events=True,
        key="-SAVEDQUESTIONS-"),
    sg.Listbox(selected_questions_titles,
        size=(50,10),
        enable_events=True,
        key="-SELECTEDQUESTIONS-"),
]

buttons = [
    [
        sg.Button("Generate PDF"),
        sg.Button("Clear selection")
    ]
]

layout = [[
    sg.Column(note),
    sg.VSeparator(),
    sg.Column(header_preview)
    ],
    listboxes,
    buttons
]

window = sg.Window("Make test", layout)

while True:
    event, values = window.read()

    if event in ('Exit', sg.WIN_CLOSED):
        break
