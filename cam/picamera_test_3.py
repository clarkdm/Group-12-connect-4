# cspace.py
import cv2
import numpy as np
import pylab
import picamera
import mahotas as mh



img_rgb = cv2.imread('image.png')
# Convert BGR to HSV
#img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
hsv = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2HSV)

cv2.imwrite('hsv1.png',hsv)

#lower_red_bgr= np.array([150,50,50 ])
#lower_red_hsv = cv2.cvtColor(lower_red_bgr,cv2.COLOR_RGB2HSV )

#upper_red_bgr= np.array([255,0,0 ])
#upper_red_hsv = cv2.cvtColor(upper_red_bgr,cv2.COLOR_RGB2HSV )

# define range of blue color in HSV
lower_red_hsv = np.array([110,50,50])
upper_red_hsv = np.array([140,255,255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_red_hsv, upper_red_hsv)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(img_rgb,img_rgb, mask= mask)



gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)


# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)

# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)


cv2.imwrite('unknown.png',unknown)
cv2.imwrite('dist_transform.png',dist_transform)
cv2.imwrite('res.png',res)



pylab.imshow(unknown)
pylab.gray()
pylab.show()










