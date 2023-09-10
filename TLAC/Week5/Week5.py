import PySimpleGUI as sg
import random
from painting import *

sg.theme("DarkAmber")

layout = [
    [sg.Text("")]
]
paintings = make_painting(paintings, size)

window = sg.Window("TLAC Week 5", paintings, element_justification='c')

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-START-":
        inc = 1
        dec = 1
        for x, row in enumerate(paintings):
            if x < size:
                for ele in row:
                    window["-ELE"+str(inc)+"-"].update(background_color='red')
                    window["-ELE"+str(size*dec-x)+"-"].update(background_color='red')
                inc+=size+1
                dec+=1
                


window.close()