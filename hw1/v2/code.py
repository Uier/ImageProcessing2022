import cv2
import numpy as np

image = np.array(cv2.imread("input.jpeg"))

# for row in range(image.shape[0]):
#     for col in range(image.shape[1]):
#         gray_value = sum(image[row][col]) / 3
#         image[row][col] = [gray_value] * 3

m = [[1/3] * 3] * 3
for row in range(image.shape[0]):
    image[row] = np.matmul(image[row], m)

cv2.imwrite('output.jpeg', image)
