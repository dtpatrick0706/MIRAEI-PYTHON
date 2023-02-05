import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

imgBackground = cv2.imread("PongBack.png")
imgBall = cv2.imread("PongBall.png", cv2.IMREAD_UNCHANGED)
imgBat1 = cv2.imread("Paddle1.png", cv2.IMREAD_UNCHANGED)
imgBat2 = cv2.imread("Paddle2.png", cv2.IMREAD_UNCHANGED)

detector = HandDetector(detectionCon=0.7, maxHands=2)

ballPos = [100, 100]
speedX = 15
speedY = 15
gameOver = False

while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)

    hands, img = detector.findHands(img, flipType=False)

    img = cv2.addWeighted(img, 0.2, imgBackground, 0.9, 0)

    if hands:
        for hand in hands:
            x, y, w, h = hand['bbox']
            w1, h1, _ = imgBat1.shape
            y1 = y - h1//2
            y1 = np.clip(y1, 20, 430)

            if hand['type'] == "Left":
                img = cvzone.overlayPNG(img, imgBat1, (60, y1))
                if 59 < ballPos[0] < 59 + w1 and y1 < ballPos[1] < y1+h1:
                    speedX = -speedX
                    ballPos[0] += 30

            if hand['type'] == "Right":
                img = cvzone.overlayPNG(img, imgBat2, (1195, y1))
                if 1195 - 50 < ballPos[0] < 1195 - 50 + w1 and y1 < ballPos[1] < y1+h1:
                    speedX = -speedX
                    ballPos[0] -= 30

    # if ballPos[0] < 40 or ballPos > 1200:
    #     gameOver = True

    if ballPos[1] >= 500 or ballPos[1] <= 10:
        speedY = -speedY

    ballPos[0] += speedX
    ballPos[1] += speedY

    img = cvzone.overlayPNG(img, imgBall, ballPos)

    cv2.imshow("Pong", img)
    cv2.waitKey(1)
