import cv2
from matplotlib import pyplot as plt

# Grayscale Image
img = cv2.imread("input-gray.jpeg", 0)

plt.title('Histogram of input')
plt.hist(img.ravel(), 256, [0, 256])
plt.savefig('./input-gray-hist.jpeg')
plt.clf()

img = cv2.equalizeHist(img)
cv2.imwrite('./output-gray.jpeg', img)

plt.clf()
plt.title('Histogram after Equalization')
plt.hist(img.ravel(), 256, [0, 256])
plt.savefig('./output-gray-hist.jpeg')
plt.clf()

# Color Image

img = cv2.imread("input-color.jpeg")

img_in_grayscale = img
cv2.cvtColor(img_in_grayscale, cv2.COLOR_BGR2GRAY)
plt.title('Histogram of input')
plt.hist(img_in_grayscale.ravel(), 256, [0, 256])
plt.savefig('./input-color-hist.jpeg')
plt.clf()

R, G, B = cv2.split(img)
R = cv2.equalizeHist(R)
G = cv2.equalizeHist(G)
B = cv2.equalizeHist(B)
equ_img = cv2.merge((R, G, B))
cv2.imwrite('./output-color.jpeg', equ_img)

plt.title('Histogram after Equalization')
plt.hist(equ_img.ravel(), 256, [0, 256])
plt.savefig('./output-color-hist.jpeg')
plt.clf()