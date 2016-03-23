import cv2
import numpy as np 

filename = 'images/chessboard.jpg'
img = cv2.imread(filename)
cv2.imshow('img1', img)
dst = cv2.dilate(img, np.ones((11,11)), (-1,-1))

cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
