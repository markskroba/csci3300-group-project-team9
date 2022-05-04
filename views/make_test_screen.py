'''Window for making tests out of saved questions'''
import PySimpleGUI as sg

layout = [[sg.Text("Window for making new tests")]]
window = sg.Window("Make test", layout)

while True:
    event, values = window.read()

    if event in ('Exit', sg.WIN_CLOSED):
        break
