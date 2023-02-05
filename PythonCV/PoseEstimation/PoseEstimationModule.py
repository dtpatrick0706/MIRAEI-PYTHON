import cv2
import mediapipe as mp
import time

class poseDetector():
    def __init__(self, mode= False, complexity= 1, landmarks= True, enable_seg= False,
                 smooth_seg= True, det_conf= 0.5, track_conf= 0.5):
        self.mode = mode
        self.complexity = complexity
        self.landmarks = landmarks
        self.enable_seg = enable_seg
        self.smooth_seg = smooth_seg
        self.det_conf = det_conf
        self.track_conf = track_conf

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.complexity, self.landmarks,
                                     self.enable_seg, self.smooth_seg, self.det_conf,
                                     self.track_conf)
    def findPose(self, img, draw=True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if draw:
            if self.results.pose_landmarks:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                       self.mpPose.POSE_CONNECTIONS)

        return img

    def findPosition(self, img, draw= True):
        lmlist = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append([id,cx,cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return lmlist


def main():
    cap = cv2.VideoCapture("Pose1.mp4")
    pTime = 0
    detector = poseDetector()
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmlist = detector.findPosition(img)
        print(lmlist)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3)
        cv2.imshow("Pose Estimation", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()