import cv2 as cv
import numpy as np
img = cv.imread('open cv/cars/6.jpg')
cv.imshow('Car',img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

#Create a circular mask
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Mask', mask)
cv.imshow('Masked Image', masked)

cv.waitKey(0)