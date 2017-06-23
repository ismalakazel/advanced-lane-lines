# Advanced Lane Finding 

*Self-driving Car Nanodegree at Udacity.*

------------

### Camera calibration

One of the components that make a self-driving car work is a video camera. A video camera will feed
the machine learning model with real time image frames of the road the self-drivincar is riding on. Images that better represent the road will have a better chance to make the car drive the safest route possible. In this context a camera calibration process ensures images are provided with a high level representation accuracy of real-life objects.

The code for calibrating the camera can be found in `scripts/calibration.py`. In summary, I first downloaded and stored checkboard images in `scripts/assets/camera_images/` with each image name followd by a number (such as `calibration01.jpg`) starting from 01 to the total number of images. Then I used the glob module to read all images, loop through them and calculate the image points from each image  with `cv2.findChessboardCorners`. I then store the images points in an array with a matchin object points array. Finally, I calibrated the camera with a test image and stored the camera matrix (mtx) and distortion coefficients (dist) in a pickle file located at `./calibration.p`.

Here is an example of a distorted image which was undistorted using `cv2.undistort`:

[checkboard undistorted](./assets/final_images/checkboard_undistorted.png)

Applying the same undistort function in a road image resulted in the following:

[road undistorted](./assets/final_images/road_undistorted.png)

### Color and gradient thresholding

Before creating a binary image I analyzed a test image using different color spaces using the `cv2.cvtColor` function to convert the color space of an image. For experiementing with different color spaces I create a file located at `./scripts/color_space.py`. To check the image in a different color space. run the script passing one of the available color space options in COLOR_SPACE. eg:

`python color_space.py "HSV"`

It's interesting how you get, or lose depeding on the context, more information from an image just by analyzing it in a different color space. Furthermore, when spliting the color space by it's channels even more information can be captured. Bellow is an example of an image, in HSV color space:

[HSL color space](./assets/final_images/hsl_color_space.png)

After experimenting with different color spaces I proceeded to create a binary image that could expose lane lines from images independently from color and light conditions. First, I converted a test image to HSV color space, then a sobel operation, in the x direction, was applied to the V channel in order to properly identify lane lines. Here is an example of this step:

[sobel x](./assets/final_images/sobel_x.png)

The result was satisfatory, though it could be improved. After experimenting combinations of multiple binary images with different color spaces I finally settled with a combo of three images. The first image, as explained above, exposed the lanes lines overal, the second image exposes the left lane line and the third image exposes the right lane line. Here's the result:

[binary combined](./assets/final_images/binary_combined.png)

The relevant code for creating the binary images can be found in `sobel.py`. Here's an example on how I converted and created a sobel binary image:

```python
v = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)[:, :, 2]                            
filter1 = sobel.binary_sobel(v, 15, 200)  
```

### Perspective transform

To change the perspective of an image I used `cv2.getPerspectiveTransform` which takes 4 points (x, y) defining a region of interest in the image, and 4 points to where this region of interest should be scaled. Here is how I created the points arrays:

```python

offset = 100

pts1 = np.float32([
    [width/2 - offset, height/2 + offset],
    [width/2 + offset, height/2 + offset],
    [width/2 - (offset * 5), height - offset],
    [width/2 + (offset * 5), height - offset]
])
pts2 = np.float32([
    [width/2 - (offset * 5), 10],
    [width/2 + (offset * 5), 10],
    [width/2 - (offset * 5), height-10],
    [width/2 + (offset * 5), height-10]
])
```
full code can be found at `scripts/perspective.py`.


