import cv2
import cvzone
import HandTrackingModule
from HandTrackingModule import handDetector
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import random

cap = cv2.VideoCapture(0)
cap.set(3, 1260)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.7, maxHands=1)


class SnakeGameClass:
    def __init__(self, pathFood):
        self.points = []
        self.lengths = []
        self.currentLength = 0
        self.allowedLength = 150
        self.previousHead = 0, 0

        self.imgFood = cv2.imread(pathFood, cv2.IMREAD_UNCHANGED)
        self.hFood, self.wFood, _ = self.imgFood.shape
        self.foodPoint = 0, 0
        self.randomFoodLocation()
        self.score = 0
        self.gameOver = False

    def randomFoodLocation(self):
        self.foodPoint = random.randint(100, 1000), random.randint(100, 600)

    def update(self, imgMain, currentHead):
        px, py = self.previousHead
        cx, cy = currentHead

        self.points.append([cx, cy])
        distance = math.hypot(cx-px, cy-py)
        self.lengths.append(distance)
        self.currentLength += distance
        self.previousHead = cx, cy

        if self.currentLength > self.allowedLength:
            for i, length in enumerate(self.lengths):
                self.currentLength -= length
                self.lengths.pop(i)
                self.points.pop(i)
                if self.currentLength < self.allowedLength:
                    break

        rx, ry = self.foodPoint
        if rx - self.wFood // 2 < cx < rx + self.wFood // 2 and \
                ry - self.hFood // 2 < cy < ry + self.hFood // 2:
            self.randomFoodLocation()
            self.allowedLength += 50
            self.score += 10
            print(self.score)



        # Draw Snake
        if self.points:
            for i, point in enumerate(self.points):
                if i != 0:
                    cv2.line(imgMain, self.points[i-1], self.points[i], (0, 0, 255), 20)
            cv2.circle(img, self.points[i-1], 10, (200, 0, 200), cv2.FILLED)

        rx, ry = self.foodPoint
        imgMain = cvzone.overlayPNG(imgMain, self.imgFood, (rx - self.wFood // 2,
                                                            ry - self.hFood // 2))

        pts = np.array(self.points[:-2], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(imgMain, [pts], False, (0, 200, 0), 3)
        minDistance = cv2.pointPolygonTest(pts, (cx, cy), True)

        if -1 <= minDistance <= 1:
            print("Hit")
            self.gameOver = True
            self.points = []
            self.lengths = []
            self.currentLength = 0
            self.allowedLength = 150
            self.previousHead = 0, 0
            self.randomFoodLocation()
            self.score = 0

        return imgMain


game = SnakeGameClass("Donut.png")


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    if hands:
        lmList = hands[0]['lmList']
        pointIndex = lmList[8][0:2]
        img = game.update(img, pointIndex)

    cv2.imshow("Snake", img)
    cv2.waitKey(1)
