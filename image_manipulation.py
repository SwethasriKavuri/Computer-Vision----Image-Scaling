import numpy as np
import cv2
import sys

#Initial Image
#img = cv2.imread('/home/swethakavuri/Downloads/python.jpg.jpg')
img = cv2.imread(str(sys.argv[1]))
cv2.imshow('Display_Initial_Image',img)
cv2.waitKey()

#Resizing Image
rse = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation = cv2.INTER_LINEAR)
cv2.imshow('Resized_Image',rse)
cv2.waitKey()

#Dividing Pixels
cv2.waitKey()
b, g, r = cv2.split(img)
b = cv2.divide(b, 2)
g = cv2.divide(g, 2)
r = cv2.divide(r, 2)
res1 = cv2.merge((b, g, r))
cv2.imshow('Pixel Divided Image',res1)
cv2.waitKey()

#Adding Pixels
b = cv2.add(b,50)
g = cv2.add(g,50)
r = cv2.add(r,50)
res2 = cv2.merge((b, g, r))
cv2.imshow('Pixel Added Image',res2)
cv2.waitKey()

#Subtracting Pixels
b = cv2.subtract(b,50)
g = cv2.subtract(g,50)
r = cv2.subtract(r,50)			
res3 = cv2.merge((b, g, r))
cv2.imshow('Pixel Subtract Image',res3)
cv2.waitKey()

#Multiplying Pixels
b = cv2.multiply(b,4)
g = cv2.multiply(g,4)
r = cv2.multiply(r,4)
res4 = cv2.merge((b, g, r))
cv2.imshow('Pixel Multiply Image',res4)
cv2.waitKey()



