import PySimpleGUI as sg
import random
from painting import *

sg.theme("DarkAmber")

layout = [
    [sg.Text("")]
]
paintings = make_painting(paintings)

window = sg.Window("TLAC Week 5", paintings)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()