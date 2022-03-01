import cv2
import numpy as np

image = np.array(cv2.imread("input.jpeg"))

m = [
    [0.114] * 3,
    [0.299] * 3,
    [0.587] * 3,
]
for row in range(image.shape[0]):
    image[row] = np.matmul(image[row], m)

cv2.imwrite('output.jpeg', image)
