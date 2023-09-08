import PySimpleGUI as sg
import random
import Complete

sg.theme("DarkAmber")
lock1= random.randint(1,100)
lock2= random.randint(1,100)
lock3 = random.randint(1,100)

lockedImage = 'PySimpleGui/TLAC/Week1/locked.png'
unlockedImage = 'PySimpleGui/TLAC/Week1/unlocked.png'

locks =[lock1, lock2, lock3]

layout =[
    [sg.Text("",size=(15,1)),sg.Input(size=(5,2),key="-RAN1-")],
    [sg.Button("Lock 1", key="-LB1-"),sg.Input(size=(25,2), key="-LOCK1-",background_color="Red", justification='center',text_color="black"),
     sg.Image(lockedImage, size=(100,100), key='-IMAGE1-')], 
    [sg.Text("",size=(15,1)),sg.Input(size=(5,2), key="-RAN2-")],
    [sg.Button("Lock 2", key= "-LB2-"),sg.Input(size=(25,2), key="-LOCK2-", background_color="Red",justification='center',text_color="black"),
     sg.Image(lockedImage, size=(100,100), key="-IMAGE2-")],
    [sg.Text("",size=(15,1)),sg.Input(size=(5,2),key="-RAN3-")],
    [sg.Button("Lock 3", key="-LB3-"),sg.Input(size=(25,2), key="-LOCK3-", background_color= "Red",justification='center',text_color="black"),
     sg.Image(lockedImage, size=(100,100), key="-IMAGE3-")],
    [sg.Button("Start Hacking", size =(20,2)),sg.Button("Stop Hacking", size=(20,2))]
    ]

window = sg.Window("TLAC Week 1", layout)
hacking1 = False
hacking2 = False
hacking3 = False
hacked1 = False
hacked2 = False
hacked3 = False

while True:
    event, values = window.read(timeout=10)

    if event == sg.WIN_CLOSED:
        break

    elif event == "Start Hacking":
        hacking1 = True
        window["-LOCK1-"].update("Locked")
        window["-LOCK1-"].update(background_color = "red")
        window["-IMAGE1-"].update(lockedImage)
        hacking2 = True
        window["-LOCK2-"].update("Locked")
        window["-LOCK2-"].update(background_color = "red")
        window["-IMAGE2-"].update(lockedImage)
        hacking3 = True
        window["-LOCK3-"].update("Locked")
        window["-LOCK3-"].update(background_color = "red")
        window["-IMAGE3-"].update(lockedImage)
        hacked1 = False
        hacked2 = False
        hacked3 = False
        
    elif event == "Stop Hacking":
        hacking1 = False
        hacking2 = False
        hacking3 = False
    
    elif event == "-LB1-":
        if hacking1 == True:
            hacking1 = False
            hacked1 = True
            window["-RAN1-"].update(lock1)
            window["-LOCK1-"].update("Unlocked")
            window["-LOCK1-"].update(background_color='green')
            window["-IMAGE1-"].update(unlockedImage)
            window.refresh()
    elif event == "-LB2-":
        if hacking2 == True:
            hacked2 = True
            hacking2 = False
            window["-RAN2-"].update(lock2)
            window["-LOCK2-"].update("Unlocked")
            window["-LOCK2-"].update(background_color='green')
            window["-IMAGE2-"].update(unlockedImage)
            window.refresh()
    elif event == "-LB3-":
        if hacking3 == True:
            hacked3 = True
            hacking3 = False
            window["-RAN3-"].update(lock3)
            window["-LOCK3-"].update("Unlocked")
            window["-LOCK3-"].update(background_color='green')
            window["-IMAGE3-"].update(unlockedImage)
            window.refresh()

    if hacking1 == True:
        window["-RAN1-"].update(random.randint(1,100))
        window["-LOCK1-"].update("Locked")
    if hacking2 == True:
        window["-RAN2-"].update(random.randint(1,100))
        window["-LOCK2-"].update("Locked")
    if hacking3 == True:
        window["-RAN3-"].update(random.randint(1,100))
        window["-LOCK3-"].update("Locked")

    if hacked1 is True and hacked2 is True and hacked3 is True:
        Complete.hack_complete()

window.close()