import random
import PySimpleGUI as sg

sg.theme("DarkAmber")

def youlose():
    # game over window
    layout = [[sg.Text('You Lose!')]]

    window = sg.Window("Wordle", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

    window.close()

def youwin():
    # you win window
    layout = [[sg.Text('You Win!')]]

    window = sg.Window("Wordle", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

    window.close()

def help():
    layout = [[sg.Text('You Win!')]]

    window = sg.Window("Wordle", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

    window.close()