import random
import PySimpleGUI as sg
import layout
import endgame

sg.theme("DarkAmber")

possible = ["BASIC"]
solution = "BASIC"
correct = 0
col = 1
row = 1

window = sg.Window("Wordle", layout.gameWindow, element_justification= 'c')

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event != "-ENTER-" and event != "-BACK-" and event != '-HELP-' and event != '-RESET-':
        if row <= 5:
            window["-"+str(col)+","+str(row)+"-"].update(window[event].get_text())
            row +=1
    
    if event == "-ENTER-":
        # Check to make sure that there are no empty spaces
        filled = True
        for place, letter in enumerate(layout.rows[col-1][0]):
            check = sg.Text.get(window["-"+str(col)+","+str(place+1)+"-"])
            if check == ' ':
                filled = False
        
        correct = 0
        if filled:
            # Make sure that we are within the total guess number
            if col <= 6:
                # Traverse through the current row and column and mark correct colors
                for place, letter in enumerate(layout.rows[col-1][0]):
                    check = sg.Text.get(window["-"+str(col)+","+str(place+1)+"-"])
                    if check == solution[place]:
                        window["-"+str(col)+","+str(place+1)+"-"].update(background_color = 'green')
                        window["-"+check+"-"].update(button_color = 'green')
                        correct += 1
                    elif  check in solution:
                        window["-"+str(col)+","+str(place+1)+"-"].update(background_color = 'blue')
                        window["-"+check+"-"].update(button_color = 'blue')
                    else:
                        window["-"+str(col)+","+str(place+1)+"-"].update(background_color = 'red')
                        window["-"+check+"-"].update(button_color = 'red')
                col += 1
                row = 1
        # If all the letters are correct you win
        if correct == 5:
            endgame.youwin()
        # If you have run out of guesses you lose
        if col>6:
            endgame.youlose()
    # Delete the last entered letter
    if event == "-BACK-":
        if row >= 2:
            window["-"+str(col)+","+str(row-1)+"-"].update(" ")
            row -= 1

    if event == "-HELP-":
        endgame.help()           

window.close()