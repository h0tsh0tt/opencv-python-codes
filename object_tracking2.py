import cv2
import numpy as np 

# capture input from webcam
def get_frame(cap, scaling_factor) :
    # capture the frame from video-capture mode
    ret, frame = cap.read()

    # resize the input frame 
    frame = cv2.resize(frame, None, fx = scaling_factor, fy = scaling_factor, interpolation = cv2.INTER_AREA)

    return frame

if __name__ == '__main__' :

    cap = cv2.VideoCapture(0)
    scaling_factor = 0.5

    # iterate until user presses ESC
    while True :
        frame = get_frame(cap, scaling_factor)

        # convert to hsv colorspace
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # define 'blue' range in hsv colorspace
        lower = np.array([0,50, 50])
        upper = np.array([10,255, 255])

        # threshold the HSV image to get only blue color
        mask = cv2.inRange(hsv, lower, upper)

        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame, frame, mask=mask)
        res =   cv2.medianBlur(res, 5)
        cv2.imshow("window", res)
        if cv2.waitKey(1) == 27 :
            break

    cap.release()
    cv2.destroyAllWindows()