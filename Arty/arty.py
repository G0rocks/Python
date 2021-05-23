import numpy
import cv2
import time

rgb_max = 255
max_colours = rgb_max*rgb_max*rgb_max
print("Max colors: " + str(max_colours))
hypothesised_width = 1000
needed_height = max_colours/hypothesised_width
print("If width = " + str(hypothesised_width) + ", height = " + str(needed_height))
width = 600
height = 400
channels = 3
mynd_size_info = (height, width, channels)

R = 0
G = 0
B = 0
litur = (R,G,B)

X = range(1, width)
Y = range(1, height)

mynd = numpy.full(mynd_size_info, litur, dtype=numpy.uint8)
for x in X:
  for y in Y:
    R = rgb_max*(height-(y-1))/height
    G = rgb_max*((height/2)-abs((-height/2 + (y-1))))/(height/2)
    B = rgb_max*(y-1)/height
    litur = (R,G,B)

    mynd[y,x] = litur
  cv2.imshow('image',mynd)
  cv2.waitKey(1)

cv2.imshow('image',mynd)
cv2.waitKey(0)
