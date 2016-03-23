import sys

import cv2
import numpy as np 

def draw_matches(img1, key1, img2, key2, matches):
    row1, col1 = img1.shape[:2]
    row2, col2 = img2.shape[:2]

    # create a new output image that concatinates the two images together 
    output_img = np.zeros((max))
if __name__ == '__main__':

    img1 = cv2.imread(sys.argv[1], 0)
    img2 = cv2.imread(sys.argv[2], 0)

    # initialize ORB detector
    orb = cv2.ORB()

    # Extract, Keypoints and descriptors
    key1, desc1 = orb.detectAndCompute(img1, None)
    key2, desc2 = orb.detectAndCompute(img2, None)

    # Create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

    # Match descriptors
    matches = bf.match(desc1, desc2)

    # Sort them in order of their distance
    matches = sorted(matches, key = lamda x:x.distance)

    # draw first 'n' matches
    img3 = draw_matches(img1, key1, img2, key2, matches[:30])

    cv2.imshow('Matched keypoints', img3)
    cv2.waitKey() 