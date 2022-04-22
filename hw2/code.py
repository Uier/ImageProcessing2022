import cv2
import numpy as np
from matplotlib import pyplot as plt

d_2 = np.array([
    [0, 128, 32, 160],
    [192, 64, 224, 96],
    [48, 176, 16, 144],
    [240, 112, 208, 80],
])
d_1 = np.array([
    [0, 56],
    [84, 28],
])

# (A)

image = np.array(cv2.imread("input.jpeg", cv2.IMREAD_GRAYSCALE))

D = d_2
while D.shape[0] < image.shape[0]:
    D = np.vstack((D, D))
while D.shape[1] < image.shape[1]:
    D = np.hstack((D, D))

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        image[i][j] = 255 if image[i][j] > D[i][j] else 0

cv2.imwrite('output-a.jpeg', image)

# (B)

image = np.array(cv2.imread("input.jpeg", cv2.IMREAD_GRAYSCALE))

D = d_1
while D.shape[0] < image.shape[0]:
    D = np.vstack((D, D))
while D.shape[1] < image.shape[1]:
    D = np.hstack((D, D))

arr = []
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        q = int(image[i][j] / (255 / 3))
        image[i][j] = q + (1 if image[i][j] - 85*q > D[i][j] else 0)
        image[i][j] = image[i][j]/4 * 255

cv2.imwrite('output-b.jpeg', image)