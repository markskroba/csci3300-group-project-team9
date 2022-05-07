'''Window for making tests out of saved questions'''
import PySimpleGUI as sg
from question_database_json import QuestionDatabaseJSON

db = QuestionDatabaseJSON("data.json")

saved_questions = db.questions
saved_question_titles = [x.body for x in saved_questions]
selected_questions = []
selected_questions_titles = [x.body for x in selected_questions]

note = [
    [sg.Text("Make new test", font=(40))],
    [sg.Text(
"""Click on questions from the left list to add them to this test
Click on question from the right list to remove them from this test""",
size=(44, 3))],
]

preview_body = sg.Text("", font=(40))
preview_type = sg.Text("")
preview_difficulty = sg.Text("")

header_preview = [
        [preview_body],
        [preview_type],
        [preview_difficulty]
]

saved_questions_listbox = sg.Listbox(saved_question_titles,
        size=(50,10),
        enable_events=True,
        key="-SAVEDQUESTIONS-")

selected_questions_listbox = sg.Listbox(selected_questions_titles,
        size=(50,10),
        enable_events=True,
        key="-SELECTEDQUESTIONS-")

listboxes = [saved_questions_listbox] + [selected_questions_listbox]


buttons = [
    [
        sg.Button("Generate PDF", enable_events=True, key="-GENERATEPDF-"),
        sg.Button("Clear selection", enable_events=True, key="-CLEARSELECTION-")
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

    if event == "-SAVEDQUESTIONS-":
        i = saved_questions_listbox.get_indexes()[0]
        selected_questions.append(saved_questions[i])

        # preview
        preview_body.update(value=f'Q: {saved_questions[i].body}')
        preview_type.update(value=f'Type: {saved_questions[i].type}')
        preview_difficulty.update(value=f'Difficulty: {saved_questions[i].difficulty}')

        selected_questions_titles = [x.body for x in selected_questions]
        selected_questions_listbox.update(values=selected_questions_titles)

    elif event == "-SELECTEDQUESTIONS-":
        selected_items = selected_questions_listbox.get_indexes()
        if len(selected_items) == 0:
            continue
        i = selected_items[0]
        selected_questions.pop(i)

        selected_questions_titles = [x.body for x in selected_questions]
        selected_questions_listbox.update(values=selected_questions_titles)

    elif event == "-CLEARSELECTION-":
        selected_questions = []
        selected_questions_titles = [x.body for x in selected_questions]
        selected_questions_listbox.update(values=selected_questions_titles)

    elif event == "-GENERATEPDF-":
        print(selected_questions)
        print(len(selected_questions))
