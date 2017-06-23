import numpy as np
import cv2
import sobel
import matplotlib.image as mpimg

IMAGE_PATH = './assets/test_images/test3.jpg'
IMG = mpimg.imread(IMAGE_PATH)
HEIGHT, WIDTH, _ = IMG.shape

def binary_image(img=IMG):
    v = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)[:, :, 2]
    filter1 = sobel.binary_sobel(v, 15, 200)

    luv_v = cv2.cvtColor(img, cv2.COLOR_RGB2LUV)[:, :, 2]
    filter2 = sobel.binary(luv_v, 165, 255)

    l = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)[:, :, 1]
    filter3 = (sobel.binary(l, 190, 255))

    combined = np.zeros_like(filter1)
    combined[(filter1 == 1) | (filter2 == 1)| (filter3 == 1)] = 1

    return combined

