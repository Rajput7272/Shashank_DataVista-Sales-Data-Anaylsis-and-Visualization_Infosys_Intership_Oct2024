import cv2
import numpy as np

cap1 = cv2.VideoCapture("C:\\Users\\91884\\Desktop\\read.py\\opencv\\2711134-uhd_3840_2160_24fps.mp4")
cap2 = cv2.VideoCapture("C:\\Users\\91884\\Desktop\\read.py\\opencv\\3571264-uhd_3840_2160_30fps.mp4")

if not cap1.isOpened() or not cap2.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        break

    frame1 = cv2.resize(frame1, (640, 360))
    frame2 = cv2.resize(frame2, (640, 360))

    h_concat = np.hstack((frame1, frame2))

    cv2.imshow('Concatenated Video', h_concat)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()