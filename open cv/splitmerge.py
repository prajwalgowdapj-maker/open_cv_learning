import cv2 as cv
import numpy as np
img = cv.imread('open cv/cars/6.jpg')
cv.imshow('Car',img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r=cv.split(img)

blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
    
cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

mergerd=cv.merge([b,g,r])
cv.imshow('Merged',mergerd)



cv.waitKey(0)