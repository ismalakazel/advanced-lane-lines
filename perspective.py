import cv2
import numpy as np

IMAGE_PATH = './assets/test_images/test5.jpg'
IMG  = cv2.imread(IMAGE_PATH)

def points(img):
    height, width, _ = img.shape

    pts1 = np.float32([
        [width/2 - 100, height/2 + 100],
        [width/2 + 100, height/2 + 100],
        [width/2 - (100 * 5), height - 50],
        [width/2 + (100 * 5), height - 50]
    ])
    pts2 = np.float32([
        [width/2 - (100 * 5), 10],
        [width/2 + (100 * 5), 10],
        [width/2 - (100 * 5), height-10],
        [width/2 + (100 * 5), height-10]
    ])
    return pts1, pts2

def perspective(img, src, dest):
    height = img.shape[0]
    width = img.shape[1]
    M = cv2.getPerspectiveTransform(src, dest)
    dst = cv2.warpPerspective(img, M, (width, height))
    return dst

