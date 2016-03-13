import cv2
import numpy as np
from matplotlib import pyplot as plt
import Image
import picamera


#Converting to Grayscale
#camera = picamera.PiCamera()
#camera.capture('image1.jpg')
img = cv2.imread('crowd1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_image.png',gray)

#Thresholding
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imwrite('Th_image.png',thresh)

#Watershed Algorithm

# Noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

# Sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)

# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)
cv2.imwrite('SegImg.png',unknown)
HeadCount = cv2.imread('SegImg.png')
#cv2.imshow('Original', img)
#cv2.imshow('Segmented', unknown)
#cv2.waitKey()
im = Image.open('SegImg.png')
width, height = im.size
TotalNumberOfPixels = width * height
#print TotalNumberOfPixels
WhitePixels = cv2.countNonZero(unknown)
#print WhitePixels
inter = float(WhitePixels) / TotalNumberOfPixels
Percentage = inter * 100
#print Percentage
#cv2.imshow('Segmented',unknown)
#cv2.imshow('Original',img)
cv2.waitKey()
cv2.destroyAllWindows()
