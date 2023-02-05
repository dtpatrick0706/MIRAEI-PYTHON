import cv2
import cvzone
from cvzone.PoseModule import PoseDetector
import numpy as np
import mediapipe as mp

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
mpHands = mp.solutions.hands
mpFace = mp.solutions.face_mesh
hands = mpHands.Hands()
pose = mpPose.Pose()
face = mpFace.FaceMesh()
cap = cv2.VideoCapture(0)

cap.set(3, 1920)
cap.set(4, 1080)

while True:
    success, img = cap.read()
    imgDraw = np.zeros_like(img)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    results2 = hands.process(imgRGB)
    results3 = face.process(imgRGB)
    # print(results.pose_landmarks)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(imgDraw, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
    if results2.multi_hand_landmarks:
        for handLms in results2.multi_hand_landmarks:
            mpDraw.draw_landmarks(imgDraw, handLms, mpHands.HAND_CONNECTIONS)
    if results3.multi_face_landmarks:
        for faceLms in results3.multi_face_landmarks:
            mpDraw.draw_landmarks(imgDraw, faceLms, mpFace.FACEMESH_CONTOURS)

    imgStacked = cvzone.stackImages([img, imgDraw], 2, 0.5)
    cv2.imshow('Motion Capture', imgStacked)
    cv2.waitKey(1)
