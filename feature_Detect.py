import cv2
import numpy as np                    # highly optimized library for numerical operations with matlab-style syntax 
from matplotlib import pyplot as plt   # python 2d plotting library

img1 = cv2.imread("images/capture1.png", 0)      # load image grayscale (flag = 0)
img2 = cv2.imread("images/capture.png", 0)	  # load image grayscale (flag = 0)

# Initiate ORB detector
orb = cv2.ORB_create()                     # could have also used SIFT or SURF

# find the keypoints and descriptors with ORB_create
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# now here comes the brute force matching part

# first we create brute force matcher object using cv2.BFMatcher()  
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)  # NORM_L2 is actually the eucleidian distance(square-root of sum of squares)
# cross check = true specifies that matcher returns only those matches such that ith descriptor in set A has jth descriptor in set B as best possible match
# One important thing to understand is that after extracting the keypoints,
# you only obtain information about their position, 
# and sometimes their coverage area (usually approximated by a circle or ellipse) in the image. 
# While the information about keypoint position might sometimes be useful, 
# it does not say much about the keypoints themselves.
# Match descriptors which are a way to compare descriptors.
matches = bf.match(des1,des2)

# Sort them in the order of their distance. 
# We sort them in ascending order of their distances so that best matches (with low distance) come to front. 
matches = sorted(matches, key = lambda x:x.distance)
# The value of the key parameter should be a function that takes a single argument and returns a key to use for sorting purposes.
# here lambda is any anonymous function ; x is a parameter ; 

# Draw first 10 matches.
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:100],  None)

plt.imshow(img3),plt.show()
