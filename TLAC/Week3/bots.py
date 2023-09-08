import PySimpleGUI as sg

sg.theme("DarkAmber")

# Bot serial and Parent
bot0p = [sg.Text("0",background_color='red',size=(5,1), justification='c',key="-BOT0P-")]
bot0s = [sg.Text("45",size=(5,1), justification='c',key="-BOT0S-")]
bot1p = [sg.Text("45",background_color='red',size=(5,1), justification='c',key="-BOT1P-")]
bot1s = [sg.Text("17",size=(5,1), justification='c',key="-BOT1S-")]
bot2p = [sg.Text("45",background_color='red',size=(5,1), justification='c',key="-BOT2P-")]
bot2s = [sg.Text("26",size=(5,1), justification='c',key="-BOT2S-")]
bot3p = [sg.Text("17",background_color='red',size=(5,1), justification='c',key="-BOT3P-")]
bot3s = [sg.Text("6",size=(5,1), justification='c',key="-BOT3S-")]
bot4p = [sg.Text("26",background_color='red',size=(5,1), justification='c',key="-BOT4P-")]
bot4s = [sg.Text("99",size=(5,1), justification='c',key="-BOT4S-")]
bot5p = [sg.Text("26",background_color='red',size=(5,1), justification='c',key="-BOT5P-")]
bot5s = [sg.Text("31",size=(5,1), justification='c',key="-BOT5S-")]

# Bots 
bot0 = [bot0p,bot0s]
bot1 = [bot1p,bot1s]
bot2 = [bot2p,bot2s]
bot3 = [bot3p,bot3s]
bot4 = [bot4p,bot4s]
bot5 = [bot5p,bot5s]

# Big Bots List
bigBots = [bot0,bot1,bot2,bot3,bot4,bot5]

def reset(window):
    window["-BOT0S-"].update(background_color = 'black')
    window["-BOT0P-"].update(background_color = 'red')
    window["-BOT1S-"].update(background_color = 'black')
    window["-BOT1P-"].update(background_color = 'red')
    window["-BOT2S-"].update(background_color = 'black')
    window["-BOT2P-"].update(background_color = 'red')
    window["-BOT3S-"].update(background_color = 'black')
    window["-BOT3P-"].update(background_color = 'red')
    window["-BOT4S-"].update(background_color = 'black')
    window["-BOT4P-"].update(background_color = 'red')
    window["-BOT5S-"].update(background_color = 'black')
    window["-BOT5P-"].update(background_color = 'red')
