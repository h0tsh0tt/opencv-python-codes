import sys
import cv2
import numpy as np 

def get_contours(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    _, contours, hierarchy = cv2.findContours(thresh, 2, 1)
    return contours

if __name__ == '__main__':
    
    img = cv2.imread("C:\Users\hp pc\Google Drive\opencv-practice\python_codes\images\paint.png")
    
     

    for contour in get_contours(img):
        # cv2.imshow("das", contour)
        orig_contour    =   contour                             
        epsilon =   0.01    *   cv2.arcLength(contour,  True)                               
        contour =   cv2.approxPolyDP(contour,   epsilon,    True)
    
        # extract convex hull from the contour
        hull = cv2.convexHull(contour, returnPoints = False)

        # extract defects from above hull 
        defects = cv2.convexityDefects(contour, hull)
        if defects is None:
            continue

        # draw lines and circles to show the defects
        # print defects.shape[0:3]
        for i in  range(defects.shape[0]):
            start_defect, end_defect, far_defect, _ = defects[i, 0]
            start = tuple(contour[start_defect][0])
            end = tuple(contour[end_defect][0])
            far = tuple(contour[far_defect][0])
            cv2.circle(img, far, 5, [128,0,0], -1)                                             
            cv2.drawContours(img, [contour], -1, (0,0,0), 3)
                

    cv2.imshow('Convexity   defects',img)               
    cv2.waitKey(0)              
    cv2.destroyAllWindows() 