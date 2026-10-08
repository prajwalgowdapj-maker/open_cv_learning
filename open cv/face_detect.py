import cv2 as cv
import numpy as np
img = cv.imread('open cv/Faces/train/Elton John/9.jpg')
cv.imshow('Elton John',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
cv.imshow('Gray', gray)

harr_cascade = cv.CascadeClassifier('open cv/haar_face.xml')

faces_rect = harr_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)   
cv.imshow('Detected Faces', img)    

cv.waitKey(0)