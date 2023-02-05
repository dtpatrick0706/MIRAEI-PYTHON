import tensorflow as tf
import cv2
import time
import argparse
import numpy as np
import math
import pandas as pd
import mediapipe as mp

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    cv2.imshow("EXEtest", img)
    cv2.waitKey(1)
