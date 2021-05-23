import numpy
import cv2
import time

width = 250
height = width
mynd_size = (width, height)

R = 9
G = 150
B = 109
litur = (R,G,B)

X = range(width)
Y = range(height)

mynd = numpy.full((height,width,3), litur, dtype=numpy.uint8)
for x in X:
  for y in Y:
    R = x
    G = y
    B = 109
    litur = (R,G,B)
    mynd[x,y] = litur

cv2.imshow('image',mynd)
cv2.waitKey(0)
