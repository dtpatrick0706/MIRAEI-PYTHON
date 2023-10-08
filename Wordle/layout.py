import random
import PySimpleGUI as sg

sg.theme("DarkAmber")

row1 = [[sg.Text(' ', size=(4,2), background_color= 'black', key='-1,1-', justification= 'c'), sg.Text(' ', size=(4,2), background_color= 'black', key='-1,2-', justification= 'c'), sg.Text(' ', size=(4,2), background_color= 'black', key='-1,3-', justification= 'c'), sg.Text(' ', size=(4,2), background_color= 'black', key='-1,4-', justification= 'c'), sg.Text(' ', size=(4,2), background_color= 'black', key='-1,5-', justification= 'c')]]
row2 = [[sg.Text(' ', size=(4,2), background_color= 'black', key='-2,1-', justification= 'c'), sg.Text(' ', size=(4,2), background_color= 'black', key='-2,2-', justification= 'c'), sg.Text(' ', size=(4,2), background_color= 'black', key='-2,3-', justification= 'c'), sg.Text(' ', size=(4,2), background_color= 'black', key='-2,4-', justification= 'c'), sg.Text(' ', size=(4,2), background_color= 'black', key='-2,5-', justification= 'c')]]
row3 = [[sg.Text(' ', size=(4,2), background_color= 'black', key='-3,1-', justification= 'c'), sg.Text(' ', size=(4,2), background_color= 'black', key='-3,2-', justification= 'c'), sg.Text(' ', size=(4,2), background_color= 'black', key='-3,3-', justification= 'c'), sg.Text(' ', size=(4,2), background_color= 'black', key='-3,4-', justification= 'c'), sg.Text(' ', size=(4,2), background_color= 'black', key='-3,5-', justification= 'c')]]
row4 = [[sg.Text(' ', size=(4,2), background_color= 'black', key='-4,1-', justification= 'c'), sg.Text(' ', size=(4,2), background_color= 'black', key='-4,2-', justification= 'c'), sg.Text(' ', size=(4,2), background_color= 'black', key='-4,3-', justification= 'c'), sg.Text(' ', size=(4,2), background_color= 'black', key='-4,4-', justification= 'c'), sg.Text(' ', size=(4,2), background_color= 'black', key='-4,5-', justification= 'c')]]
row5 = [[sg.Text(' ', size=(4,2), background_color= 'black', key='-5,1-', justification= 'c'), sg.Text(' ', size=(4,2), background_color= 'black', key='-5,2-', justification= 'c'), sg.Text(' ', size=(4,2), background_color= 'black', key='-5,3-', justification= 'c'), sg.Text(' ', size=(4,2), background_color= 'black', key='-5,4-', justification= 'c'), sg.Text(' ', size=(4,2), background_color= 'black', key='-5,5-', justification= 'c')]]
row6 = [[sg.Text(' ', size=(4,2), background_color= 'black', key='-6,1-', justification= 'c'), sg.Text(' ', size=(4,2), background_color= 'black', key='-6,2-', justification= 'c'), sg.Text(' ', size=(4,2), background_color= 'black', key='-6,3-', justification= 'c'), sg.Text(' ', size=(4,2), background_color= 'black', key='-6,4-', justification= 'c'), sg.Text(' ', size=(4,2), background_color= 'black', key='-6,5-', justification= 'c')]]

rows = [row1,row2,row3,row4,row5,row6]

keyboard1 = [[sg.Button('Q', size=(3,2),key="-Q-"),sg.Button('W', size=(3,2),key="-W-"), sg.Button('E', size=(3,2),key="-E-"), sg.Button('R', size=(3,2),key="-R-"), sg.Button('T', size=(3,2),key="-T-"),sg.Button('Y', size=(3,2),key="-Y-"),sg.Button('U', size=(3,2),key="-U-"), sg.Button('I', size=(3,2),key="-I-"),sg.Button('O', size=(3,2),key="-O-"),sg.Button('P', size=(3,2),key="-P-")]]
keyboard2 = [[sg.Button('A', size=(3,2),key="-A-"),sg.Button('S', size=(3,2),key="-S-"), sg.Button('D', size=(3,2),key="-D-"), sg.Button('F', size=(3,2),key="-F-"), sg.Button('G', size=(3,2),key="-G-"),sg.Button('H', size=(3,2),key="-H-"),sg.Button('J', size=(3,2),key="-J-"), sg.Button('K', size=(3,2),key="-K-"),sg.Button('L', size=(3,2),key="-L-")]]
keyboard3 = [[sg.Button('BACK', size=(6,2),key="-BACK-"),sg.Button('Z', size=(3,2),key="-Z-"), sg.Button('X', size=(3,2),key="-X-"), sg.Button('C', size=(3,2),key="-C-"), sg.Button('V', size=(3,2),key="-V-"),sg.Button('B', size=(3,2),key="-B-"),sg.Button('N', size=(3,2),key="-N-"), sg.Button('M', size=(3,2),key="-M-"),sg.Button('ENTER', size=(6,2),key="-ENTER-")]]

gameWindow = [
    [sg.Text('WORDLE CLONE', font=60)],
    [sg.Button('?', size=(10,1), key='-HELP-'), sg.Button('Reset', size=(10,1), key='-RESET-')],
    [sg.Column(row1, element_justification= 'c')],
    [sg.Column(row2, element_justification= 'c')],
    [sg.Column(row3, element_justification= 'c')],
    [sg.Column(row4, element_justification= 'c')],
    [sg.Column(row5, element_justification= 'c')],
    [sg.Column(row6, element_justification= 'c')],
    [sg.Column(keyboard1, element_justification= 'c')],
    [sg.Column(keyboard2, element_justification= 'c')],
    [sg.Column(keyboard3, element_justification= 'c')]
]