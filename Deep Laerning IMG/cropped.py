import cv2

img = cv2.imread("C:\\Users\\91884\\Desktop\\read.py\\opencv\\images (4).jpeg")
cropped = img[50:200, 100:300]

cv2.imshow('Cropped Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()