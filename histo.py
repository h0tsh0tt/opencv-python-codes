import cv2
import numpy as np 
import sys
import matplotlib.pyplot as plt

if __name__ == '__main__' :

    cap = cv2.VideoCapture(0)
    ret, frame  = cap.read()

    frame = cv2.resize(frame, None, fx = 3, fy = 3, interpolation  = cv2.INTER_AREA)

    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([frame], [None], 0, [360], [0,256])

    # cv2.imshow("window", hist)
    plt.figure()
    plt.title("histogram")
    plt.xlabel("bins")
    plt.ylabel("# of pixels")
    plt.plot(hist)
    plt.xlim([0,256])
    plt.show()
    cv2.waitKey(0) 
    
    cap.release()
    cv2.destroyAllWindows()

