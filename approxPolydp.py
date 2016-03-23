import cv2
import numpy as np 
import sys

def get_contours(img):
    gray = cv2.cvtColor(img, cv2.Color_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, 0)
    _, contours, _ = cv2.findContours(thresh, 2, 1)
    return contours

if __name__ == '__main__':
    img = cv2.imread("")
    contours = get_contours(img)
    
