import PySimpleGUI
import random
import time

art = random.randint(1,100)
train = [48,49,50,51,52]

def move_train(train):
    move = random.randint(0,1)
    if train[2] == 1:
        train = [i+1 for i in train]
    elif  train[2] == 100:
        train = [i-1 for i in train]
    else:
        if move == 0:
            train = [i-1 for i in train]
        elif move == 1:
            train = [i+1 for i in train]
    return train
    