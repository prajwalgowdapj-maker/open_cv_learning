import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('open cv/cars/6.jpg')
cv.imshow('Car',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blank = np.zeros(gray.shape, dtype='uint8')
mask=cv.circle(blank, (gray.shape[1]//2, gray.shape[0]//2), 100, 255, -1)
masked = cv.bitwise_and(gray, gray, mask=mask)
cv.imshow('Masked Image', masked)
#grayscale histogram
hist = cv.calcHist([gray], [0],masked, [256], [0, 256])
plt.plot(hist)
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.title('Grayscale Histogram')
#plt.show()

#Colour histogram
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist_color = cv.calcHist([img], [i],masked, [256], [0, 256])
    plt.plot(hist_color, color=col)
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.title('Colour Histogram')
plt.show()

cv.waitKey(0)