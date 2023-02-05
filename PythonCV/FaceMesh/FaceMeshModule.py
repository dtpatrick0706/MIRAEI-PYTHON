import cv2
import time
import mediapipe as mp


class FaceMeshDetector():
    def __init__(self, static_mode=False, max_num_faces=1, ref_landmarks=False,
                 det_conf=0.5, track_conf=0.5):
        self.static_image_mode = static_mode,
        self.max_num_faces = max_num_faces,
        self.refine_landmarks = ref_landmarks,
        self.min_detection_confidence = det_conf,
        self.min_tracking_confidence = track_conf,

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(self.static_image_mode, self.max_num_faces,
                                                 self.refine_landmarks, self.min_detection_confidence,
                                                 self.min_tracking_confidence)

        self.drawingSpec = self.mpDraw.DrawingSpec(color=(0, 255, 0),
                                                   thickness=1, circle_radius=1)

    def findFaceMesh(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.faceMesh.process(imgRGB)
        if self.results.multi_face_landmarks:
            for faceLms in results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_CONTOURS,
                                               self.drawingSpec, self.drawingSpec)
            # for lm in faceLms.landmark:
            #     # print(lm)
            #     ih, iw, ic = img.shape
            #     x, y = int(lm.x * iw), int(lm.y * ih)
            #     print(id, x, y)
            return img


def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = FaceMeshDetector()

    while True:
        success, img = cap.read()
        img = detector.findFaceMesh(img)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS:{str(int(fps))}', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                    3, (0, 255, 0), 3)
        cv2.imshow("Face Mesh", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
