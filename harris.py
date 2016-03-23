import cv2
import numpy as np 
from pprint import pprint

filename = 'green.png'
img = cv2.imread(filename)
# pprint( img)
print type(img)
print type(img[0])
print type(img[0][0])
print type(img[0][0][0])
print len(img[0][0])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# with open('file','w') as f:
# 	i=0
# 	for x in dst:
# 		# if i==100:
# 		# 	break
# 		f.write(',  '.join(map(str,x)))
# 		f.write('\n')


# # dst = cv2.dilate(dst,None)

# # img = [0,0,255]

# # #show image
# # cv2.imshow('img3', dst)

# # #exit at closing of window
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
