import cv2
import numpy as np

cap = cv2.VideoCapture('./videos/video.mp4')
#cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    if frame is None:
        break
    cv2.imshow('app', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()