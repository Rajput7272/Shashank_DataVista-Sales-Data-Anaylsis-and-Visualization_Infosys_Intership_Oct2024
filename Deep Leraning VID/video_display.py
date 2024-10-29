import cv2
cap_video1 = cv2.VideoCapture("C:\\Users\\91884\\Desktop\\read.py\\opencv\\2711134-uhd_3840_2160_24fps.mp4")
cap_video2 = cv2.VideoCapture("C:\\Users\\91884\\Desktop\\read.py\\opencv\\3571264-uhd_3840_2160_30fps.mp4")
cap_webcam = cv2.VideoCapture(0)
current_video = cap_video1

while True:
    ret, frame = current_video.read()
    if not ret:
        if current_video == cap_video1:
            current_video = cap_video2
        elif current_video == cap_video2:
            current_video = cap_webcam
        else:
            current_video.set(cv2.CAP_PROP_POS_FRAMES, 0)  
        continue
    cv2.imshow('Media', frame)
    if cv2.waitKey(1) & 0xFF == ord('n'):
        if current_video == cap_video1:
            current_video = cap_video2
        elif current_video == cap_video2:
            current_video = cap_webcam
        else:
            current_video = cap_video1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap_video1.release()
cap_video2.release()
cap_webcam.release()
cv2.destroyAllWindows()