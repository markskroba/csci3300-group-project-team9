'''Views'''
import PySimpleGUI as sg

layout = [[sg.Column([[sg.Text("Hello world")]])]]

window = sg.Window("Hello world", layout)

while True:
    event, values = window.read()
    if event in ('Exit', sg.WIN_CLOSED):
        break
