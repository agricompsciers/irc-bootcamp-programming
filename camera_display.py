import threading
import cv2
from deepface import DeepFace

capt = cv2.VideoCapture(0, cv2.CAP_DSHOW)

capt.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)
capt.set(cv2.CAP_PROP_FRAME_HEIGHT, 700)

count = 0

face_alexa = False

ref_img = cv2.imread("facetrain.jpg")

def face_detect(frame):
    global face_alexa
    try:
        if DeepFace.verify(frame, ref_img.copy())['verified']:
            face_alexa = True
        else:
            face_alexa = False
    except ValueError:
        face_alexa = False

while True:
    ret, frame = capt.read()

    if ret:
        if count % 20 == 0:
            try:
                threading.Thread(target=face_detect, args=(frame.copy(),)).start()
            except ValueError:
                pass
        count += 1
        if face_alexa:
            cv2.putText(frame, "Filzah Alexandra FOUND", (20, 450), cv2.FONT_ITALIC, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, "Filzah Alexandra NOT FOUND", (20, 450), cv2.FONT_ITALIC, 2, (255, 0, 0), 3)
        
        cv2.imshow("video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
