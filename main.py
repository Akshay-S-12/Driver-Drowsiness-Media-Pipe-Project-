import cv2
import mediapipe as mp
import pyttsx3
import time
import math

# ---------- TEXT TO SPEECH ----------
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)

last_alert_time = 0
cooldown = 4

# ---------- FACE MESH ----------
mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(refine_landmarks=True)

video = cv2.VideoCapture(0)

def dist(p1, p2):
    return math.hypot(p1[0]-p2[0], p1[1]-p2[1])

while True:
    ret, img = video.read()
    img = cv2.flip(img, 1)
    h, w, _ = img.shape

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(img_rgb)

    status = "Alert"

    if result.multi_face_landmarks:
        face = result.multi_face_landmarks[0]
        lm = {}

        for i, p in enumerate(face.landmark):
            lm[i] = (int(p.x * w), int(p.y * h))

        # ---------- EYE ----------
        eye_open = dist(lm[159], lm[145])

        # ---------- MOUTH ----------
        mouth_w = dist(lm[61], lm[291])
        mouth_h = dist(lm[13], lm[14])

        # ---------- RATIOS ----------
        eye_ratio = eye_open / mouth_w
        mouth_ratio = mouth_h / mouth_w

        # ---------- DROWSINESS LOGIC ----------
        if eye_ratio < 0.08:
            status = "Drowsy - Eyes Closed"
        elif mouth_ratio > 0.30:
            status = "Yawning - Sleepy"
        else:
            status = "Alert"

        # ---------- VOICE ALERT ----------
        now = time.time()
        if status != "Alert" and now - last_alert_time > cooldown:
            engine.say(status)
            engine.runAndWait()
            last_alert_time = now

        # ---------- DRAW LANDMARKS ----------
        # for point in [159, 145, 61, 291, 13, 14]:
        #     cv2.circle(img, lm[point], 2, (0, 255, 0), -1)

    cv2.putText(img, f"Status: {status}", (40, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

    cv2.imshow("Driver Drowsiness Detection", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
