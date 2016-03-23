# import opencv
import cv2
 
# Read image
src = cv2.imread("images/threshold.png", cv2.IMREAD_GRAYSCALE)
 
# Set threshold and maxValue
print src.max()
thresh = 0.1*src.max()
maxValue = 255
 
# Basic threshold example
rand, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY);

cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
print rand