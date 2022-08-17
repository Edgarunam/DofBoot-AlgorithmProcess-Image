import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread("/home/jetson/Open-CV-Servicio/Img-Src/Cirulo-Color.png")
hsv_nemo = cv.cvtColor(image, cv.COLOR_RGB2HSV)
light_orange=(1,190,200)
dark_orange=(18,255,255)
mask = cv.inRange(hsv_nemo, light_orange, dark_orange)
result = cv.bitwise_and(image, image, mask=mask)
#·lt.imshow(image)
plt.imshow(mask)
plt.show()