'''Window for making tests out of saved questions'''
import PySimpleGUI as sg

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
    sg.Listbox(["test1", "test2"], size=(50,10), enable_events=True, key="-SAVEDQUESTIONS-"),
    sg.Listbox(["test1", "test2"], size=(50,10), enable_events=True, key="-SELECTEDQUESTIONS-"),
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
