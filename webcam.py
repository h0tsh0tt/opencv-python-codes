import cv2

cap = cv2.VideoCapture(2)                               # creating a videocapture object

#check if the webcam is opened correctly
if not cap.isOpened():
    raise   Exception("Cannot open    webcam")          # raise keyword is used which is used to raise your own error


while True:
    ret, frame = cap.read()                             # ret = true if image(frame) read properly else 
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == 27:                            # the function waits for 1 ms until esc(27) is pressed
        break
# when everything done release the capture
cap.release()
cv2.destroyAllWindows()