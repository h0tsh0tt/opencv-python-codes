import cv2
import numpy as np 
import sys

def draw_matches(img1, key1, img2, key2, matches):                
    rows1, cols1 = img1.shape[:2]
    rows2, cols2 = img2.shape[:2]

    output_image = np.zeros((max(rows1,rows2), cols1+cols2, 3,), dtype = 'uint8')
    output_image[:rows1, :cols1, :] = np.dstack([img1, img1, img1])
    output_image[:rows2, cols1:cols1+cols2, :] = np.dstack([img2, img2, img2])

    # Draw connecting lines between matching keypoints
    for match in matches:                                           # matches is vector<DMatch> , each element has queryIdx and trainIdx
        # Get the matching keypoint for each of the images
        img1_idx = match.queryIdx                                   # indexes into keypoint1
        img2_idx = match.trainIdx                                   # indexes into keypoint2
        
        (x1, y1) = keypoints[img1_idx].pt
        (x2, y2) = keypoints[img2_idx].pt

        # draw a small circle at both co-ordinates and then draw a line
        cv2.circle(output_image, (int(x1), int(y1)), 4, (0,255,0), 1)


        # ***********chapter 6 opencv with examples************

