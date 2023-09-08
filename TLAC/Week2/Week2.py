import PySimpleGUI as sg

sg.theme("DarkAmber")

person1 = ["John", "Green", "Brown", False]
person2 = ["Ava", "Black", "Brown", False]
person3 = ["Gerald", "Blue", "White", True]
person4 = ["Bernice", "Hazel", "Red", True]
person5 = ["Adela", "Green", "Black", False]

resistance = [person1, person2, person3, person4, person5] 

questionImage = "PySimpleGui/TLAC/Week2/question.png"
personImage = "PySimpleGui/TLAC/Week2/person"

col1 = [
    [sg.Text('Information', size=(30,1), justification='center', font=20)],
    [sg.Text("Name", size=(10,1)), sg.Input('', key="-NAME-", size=(30,1))],
    [sg.Text("Eye Color", size =(10,1)), sg.Input('', key="-EYE-", size=(30,1))],
    [sg.Text("Hair Color", size =(10,1)), sg.Input('', key="-HAIR-", size=(30,1))],
    [sg.Text("Glasses", size =(10,1)), sg.Input('', key="-GLASSES-", size=(30,1))],
    [sg.Button("Previous", size=(20,1)),sg.Button("Next", size=(20,1))]
    ]
col2 = [[sg.Image(questionImage, size=(300,300), key="-IMG-")]]

layout = [
[sg.Column(col1),sg.Column(col2)]
]
currentPerson = 0
window = sg.Window("TLAC Week 2", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == "Next":
        currentPerson += 1
        if currentPerson > len(resistance):
            currentPerson = 1
        window["-NAME-"].update(resistance[currentPerson-1][0])
        window["-EYE-"].update(resistance[currentPerson-1][1])
        window["-HAIR-"].update(resistance[currentPerson-1][2])
        window["-GLASSES-"].update(resistance[currentPerson-1][3])
        window["-IMG-"].update(personImage+str(currentPerson)+'.png')
    elif event == "Previous":
        currentPerson -= 1
        if currentPerson < 1:
            currentPerson = len(resistance)
        window["-NAME-"].update(resistance[currentPerson-1][0])
        window["-EYE-"].update(resistance[currentPerson-1][1])
        window["-HAIR-"].update(resistance[currentPerson-1][2])
        window["-GLASSES-"].update(resistance[currentPerson-1][3])
        window["-IMG-"].update(personImage+str(currentPerson)+'.png')

window.close()