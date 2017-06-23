'''
**Why camera calibration in self-driving car?**

One of the components that make a self-driving car work is a video camera. A video camera will feed
the machine learning model with real time image frames of the road the self-drivincar is riding on. Images that
better represent the road will have a better chance to make the car drive the safest route possible. In this context
a camera calibration process ensures images are provided with a high level representation accuracy of real-life objects.

The main issue a camera calibration solves is image distortion, which primarely falls in two distorion categories:
radial distortion and tangential distortion.

example radial distortion:

For a self-driving car, image distortion can make a straight line appear to be a curve, or make an object look closer
or futher than it actually is in relation to other objects. These undesireble effects will have a high cost when images are being predicted by the model, which in turn
will make car drive not optimally.

[opencv](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_calib3d/py_calibration/py_calibration.html)
[mathworks](https://www.mathworks.com/help/vision/ug/camera-calibration.html?requestedDomain=www.mathworks.com)

'''

import numpy as np
import cv2
import glob
import pickle

'''
Source code taken from opencv website:
http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_calib3d/py_calibration/py_calibration.html
'''

IMAGES_GLOB = glob.glob('./assets/camera_images/calibration*.jpg')
TEST_IMAGE = cv2.imread('./assets/test_images/test_image.jpg')

WIDTH = 9
HEIGHT = 6
CHANNELS = 3

OBJP = np.zeros((HEIGHT*WIDTH, CHANNELS), np.float32)
OBJP[:,:2] = np.mgrid[0:WIDTH, 0:HEIGHT].T.reshape(-1,2)

objpoints = []
imgpoints = []

for _, fname in enumerate(IMAGES_GLOB):
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (WIDTH, HEIGHT), None)
    if ret:
        objpoints.append(OBJP)
        imgpoints.append(corners)

width, height, _ = TEST_IMAGE.shape
_, mtx, dist, _, _ = cv2.calibrateCamera(objpoints, imgpoints, (width, height), None, None)


dist_pickle = {}
dist_pickle["mtx"] = mtx
dist_pickle["dist"] = dist
pickle.dump(dist_pickle, open("calibration.p", "wb"))

