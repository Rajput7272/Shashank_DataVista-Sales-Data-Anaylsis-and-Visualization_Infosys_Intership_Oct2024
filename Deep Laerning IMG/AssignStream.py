import cv2

cap1 = cv2.VideoCapture(0)

cap2 = cv2.VideoCapture("C:\\Users\\91884\\Desktop\\read.py\\opencv\\2711134-uhd_3840_2160_24fps.mp4")
cap3 = cv2.VideoCapture("C:\\Users\\91884\\Desktop\\read.py\\opencv\\3571264-uhd_3840_2160_30fps.mp4")

if not cap1.isOpened():
    print("Error: Could not open the inbuilt webcam.")
    exit()
if not cap2.isOpened():
    print("Error: Could not open video1.")
    exit()
if not cap3.isOpened():
    print("Error: Could not open video2.")
    exit()

while True:
    
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    ret3, frame3 = cap3.read()

    if not ret1 or not ret2 or not ret3:
        print("Error: Failed to capture frame from one or more streams.")
        break
    
    cv2.imshow('Webcam', frame1)
    cv2.imshow('Video 1', frame2)
    cv2.imshow('Video 2', frame3)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap1.release()
cap2.release()
cap3.release()
cv2.destroyAllWindows()
