import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectaangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Rectangle', rectaangle)
cv.imshow('Circle', circle)

#bitwise AND-overlapping areas
bitwise_and = cv.bitwise_and(rectaangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

#bitwise OR-overlapping areas + non overlapping areas
bitwise_or = cv.bitwise_or(rectaangle, circle)  
cv.imshow('Bitwise OR', bitwise_or)

#bitwise XOR-non overlapping areas
bitwise_xor = cv.bitwise_xor(rectaangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

#bitwise NOT
bitwise_not = cv.bitwise_not(rectaangle)
cv.imshow('Bitwise NOT', bitwise_not)

cv.waitKey(0)