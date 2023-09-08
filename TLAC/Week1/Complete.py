import PySimpleGUI as sg
import Week1

sg.theme("DarkAmber")

def hack_complete():
    layout2 = [
        [sg.Text("Successfully hacked into the system.")],
        [sg.Button("Again"), sg.Button("Close")]
        ]
    window = sg.Window("Congratulations", layout2)

    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED:
            Week1.hacked1 = False
            Week1.hacked2 = False
            Week1.hacked3 = False
            break

        elif event == "Again":
            Week1.hacked1 = False
            Week1.hacked2 = False
            Week1.hacked3 = False
            break

        elif event == "Close":
            Week1.hacked1 = False
            Week1.hacked2 = False
            Week1.hacked3 = False
            break

    window.close()
