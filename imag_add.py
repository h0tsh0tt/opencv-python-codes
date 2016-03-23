import cv2
import numpy as np 

img2 = cv2.imread('C:\Users\hp pc\Google Drive\opencv-practice\python_codes\images\\download.png')
img1 = cv2.imread('C:\Users\hp pc\Google Drive\opencv-practice\python_codes\images\waldo.jpg')

row, col, channel = img2.shape
roi = img1[0:row, 0:col]

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

cv2.imshow("first", img2gray)
cv2.waitKey(0)

ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)

cv2.imshow("second", mask)
cv2.waitKey(0)

mask_inv = cv2.bitwise_not(mask)

cv2.imshow("third", mask_inv)
cv2.waitKey(0)

img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
cv2.imshow("fourth", img1_bg)
cv2.waitKey(0)
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
 
# Put logo in ROI and modify the main image
dst = cv2.add(img2_fg,img1_bg)
img1[0:row, 0:col ] = dst

cv2.imshow("final", img1)
cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()