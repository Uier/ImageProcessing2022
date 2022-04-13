import cv2

def otsu(histogram):
    total = sum(histogram)
    probabilities = [(hist/total, i) for i, hist in enumerate(histogram) if hist != 0]
    m = sum(prob * i for prob, i in probabilities)
    m_a = 0.0
    a = 0.0
    mx, threshold = 0.0, -1
    for prob, i in probabilities:
        m_a += i * prob
        a += prob
        if a == 0 or (1 - a) == 0:
            continue
        v = (m_a - m * a) ** 2 / (a * (1 - a))
        if v > mx:
            threshold = i
            mx = v
    return threshold


img = cv2.imread("input.jpeg", 0)
hist = cv2.calcHist([img], [0], None, [256], [0,256])
threshold = otsu(hist)
img[img >= threshold] = 255
img[img < threshold] = 0

cv2.imwrite('./output.jpeg', img)