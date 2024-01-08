import cv2
import numpy as np
img = cv2.imread('abc.jpg')
cv2.imshow('original',img)


gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


img2 = np.zeros_like(img)
img2[:,:,0] = gray_image
img2[:,:,1] = gray_image
img2[:,:,2] = gray_image

cv2.imshow('grayimg',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

