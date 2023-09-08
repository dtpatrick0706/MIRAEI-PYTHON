import PySimpleGUI as sg
import random
from bots import *

sg.theme("DarkAmber")

layout = [
    [sg.Column(bot0,element_justification='c',background_color='yellow')],
    [sg.Column(bot1,element_justification='c',background_color='yellow'),
     sg.Column(bot2,element_justification='c',background_color='yellow')],
    [sg.Column(bot3,element_justification='c',background_color='yellow'),
     sg.Column(bot4,element_justification='c',background_color='yellow'),
     sg.Column(bot5,element_justification='c',background_color='yellow')],
    [sg.Button("Find Route Bot", size=(20,1), key="-ROUTE-",button_color="yellow")]
]
window = sg.Window("TLAC Week 3", layout, element_justification='c')

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == "-ROUTE-":
        reset(window)
        choice = random.randint(1,3)
        if choice == 1:
            window["-BOT3S-"].update(background_color = 'green')
            window["-BOT3P-"].update(background_color = 'green')
            window["-BOT1S-"].update(background_color = 'green')
            window["-BOT1P-"].update(background_color = 'green')
            window["-BOT0S-"].update(background_color = 'green')
            window["-BOT0P-"].update(background_color = 'green')
        elif choice == 2:
            window["-BOT4S-"].update(background_color = 'green')
            window["-BOT4P-"].update(background_color = 'green')
            window["-BOT2S-"].update(background_color = 'green')
            window["-BOT2P-"].update(background_color = 'green')
            window["-BOT0S-"].update(background_color = 'green')
            window["-BOT0P-"].update(background_color = 'green')
        elif choice == 3:
            window["-BOT5S-"].update(background_color = 'green')
            window["-BOT5P-"].update(background_color = 'green')
            window["-BOT2S-"].update(background_color = 'green')
            window["-BOT2P-"].update(background_color = 'green')
            window["-BOT0S-"].update(background_color = 'green')
            window["-BOT0P-"].update(background_color = 'green')
            
window.close()