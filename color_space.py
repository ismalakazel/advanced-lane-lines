import sys
import cv2
import matplotlib.pyplot as plt

IMAGE_PATH = './assets/test_images/test5.jpg'

COLOR_SPACE = {
    "HLS": cv2.COLOR_BGR2HLS,
    "HSV": cv2.COLOR_BGR2HSV,
    "LUV": cv2.COLOR_BGR2LUV,
    "LAB": cv2.COLOR_BGR2LAB,
    "YCRCB": cv2.COLOR_BGR2YCrCb
}

img = cv2.imread(IMAGE_PATH)
color_space = img

color_space = cv2.cvtColor(img, COLOR_SPACE[sys.argv[1]])

one = color_space[:, :, 0]
two = color_space[:, :, 1]
three = color_space[:, :, 2]

f, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(24, 9))
f.tight_layout()
ax1.imshow(img)
ax2.imshow(one, cmap='gray')
ax3.imshow(two, cmap='gray')
ax4.imshow(three, cmap='gray')
plt.show()

