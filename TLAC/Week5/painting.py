import PySimpleGUI as sg
import random

paintings = []
p_size = [3,5,7,9,11,13,15]

def make_painting(paintings):
    size = random.choice(p_size)
    for i in range(0,size):
        row = []
        for j in range(0, size):
            row.append(sg.Text("", background_color= "yellow", size =(4,2), justification='c'))
        paintings.append(row)
    return paintings