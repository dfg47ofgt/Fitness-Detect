# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 14:15:24 2021

@author: User
"""

import cv2
import numpy as np
import time
import PoseModule as pm
import Draw as dr
#import winsound
import math
#from connect_mssql import user_status
from queue import Queue
import os 

detector = pm.poseDetector()

cap = cv2.VideoCapture("./input/33.mp4")
#cap = cv2.VideoCapture("../input/13.mp4")
# pTime = 0




# detector = pm.poseDetector()
# cv2.namedWindow("Image")


cap = cv2.VideoCapture("./input/13.mp4")
#cap = cv2.VideoCapture("./input/33.mp4")
while True:
    success, img = cap.read()   
    
   

    img = detector.findPose(img)
    img = detector.DrawPose(img, True)
    lmList = detector.findPosition(img, False)
    cv2.imshow('Image', img)
    
    #cv2.imshow('skeletion', skeletion)
    #cv2.waitKey(10)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()    
cv2.destroyAllWindows()



# resize = 2  
# img = cv2.imread("./input/50.jpg")
# height, width, channels = img.shape
# print(height,width)
# count_l_Lift = 0
# dir1 = 0
# dir2 = 0
 
# img = cv2.resize(img, (int(width/resize),int(height/resize)))
   
# img = detector.findPose(img)
# img = detector.DrawPose(img, True)
# lmList = detector.findPosition(img, False)
# cv2.imshow('Image', img)

# #cv2.imshow('skeletion', skeletion)
# #cv2.waitKey(10)
# cv2.waitKey(0) 
# cap.release()    
# cv2.destroyAllWindows()