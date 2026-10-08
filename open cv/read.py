import cv2 as cv
# Read the image
#img = cv.imread('open cv/cars/2.jpg')
#cv.imshow('Car',img)
#cv.waitKey(0)

#Reading the video
capture = cv.VideoCapture('open cv/Sample_Video/Manipal.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
