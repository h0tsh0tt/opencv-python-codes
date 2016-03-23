import cv2
import numpy as np

class ObjectTracker(object) :

    # Method to start tracking the object
    def start_tracking(self) :
        # iterate until user presses ESC
        while True :
            # Capture the frame from webcam
            ret, self.frame = self.cap.read()
            # resize the input frame
            self.frame = cv2.resize(self.frame, None, fx = self.scaling_factor, fy = self.scaling_factor, interpolation = cv2.INTER_AREA)
            vis = self.frame.copy()

            # Convert to HSV colorspace
            hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)

            # Create the mask based on predefined threshold
            mask = cv2.inRange(hsv, np.array([0, 60, 32]), np.array([180, 255, 255]))

            if self.selection :
                x0, y0, x1, y1 = self.selection
                self.track_window = (x0, y0, x1-x0, y1-y0)
                hsv_roi = hsv[y0:y1, x0:x1]
                mask_roi = mask[y0:y1, x0:x1]

                # compute the histogram
                hist = cv2.calcHist([hist_roi], [0], mask_roi, [16], [0,180])



if __name__ == '__main__' :
    ObjectTracker().start_tracking()