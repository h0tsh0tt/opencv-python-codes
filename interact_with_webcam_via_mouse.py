import cv2
import numpy as np 

def draw_rectangle(event, x, y, flags, params):
    global x_init, y_init, drawing, conv1, conv2
    # print (x,y)
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x_init, y_init = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            conv2 = (min(x_init, x), min(y_init, y))
            conv1 = (max(x_init, x), max(y_init, y))
            img[y_init:y, x_init:x] = 255 - img[y_init:y, x_init:x]

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        conv2 = (min(x_init, x), min(y_init, y))
        conv1 = (max(x_init, x), max(y_init, y))
        img[y_init:y, x_init:x] = 255 - img[y_init:y, x_init:x]

if __name__ == '__main__':
    drawing = False
    conv1, conv2 = (-1, -1), (-1, -1)

    cap = cv2.VideoCapture(0)                                      

        # check if Webcam is open correctly
    if not cap.isOpened():
        raise Exception("Webcam not opened")

    cv2.namedWindow('Webcam')
    cv2.setMouseCallback('Webcam', draw_rectangle)

    while True:
        ret, frame = cap.read()
        img = cv2.resize(frame, None, fx = 1, fy = 1, interpolation = cv2.INTER_AREA)
        cv2.imshow('Webcam', img)
        (x0, y0), (x1, y1) = conv1, conv2
        # print "*"
        # print conv1
        img[y0:y1, x0:x1] = 255 - img[y0:y1, x0:x1]
        c = cv2.waitKey(1)
        if c == 27:
            break

    cap.release()
    cv2.destroyAllWindows()