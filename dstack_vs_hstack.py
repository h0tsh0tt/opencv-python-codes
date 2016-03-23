import cv2
import numpy as np 

if __name__ == '__main__' :
    
    img1 = cv2.imread("C:\Users\hp pc\Google Drive\opencv-practice\python_codes\images\waldo.jpg")
    # img2 = cv2.imread("C:\Users\hp pc\Google Drive\opencv-practice\python_codes\images\capture.png")
    img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    print img2.size, img1.size
    # img3 = np.hstack((img2, img1))
    # cv2.imshow("window1", img3)
    # cv2.imshow("window2", img2)
    # img4 = np.hstack((img1, img2))
    # cv2.imshow("window2", img4)

    cv2.waitKey(0)

    cv2.destroyAllWindows()
