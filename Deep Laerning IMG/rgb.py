import cv2

img = cv2.imread("C:\\Users\\91884\\Desktop\\read.py\\opencv\\images (1).jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()