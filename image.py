import cv2 as cv

#Read an image
# img = cv.imread('Photos/cutecat.jpeg')
# cv.imshow('Cute Cat', img)
# cv.waitKey(0) # 0 means wait indefinitely for a key press

#Capture a video
capture = cv.VideoCapture('Videos/Dog_and_Cat.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()





