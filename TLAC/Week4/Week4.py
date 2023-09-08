import PySimpleGUI as sg
import random
import time
from train import *

sg.theme("DarkAmber")

layout = [
    [sg.Text("Artifact Location:"),sg.Text("", key='-ART-'), sg.Text("Moves: "),sg.Text("", key ='-COUNT-')],
    [sg.Text("", size=(1,4), background_color="yellow")],
    [sg.Text("", size=(4,2),background_color="gray", key='-CAR1-', justification='c'),
     sg.Text("", size=(4,2),background_color="gray", key='-CAR2-', justification='c'),
     sg.Text("", size=(4,2),background_color="gray", key='-CAR3-', justification='c'),
     sg.Text("", size=(4,2),background_color="gray", key='-CAR4-', justification='c'),
     sg.Text("", size=(4,2),background_color="gray", key='-CAR5-', justification='c')],
    [sg.Button("Start", size=(18,1), key= "-START-")]
]

window = sg.Window("TLAC Week 4", layout,element_justification='c')

solving = False
count = 0

while True:
    event, values = window.read(timeout=1)

    if event == sg.WIN_CLOSED:
        break

    if event == '-START-':
        solving = True
        window["-ART-"].update(art)

    if solving:
        if train[2]== art:
            solving = False
            window["-CAR3-"].update(background_color='red')

        # for x, i in enumerate(train):
        #     if i > 0:
        #         window["-CAR"+str(x+1)+"-"].update(visible = True)
        #     else:
        #         window["-CAR"+str(x+1)+"-"].update(visible = False)

        window["-CAR1-"].update(train[0])
        window["-CAR2-"].update(train[1])
        window["-CAR3-"].update(train[2])
        window["-CAR4-"].update(train[3])
        window["-CAR5-"].update(train[4])
        window["-COUNT-"].update(count)
        train = move_train(train)
        
        count += 1



window.close()