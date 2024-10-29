import cv2

# Read an image
image = cv2.imread("C:\\Users\\91884\\Desktop\\read.py\\opencv\\images (3).jpeg")
image1 = cv2.imread("C:\\Users\\91884\\Desktop\\read.py\\opencv\\images (1).jpeg")

# Display the image using OpenCV
cv2.imshow('Image', image)
cv2.imshow('Image', image1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# To check dimensions of the image
print(image.shape)