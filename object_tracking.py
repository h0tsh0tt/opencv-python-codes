import cv2
import numpy as np 

# Compute the frame difference
def frame_diff(prev_frame, cur_frame, next_frame) :
    # absolute difference between current frame and next frame
    diff_frames1 = cv2.absdiff(next_frame, cur_frame)
    # cv2.imshow("window1", diff_frames1)
    # cv2.waitKey(0)
    # absolute difference between current frame and previous frame
    diff_frames2 = cv2.absdiff(cur_frame, prev_frame)
    # cv2.imshow("window2", diff_frames2)
    # cv2.waitKey(0)
    # return the result of 'bitwise and' between two images
    return cv2.bitwise_and(diff_frames1, diff_frames2) 
   
def get_frame(cap) :
    # capture the frame
    ret, frame = cap.read()

    # resize the image
    frame = cv2.resize(frame, None, fx = scaling_factor, fy = scaling_factor, interpolation = cv2.INTER_AREA)

    # return the gray-scale image
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

if __name__ == '__main__' :
    
    cap = cv2.VideoCapture(0)
    scaling_factor = 1

    prev_frame = get_frame(cap)
    # cv2.imshow("window", prev_frame)
    cur_frame = get_frame(cap)
    # cv2.imshow("window1", cur_frame)
    next_frame = get_frame(cap)
    # cv2.imshow("window2", next_frame)
    
    # iterate until user presses ESC key
    while True :
        # Display result of frame differencing
        cv2.imshow("object movement", frame_diff(prev_frame, cur_frame, next_frame))
        # frame_diff(prev_frame, cur_frame, next_frame)

        # update the variables
        prev_frame = cur_frame
        cur_frame = next_frame
        next_frame = get_frame(cap)

        # check if user pressed ESC
        key = cv2.waitKey(1)
        if key == 27 :
            break

    cap.release()
    cv2.destroyAllWindows()