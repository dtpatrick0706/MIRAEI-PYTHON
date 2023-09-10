# import PySimpleGUI as sg
# import random

# paintings = []
# p_size = [3,5,7,9,11,13,15]
# size = random.choice(p_size)

# def make_painting(paintings,size):
#     rowNum = 1
#     for i in range(0,size):
#         count = 1
#         row = []
#         for j in range(0, size):
#             row.append(sg.Text("", background_color= "yellow", size =(4,2), 
#                                justification='c', key="-"+str(rowNum)+"ELE"+str(count)+"-"))
#             count+=1
#         rowNum+=1
#         paintings.append(row)
#     paintings.append([sg.Button("Start", size=(10,2), button_color= 'yellow',key="-START-")])
#     return paintings

import PySimpleGUI as sg
import random

paintings = []
p_size = [3,5,7,9,11,13,15]
size = random.choice(p_size)

def make_painting(paintings, size):
    count = 1
    for i in range(0,size):
        row = []
        for j in range(0, size):
            row.append(sg.Text("", background_color= "yellow", size =(4,2), justification='c', key = '-ELE'+str(count)+'-'))
            count += 1
        paintings.append(row)
    paintings.append([sg.Button('Start', size = (20, 2), button_color = 'yellow', key = '-START-')])
    return paintings