import cv2 as cv
import numpy as np
img = cv.imread('open cv/cars/6.jpg')
cv.imshow('Car',img)

#Average Blur
avg_blur = cv.blur(img, (5, 5))
cv.imshow('Average Blur', avg_blur)

#Gaussian Blur
gaussian_blur = cv.GaussianBlur(img, (5, 5), 0)
cv.imshow('Gaussian Blur', gaussian_blur)

#Median Blur
median_blur = cv.medianBlur(img, 5)
cv.imshow('Median Blur', median_blur)

#Bilateral Blur
bilateral_blur = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral Blur', bilateral_blur)
cv.waitKey(0)