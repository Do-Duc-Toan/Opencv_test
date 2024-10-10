import os
os.environ["QT_QPA_PLATFORM"] = "xcb"

import cv2 as cv
import numpy as np

img = cv.imread('Photos/dog.jpg')
cv.imshow('Dog', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

cv.imshow()
# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT) # (5,5) is the kernel size
# cv.imshow('Blur', blur)
# canny = cv.Canny(blur, 125, 175) # 125 is the lower threshold and 175 is the upper threshold, this function uses the Canny edge detection algorithm
# cv.imshow('Canny', canny)

ret, thresh = cv.threshold() # 125 is the threshold value, 255 is the max value, cv.THRESH_BINARY is the threshold type

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) #RETR_LIST retrieves all of the contours and doesn't create any parent-child relationship, the CHAIN_APPROX_NONE retrieves all of the points of the contour
print(f'{len(contours)} contour(s) found!')

cv.waitKey(0)

