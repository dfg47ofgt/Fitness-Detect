import cv2
import time
import mediapipe as mp
import PoseModule_new as pm
import numpy as np
import os
import socket

os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"   
os.environ["CUDA_VISIBLE_DEVICES"]="0"   

def Fitness_detect():
    cap = cv2.VideoCapture(0)
    print('camera is open')
    #cap = cv2.VideoCapture("./input/lex61335_4.mp4")
    
    success = True
    detector = pm.poseDetector()
    pTime = 0
    count = 0
    dir = 0
    per = 0
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    Filename = './output/'+time.strftime('%Y%m%d_%H%M%S', time.localtime())+'.avi'
    cv2.namedWindow("Image")
    out = cv2.VideoWriter(Filename, fourcc, 30.0, (1280, 720))
    #while ret:    
    while True:
            success, img = cap.read()
            #img = cv2.resize(img, (640,480))      #(1920,1080)(552,739)
            
            #fps
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(img, "fps:"+str(int(fps)), (20, 30), cv2.FONT_HERSHEY_DUPLEX, 1
                       ,(255, 99, 71), 2)
            
            if success:
                img = detector.findPose(img)
                img = detector.DrawPose(img, True)
                lmList = detector.findPosition(img, False)
                if len(lmList) != 0:
             ##########################################################################     
                    #Left
                    angle5 = detector.findAngle(img, 23, 25, 27, True)   #夾角角度
                    #Right
                    angle5 = detector.findAngle(img, 24, 26, 28, True)
                    #lenn = detector.findLen(img, 11,23, True)
                    #print(lenn)                
                    per = np.interp(angle5, (90, 170), (0, 100))
                    bar = np.interp(angle5, (100, 170), (650, 100))
                    #print(angle5, per)
                
                #計數器 
                    color = (255, 0, 255)
                    if per == 100:
                        color = (0, 255, 0)
                        if dir == 0:                    
                            count += 0.5
                            dir = 1
                    if per == 0:
                        color = (0, 255, 0)               
                        if dir == 1:                    
                            count += 0.5
                            dir = 0
                #print(count)
                
                #Draw bar
                    cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)   #(1100, 100), (1175, 650)  (600, 100), (100, 140)
                    cv2.rectangle(img, (1100, int(bar)),(1175, 650), color, cv2.FILLED)
                    cv2.putText(img, f'{int(per)}%', (1100,100), cv2.FONT_HERSHEY_DUPLEX, 2
                            , color, 2)
                
                #Draw count
                    cv2.putText(img, "Done:"+str(int(count)), (20, 70), cv2.FONT_HERSHEY_DUPLEX, 1
                            , (255, 0, 0), 2)
                    
                out.write(img)  
                cv2.imshow('Image', img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
            else:
                break  
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    Fitness_detect()
    