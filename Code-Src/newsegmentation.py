import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
 
video = cv.VideoCapture(0)
  
while(True):
      
    ret, frame = video.read()
    capture = cv.cvtColor(frame, cv.COLOR_RGB2HSV)
    light_orange=(50,20,20)
    dark_orange=(100,255,255)
    light_green=(50,100,100)
    dark_green=(70,255,255)
    mask = cv.inRange(capture, light_orange, dark_orange)

     
    kernel = np.ones((7,7),np.uint8)
    
    mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
  
    #
    result = cv.bitwise_and(capture, capture, mask=mask)
    contours, hierarchy = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    output = cv.drawContours(result, contours, -1, (0, 0, 255), 3)
  
    cv.imshow('frame', output)
      

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
  

video.release()

cv.destroyAllWindows()
