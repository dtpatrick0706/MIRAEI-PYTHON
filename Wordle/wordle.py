import random
import PySimpleGUI as sg
import layout

sg.theme("DarkAmber")

possible = ["BASIC"]
solution = "BASIC"
col = 1
row = 1

window = sg.Window("Wordle", layout.gameWindow, element_justification= 'c')

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event != "-ENTER-" and event != "-BACK-":
        if row <= 5:
            window["-"+str(col)+","+str(row)+"-"].update(window[event].get_text())
            row +=1
    
    if event == "-ENTER-":
        if col <= 5:
            # Update the column from -1 to be whatever our current column is
            # game over, both win and lose
            # change color scheme
            for place, letter in enumerate(layout.rows[col-1][0]):
                check = sg.Text.get(window["-1,"+str(place+1)+"-"])
                if check == solution[place]:
                    window["-1,"+str(place+1)+"-"].update(background_color = 'green')
                    window["-"+check+"-"].update(button_color = 'green')
                elif  check in solution:
                    window["-1,"+str(place+1)+"-"].update(background_color = 'blue')
                    window["-"+check+"-"].update(button_color = 'blue')
                else:
                    window["-1,"+str(place+1)+"-"].update(background_color = 'white')
                    window["-"+check+"-"].update(button_color = 'white')
            col += 1
            row = 1


    if event == "-BACK-":
        if row >= 2:
            window["-"+str(col)+","+str(row-1)+"-"].update(" ")
            row -= 1
            

window.close()