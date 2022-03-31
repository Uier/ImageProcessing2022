from cmath import cos, sin, sqrt, log
import random
import cv2
import numpy as np
from matplotlib import pyplot as plt

def add_noise(noise_img, sigma):
    for x in range(noise_img.shape[0]):
        for y in range(noise_img.shape[1] - 1):
            # generate random number r, phi
            r, phi = random.uniform(0, 1), random.uniform(0, 1)
            z1 = sigma * cos(2 * np.pi * phi) * sqrt(-2 * log(r))
            z2 = sigma * sin(2 * np.pi * phi) * sqrt(-2 * log(r))
            noise_img[x][y] = max(0, min(255, noise_img[x][y] + z1))
            noise_img[x][y+1] = max(0, min(255, noise_img[x][y+1] + z2))

img = np.full((512, 512), 100, dtype=np.uint8)
cv2.imwrite('./gray.jpeg', img)
plt.hist(img.ravel(), 256, [0, 256])
plt.savefig('./gray-hist.jpeg')
plt.clf()

noise_img = img.copy()
add_noise(noise_img, sigma=10)
cv2.imwrite('./noise-10.jpeg', noise_img)
plt.hist(noise_img.ravel(), 256, [0, 256])
plt.savefig('./noise-10-hist.jpeg')
plt.clf()

noise_img = img.copy()
add_noise(noise_img, sigma=5)
cv2.imwrite('./noise-5.jpeg', noise_img)
plt.hist(noise_img.ravel(), 256, [0, 256])
plt.savefig('./noise-5-hist.jpeg')