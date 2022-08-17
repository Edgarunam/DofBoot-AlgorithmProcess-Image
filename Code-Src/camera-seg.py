import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
 
video = cv.VideoCapture(0)
  
while(True):
      
    ret, frame = video.read()
    capture = cv.cvtColor(frame, cv.COLOR_RGB2HSV)
    light_orange=(20,20,20)
    dark_orange=(150,150,150)
    mask = cv.inRange(capture, light_orange, dark_orange)

  
    
    #
    result = cv.bitwise_and(capture, capture, mask=mask)
    #contours, hierarchy = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    #output = cv.drawContours(result, contours, -1, (0, 0, 255), 3)
  
    cv.imshow('frame', mask)
      

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
  

video.release()

cv.destroyAllWindows()