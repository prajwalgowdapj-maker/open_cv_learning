import cv2 as cv

img = cv.imread('open cv/cars/1.jpg')
cv.imshow('Car',img)
#convert to grayscale
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Blur
blur= cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#Edge Cascade
canny=cv.Canny(blur,125,175)
cv.imshow('Canny',canny)

#Dilating the image
dilated=cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dilated',dilated)

#Eroding the image
eroded=cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded',eroded)

#resizing
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#cropping
cropped=img[50:200,200:400]
cv.imshow('Cropped',cropped)
cv.waitKey(0)
