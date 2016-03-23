import cv2
import numpy as np 

face_cascade = cv2.CascadeClassifier('C:\opencv\sources\data\haarcascades_cuda\haarcascade_frontalface_alt.xml')

face_mask = cv2.imread('C:\Users\hp pc\Google Drive\opencv-practice\python_codes\images\\find.jpg')
h_mask, w_mask = face_mask.shape[:2]

if face_cascade.empty():
    raise IOERROR('Unable to load the face cascade classifier xml file')

cap = cv2.VideoCapture(0)
scaling_factor = 0.5

while true:
    ret, frame = cv2.read()
    frame = cv2.resize(frame, None, fx = 0.5, fy = 0.5, Interpolation =  cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_rects = face_cascade.detectMultiScale(gray, 1.3, 2)

    for (x, y, w, h) in face_rects:
        if h > 0 and w > 0:
            h, w = int(1.4*h), int(1*w) 
            ##

            # extract the region of interest(roi) from the image
            frame_roi  = frame[y:y+h, x:x+w]
            face_mask_small = cv2.resize(face_mask, (w,h), interpolation = cv2.INTER_AREA)

            # convert color image to grayscale and threshold it
            gray_mask = cv2.cvtColor(face_mask_small, cv2.BGRTOGRAY)
            ret, mask = cv2.threshold(gray_mask, 180, 255, cv2.THRESH_BINARY_INV)   # a binary image forms

            # create an inverse mask
            mask_inv = cv2.bitwise_not(mask)                                        # inverts the color


            # use the mask to extract face mask region of interest
             