import cv2

img = cv2.imread("input.jpeg")

avg_filtered_img = cv2.blur(img, (3, 3))
cv2.imwrite('./output-avg.jpeg', avg_filtered_img)

me_filtered_img = cv2.medianBlur(img, 3)
cv2.imwrite('./output-me.jpeg', me_filtered_img)

low_pass_filtered_img = cv2.GaussianBlur(img, (3, 3), 0)
filtered_scaled_img = low_pass_filtered_img * (k := 0.9)
usm_img = img + (img - filtered_scaled_img)
cv2.imwrite('./output-usm.jpeg', usm_img)
cv2.imwrite('./output-mask.jpeg', img - filtered_scaled_img)