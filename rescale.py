import cv2 as cv

#Rescale Function
img = cv.imread('Photos/catsfriend.jpeg')
cv.imshow('Cat', img)   #Show the image

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Image Resized', resized_image)
#cv.waitKey(0)

def changeRes(width, height):
    #Only Live Videos, not for images or videos
    capture.set(3, width)
    capture.set(4, height)

#Rescale Video
capture = cv.VideoCapture('Videos/Dog_and_Cat.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=0.5)

    cv.imshow('Video', frame)   #Show the video
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()