import cv2
import numpy as np 

img = cv2.imread('C:\Users\hp pc\Google Drive\opencv-practice\python_codes\images\\find.jpg')

img = img[:,:,1]

cv2.imshow('Window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
