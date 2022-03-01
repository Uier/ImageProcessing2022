import cv2

image = cv2.imread('./input.jpeg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('./output.jpeg', image)
