import cv2
import numpy as np

image = np.array(cv2.imread("input.jpeg"))

m = np.ones((3, 3))
for row in range(image.shape[0]):
    image[row] = np.matmul(image[row], m)

cv2.imwrite('output.jpeg', image)
