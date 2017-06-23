import numpy as np
import cv2

DEFAULT_IMAGE = cv2.imread('assets/test_images/test5.jpg')
DEFAULT_IMAGE = cv2.cvtColor(DEFAULT_IMAGE, cv2.COLOR_BGR2GRAY)
MIN_TRESH = 30
MAX_TRESH = 150

def sobelx(image):
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    magnitude = np.absolute(sobelx)
    scaled_sobel = np.uint8(255*magnitude/np.max(magnitude))
    return scaled_sobel

def sobely(image):
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    magnitude = np.absolute(sobely)
    scaled_sobel = np.uint8(255*magnitude/np.max(magnitude))
    return scaled_sobel

def sobel(image):
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    magnitude = np.sqrt(sobelx**2 + sobely**2)
    scaled_sobel = np.uint8(255*magnitude/np.max(magnitude))
    return scaled_sobel

def binary_sobel(img, min_thresh, max_thresh):
    sobel_img = sobelx(img)
    binary = np.zeros_like(sobel_img)
    binary[(sobel_img >= min_thresh) & (sobel_img <= max_thresh)] = 1
    return binary

def binary(img, min_thresh, max_thresh):
    binary = np.zeros_like(img)
    binary[(img >= min_thresh) & (img <= max_thresh)] = 1
    return binary

