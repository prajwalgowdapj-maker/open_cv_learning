import cv2 as cv
import numpy as np
img = cv.imread('open cv/cars/6.jpg')
cv.imshow('Car',img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
cv.imshow('Gray', gray)

#Laplacian Gradient
laplacian = cv.Laplacian(gray, cv.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))
cv.imshow('Laplacian', laplacian)

#Sobel Gradient
sobelx = cv.Sobel(gray, cv.CV_64F, 1,0)
sobely = cv.Sobel(gray, cv.CV_64F, 0,1)
sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))

combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel) 
cv.waitKey(0)