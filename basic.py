import os
os.environ["QT_QPA_PLATFORM"] = "xcb"

import cv2 as cv
# Your code goes here...

img = cv.imread('Photos/catsfriend.jpeg')
cv.imshow('Cats', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Edge Cascade
canny = cv.Canny(img, 75, 175)
cv.imshow('Canny Edges', canny)

#Dilate the image
dilate = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilate)

#Eroding
eroded = cv.erode(dilate, (7,7), iterations=1)
cv.imshow('Eroded', eroded)

#Resize
resized = cv.resize(img, (200,200), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#Cropping
cropped = img[100:200, 200:400]
cv.imshow('Cropped', cropped)

cv.imshow()

cv.waitKey(0)