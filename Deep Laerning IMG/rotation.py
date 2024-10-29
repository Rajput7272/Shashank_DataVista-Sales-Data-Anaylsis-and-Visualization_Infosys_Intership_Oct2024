import cv2

img = cv2.imread("C:\\Users\\91884\\Desktop\\read.py\\opencv\\images (4).jpeg")
(h, w) = img.shape[:2]
center = (w // 2, h // 2)

angle = 45
scale = 1.0

rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotated_img = cv2.warpAffine(img, rotation_matrix, (w, h))

cv2.imshow('Rotated Image', rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()