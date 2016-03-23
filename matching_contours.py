import sys
import cv2
import numpy as np 

# extract reference contour from the image
def get_ref_contour(img):
    ref_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(ref_gray, 127, 255, 0)             # thresholding binary (THRESH_BINARY)

    # find all contours in the threshold image. the values for second and third parameter are restricted to certain possible number
    # of possible values
    contours, hierarchy = cv2.findContours(thresh, 1, 2)

    for contour in contours:
        area = cv2.contourArea(contour)
        img_area = img_shape[0] * img_shape[1]
        if 0.05 < area/float(img_area) < 0.8:
            return contour

# Extract all the contours from the image 
def get_all_contours(img):
    ref_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(ref_gray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    return contours

if __name__ == '__main__':
    # boomerang reference image
    img1 = cv2.imread(sys.argv[1])

    # image containing all shapes
    img2 = cv2.imread(sys.argv[2])

    # Extract the reference contour
    ref_contour = get_ref_contour(img1)

    # Extract all the contours from the input image
    input_contours = get_all_contours(img2)

    closest_contour = input_contours[0]
    min_dist = sys.maxint

    # finding closest contour 
    for contour in  input_contours:
        # Matching shapes and taking the closest one 
        ret = cv2.matchShapes(ref_contour, contour, 1, 0.0)
        if ret < min_dist:
            min_dist = ret 
            closest_contour = contour

    cv2.drawContours(img2, [closest_contour], -1, (0,0,0), 3)
    cv2.imshow('window', img2)
    cv2.waitKey()

