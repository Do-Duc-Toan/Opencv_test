import os
os.environ["QT_QPA_PLATFORM"] = "xcb"

import cv2 as cv
import numpy as np

img = cv.imread('Photos/cutecat.jpeg')
# Check image dimensions
height, width = img.shape[:2]
print(f"Image dimensions: {width}x{height}")
cv.imshow('Cat', img)

# Translation
def translate(image, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (image.shape[1], image.shape[0])
    return cv.warpAffine(image, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down    

translated = translate(img, 30, -100)
cv.imshow('Translated', translated)

#Rotation
def rotate(image, angle, rotPoint=None):
    (height, width) = image.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) #1.0 is scale
    dimensions = (width, height)

    return cv.warpAffine(image, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(img, 90)
cv.imshow('Rotated Rotated', rotated_rotated)

#Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC) #INTER_LINEAR is default
cv.imshow('Resized', resized)

#Flipping
flip = cv.flip(img, 1) #0: vertical flip, 1: horizontal flip, -1: both
cv.imshow('Flip', flip)

#Cropping
cropped = img[100:300, 100:300]
cv.imshow('Cropped', cropped)

cv.waitKey(0)