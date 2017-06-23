import numpy as np
import cv2
import sobel
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

IMAGE_PATH = './assets/test_images/test3.jpg'
IMG = mpimg.imread(IMAGE_PATH)
HEIGHT, WIDTH, _ = IMG.shape

def binary_image(img=IMG):
    v = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)[:, :, 2]
    filter1 = sobel.binary_sobel(v, 15, 200)

    return filter1


plt.imshow(binary_image(), cmap="gray")
plt.show()
