'''Starter Main Screen'''
import PySimpleGUI as sg

question_list_column = [
            [sg.Text('Some text')],
            [sg.InputText(), sg.Button("Search")],
            [sg.Button("Question 1"),sg.Button("Question 2"),sg.Button("Question 3")],
            [sg.Button("Question 4"),sg.Button("Question 5"),sg.Button("Question 6")],
            [sg.Text('_'  * 40)],
            [sg.Button('Add a question'), sg.Button('Cancel')]
]

question_body_column = [
            [sg.Text("Question #", size=(20), font=(40), key = '-TITLE-')],
            [sg.Text("Q: Lorem ipsum dolor sit amet, consectetur adipiscing elit,"\
            " sed do eiusmod tempor incididunt ut labore et dolore magna aliqua?", size=(30,6))],
            [sg.Text("A: Lorem ipsum dolor sit amet, consectetur adipiscing elit,"\
            " sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", size=(30,6))]
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
        window["-TITLE-"].update(event)

window.close()
