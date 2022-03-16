import cv2
import numpy as np

image = np.array(cv2.imread("input.jpeg", cv2.IMREAD_GRAYSCALE))

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
D = d_1
while D.shape[0] < image.shape[0]:
    D = np.vstack((D, D))
while D.shape[1] < image.shape[1]:
    D = np.hstack((D, D))

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        q = image[i][j] / (255 / 3)
        image[i][j] = 255 if image[i][j] > D[i][j] else 0

cv2.imwrite('output-b.jpeg', image)