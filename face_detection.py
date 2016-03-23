import cv2
import numpy as np 

face_cascade = cv2.CascadeClassifier('C:\opencv\sources\data\haarcascades_cuda\haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('C:\opencv\sources\data\haarcascades_cuda\haarcascad_eeye.xml')
cap = cv2.VideoCapture(0)
scaling_factor = 0.5

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx = scaling_factor, fy = scaling_factor, interpolation = cv2.INTER_AREA)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # np.copyto(gray, frame)
    face_rects = face_cascade.detectMultiScale(frame, 3.1, 2)           # outputs rectangle co-ordinates, 50 is min_size
    
    for (x,y,w,h) in face_rects:                                        # each face will have only one (x,y,w,h)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        print x, y, w, h
    cv2.imshow('window', frame)
    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
