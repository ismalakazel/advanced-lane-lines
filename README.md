# Advanced Lane Finding 

*Self-driving Car Nanodegree at Udacity.*

------------

### Camera calibration

The code for calibrating the camera can be found in `scripts/calibration.py`. 

In summary, I first downloaded and stored checkboard images in `scripts/assets/camera_images/` with each image name followed by a number (such as `calibration01.jpg`) starting from 01 to the total number of images. Then I used the glob module to read all images, loop through them and calculate the image points from each image  with `cv2.findChessboardCorners`. I then store the images points in an array with a matchin object points array. Finally, I calibrated the camera with a test image and stored the camera matrix (mtx) and distortion coefficients (dist) in a pickle file located at `./calibration.p`.

Here is an example of a distorted image which was undistorted using `cv2.undistort`:

![checkboard undistorted](https://github.com/ismalakazel/advanced-lane-lines/blob/master/assets/final_images/checkboard_undistorted.png)

Applying the same undistort function in a road image resulted in the following:

![road undistorted](https://github.com/ismalakazel/advanced-lane-lines/blob/master/assets/final_images/road_undistorted.png)

### Color and gradient thresholding

Before creating a binary image I analyzed a test image using different color spaces using the `cv2.cvtColor` function to convert the color space of an image. For experiementing with different color spaces I create a file located at `./scripts/color_space.py`. To check the image in a different color space. run the script passing one of the available color space options in COLOR_SPACE. eg:

`python color_space.py "HSV"`

Bellow is an example of an image, in HSV color space:

![HSL color space](https://github.com/ismalakazel/advanced-lane-lines/blob/master/assets/final_images/hsl_color_space.png)

After experimenting with different color spaces I proceeded to create a binary image that could expose lane lines from images independently from color and light conditions. First, I converted a test image to HLS color space, then a sobel operation, in the x direction, was applied to the S channel in order to properly identify lane lines. Here is an example of this step:

![sobel x](https://github.com/ismalakazel/advanced-lane-lines/blob/master/assets/final_images/sobelx.png)

The result was satisfatory, though it could be improved. After experimenting combinations of multiple binary images with different color spaces I finally settled with a combo of three images. The first image, as explained above, exposed the lanes lines overal, the second image exposes the left lane line and the third image exposes the right lane line. Here's the result:

![binary combined](https://github.com/ismalakazel/advanced-lane-lines/blob/master/assets/final_images/binary.png)

The relevant code for creating the binary images can be found in `sobel.py`. Here's an example on how I converted and created a sobel binary image:

```python
v = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)[:, :, 2]                            
filter1 = sobel.binary_sobel(v, 15, 200)  
```

### Perspective transform

To change the perspective of an image I used `cv2.getPerspectiveTransform` which takes 4 points (x, y) defining a region of interest in the image, and 4 points to where this region of interest should be scaled. Here is how I created the points arrays:

```python

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
```
full code can be found at `scripts/perspective.py`.

Result of a perspective transform on a road image:

![perspective](https://github.com/ismalakazel/advanced-lane-lines/blob/master/assets/final_images/perspective.png)

### Finding lane lines

To find the lane lines in the warped_binary image, resulted from pipeline described above, I took a histogram of it on the x axis. The peaks of the histogram were the indicators of the left and right lanes. 

With the peaks being found I proceeded with the sliding windown algorithm to track the center of the line from the base to the top of the image. Then, a second order polynomial was applied to fit the left and right lanes. The result can be seen bellow:

![polynomial](https://github.com/ismalakazel/advanced-lane-lines/blob/master/assets/final_images/polynomial.png)

The code for finding lane lines is located at cell 7 of the Solution.ipynb notebook

### Lane curvature

To calculate the radius of the curvature of the lane I used a constant of 30 meters for lane lengh and another contanst of 3.7 for lane width. The camera as assumed to be in the center. Then I used the following equation: Curve = (1 + (2Ay + B)^2)^3/2) / |2A|

The implementation of lane curvature can be found in the Solution.ipynb notebook cell 8.

### Pipeline result:

Putting all the pieces described above together resulted in the following image:

![result](https://github.com/ismalakazel/advanced-lane-lines/blob/master/assets/final_images/result.png)

### Issues:

After testing the pipeline on the challenge videos it was noted that different lighting condition pose a problem to identifying lanes properly. Also, the current pipeline may mistakenly identify shadows or other continious lines on the road as lanes. More testing needs to be done in the color spacing field.

I would also like to experiment more with lane curvature and come up with a better wrapper class to make a cohesive pipeline for finding lanes.

