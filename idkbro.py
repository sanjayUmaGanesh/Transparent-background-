import cv2 
import numpy as np 
import pyautogui as pg
import time
  
video = cv2.VideoCapture(0)
time.sleep(3)
ret, masker = video.read()

ci = input('what colour?')
if ci == 'red':
    l_green = np.array([0,180,50])
    u_green = np.array([10,255,255])
if ci == 'blue':
    l_green = np.array([100,150,0])
    u_green = np.array([180,255,255])

while True:
  
    ret, frame = video.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  
    frame = cv2.resize(frame, (640, 480))
    masker = cv2.resize(masker, (640, 480))
 
    mask = cv2.inRange(hsv, l_green, u_green)
    res = cv2.bitwise_and(frame, frame, mask = mask)
  
    f = frame - res
    f = np.where(f == 0, masker, f)
  
    cv2.imshow("video", masker)
    cv2.imshow("mask", f)
  
    if cv2.waitKey(25) == 27:
        break 
  
video.release()
cv2.destroyAllWindows()