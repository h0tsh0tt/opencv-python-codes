import cv2
import numpy as np 
import sys



# def get_contours(img):
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
#     _, contours, hierarchy = cv2.findContours(thresh, 2, 1)
#     return contours

if __name__ == '__main__':
    
    hand_cascade = cv2.CascadeClassifier("C:/Users/hp pc/Google Drive/opencv-practice/xmls/palm.xml")
    if hand_cascade.empty() :
        print "file cudn't load"
    cap = cv2.VideoCapture(0)
    scaling_factor = 0.5
    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx = 1, fy = 1, interpolation = cv2.INTER_AREA)
        hand_rects = hand_cascade.detectMultiScale(frame, 1.3, 3)
       
        for (x,y,w,h) in hand_rects:                                        # each hand will have only one (x,y,w,h)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # print x, y, w, h
    
        cv2.imshow('window', frame)
        c = cv2.waitKey(1)
        if c == 27:
            break

    cap.release()
    cv2.destroyAllWindows()