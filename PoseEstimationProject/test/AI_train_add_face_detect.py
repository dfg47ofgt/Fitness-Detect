import cv2
import numpy as np
import time
import PoseModule as pm
import Draw as dr
import winsound
import math
import sys
import face_recognition
import pickle

#cap = cv2.VideoCapture('./input/17.MOV')
#cap = cv2.VideoCapture('./input/26.mp4')
#cap = cv2.VideoCapture('./input/22.mp4')
cap = cv2.VideoCapture(0)

detector = pm.poseDetector()
draw = dr.Draw()


count_l_Lift,per_l_Lift,count_r_Lift,per_r_Lift,count_Squat,per_Squat = 0,0,0,0,0,0
bar_l_Lift,bar_r_Lift,bar_Squat = 450,450,450
color_l_Lift,color_r_Lift,color_Squat = (200, 200, 200),(200, 200, 200),(200, 200, 200)

#起始自訂義
start_count = 0
set_count = 0
images = []
classNames = []
detect_USER = "Unknown"
User = "None"
dir1 = 0
dir2 = 0
pTime = 0
strat1 = 0
strat2 = 0
Face=""
using = False
with open('./images_id/id/dataset_faces.dat', 'rb') as f:
	all_face_encodings = pickle.load(f)

classNames = list(all_face_encodings.keys())
encodeListKnown = np.array(list(all_face_encodings.values()))

#fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#Filename = './output/'+time.strftime('%Y%m%d_%H%M%S', time.localtime())+'.avi'

#print()

#out = cv2.VideoWriter(Filename,fourcc,30.0,(1210,480))
pixel_x = int(cap.get(3))
pixel_y = int(cap.get(4))
print(pixel_x,pixel_y)
resize = 1


while True: 
    print(using)
    success, img = cap.read()
    if User != "None":
        #img = cv2.imread("./input/20.png")
        #img = cv2.resize(img, (int(pixel_x/resize),int(pixel_y/resize)))
        #img = cv2.resize(img, (640,480))
        #fps
        img = detector.findPose(img)
        lmList = detector.findPosition(img, False)
        #print(lmList)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        
        #box for User
        cv2.rectangle(img, (500,0), (640, 50),(79 ,79 ,60), cv2.FILLED) 
        cv2.putText(img, User, (520, 35), cv2.FONT_HERSHEY_DUPLEX, 1,
                       (255 ,206 ,135), 2)
        if len(lmList) != 0:
            Face = detector.Face()
            # Right Arm
            #angle = detector.findAngle(img, 12, 14, 16,True)
            # Left Arm
            #angle = detector.findAngle(img, 11, 13, 15,True)
            # Left Leg
            #angle = detector.findAngle(img, 23, 25, 27, False)
            
            if set_count <= 50:
                set1 = detector.findAngle(img, 14,12,24, False)
                set2 = detector.findAngle(img, 13,11,23, False)
                set3 = detector.findAngle(img, 23,24,26, False)
                set4 = detector.findAngle(img, 24,23,25, False)
                
                if 70 <= set1  and 70 <= set2  and 90 <= set3 <= 115 and 90 <= set4 <= 115:
                    img = detector.DrawPose(img, True)
                    set_count += 1
                    #print(set_count)
                else:
                    set_count = 0
                per= np.interp(set_count, (0, 50), (0, 100))
                bar = np.interp(set_count, (0, 50), (10, 200))
                
                # Draw Bar
                color = (180,180,180)
                if per > 90:
                    color = (0,255,255)
                    
                cv2.rectangle(img, (0,0), (270, 110),(79 ,79 ,60), cv2.FILLED)    
                cv2.putText(img, "fps:"+str(int(fps)), (10, 35), cv2.FONT_HERSHEY_DUPLEX, 1,
                      (200, 200, 200), 2)
                cv2.putText(img, "Get ready Pose", (10, 70), cv2.FONT_HERSHEY_DUPLEX, 1,color, 2)    	
                cv2.rectangle(img, (10, 85), (200, 100), color, 3)
                cv2.rectangle(img, (10,85), (int(bar), 100), color, cv2.FILLED)
                cv2.putText(img, f'{int(per)}%', (205, 100), cv2.FONT_HERSHEY_DUPLEX, 1,color, 1)
                if set_count == 51:  
                    strat1 = detector.findLen(img, 11,12,True)
                    strat2 = detector.findLen(img, 23,24,True)
                    using = True
                    #print(strat1,strat2)
                    
                #cv2.namedWindow("Image")
                #cv2.imshow("Image", img)
                #out.write(img)
            if set_count > 50:
                cv2.rectangle(img,(220,0),(420,50),(79 ,79 ,60), cv2.FILLED)
                img = detector.DrawPose(img, True)
                #cv2.putText(img, "Recording...",(10, 65), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,color, 1)
    
                
                distance1 = detector.findLen(img, 11,12,False)
                distance2 = detector.findLen(img, 23,24,False)
                per_distance1 = np.interp(distance1, (0, strat1), (0, 100))
                per_distance2 = np.interp(distance2, (0, strat2), (0, 100))
                # per_distance = (per_distance1 + per_distance2) / 2
                # print("distance:",per_distance1)
                
                
                #if per_distance < 55:
                if per_distance1 < 65 and per_distance2 < 70:
                    if Face == "L":
                        
                        
                        cv2.putText(img, "Left_side", (245, 35), cv2.FONT_HERSHEY_DUPLEX, 1,
                                    (0,0,255), 2)
                        #per_l_Lift,per_r_Lift,per_Squat = 0,0,0
                        
                        #####################################################
                        #left lift#
                        angle = detector.findAngle(img, 11, 13, 15,False)
                        #print(angle)
                        per_l_Lift = np.interp(angle, (50, 150), (100, 0))
                        bar_l_Lift = np.interp(angle, (50, 140), (165, 450))
                        
                        #Check for the dumbbell curls
                        color_l_Lift = (200, 200, 200)
                        if per_l_Lift == 100:
                            color_l_Lift = (0,255,255)
                            if dir1 == 0:
                                count_l_Lift += 0.5
                                dir1 = 1
                        if per_l_Lift == 0:
                            color_l_Lift = (156, 156, 156)
                            if dir1 == 1:
                                count_l_Lift += 0.5
                                dir1 = 0
                        
                        #########################################################
                        
                        #left squat#
                        angle = detector.findAngle(img, 11,23,25,False)
                        per_Squat_1 = np.interp(angle, (90, 160), (100, 0))
                        bar_Squat_1 = np.interp(angle, (90, 160), (165, 450))
                        
                        angle = detector.findAngle(img, 23,25,27, False)
                        per_Squat_2 = np.interp(angle, (90, 160), (100, 0))
                        #print(per_Squat_1,per_Squat_2)
                        bar_Squat_2 = np.interp(angle, (90, 160), (165, 450))
                        #print(angle, per, bar)
                        per_Squat = (per_Squat_1 + per_Squat_2) / 2
                        bar_Squat = (bar_Squat_1 + bar_Squat_2) / 2
                        #print(per_Squat)
                        # Check for the dumbbell curls
                        color_Squat = (200, 200, 200)
                        if per_Squat == 100:
                            color_Squat = (0,255,255)
                            if dir2 == 0:
                                count_Squat += 0.5
                                dir2 = 1
                        if per_Squat == 0:
                            color_Squat = (156, 156, 156)
                            if dir2 == 1:
                                count_Squat += 0.5
                                dir2 = 0
                        
                        ############################################################
                    else:
                        cv2.putText(img, "Right_side", (245, 35), cv2.FONT_HERSHEY_DUPLEX, 1,
                                    (0,0,255), 2)
                        
                        #####################################################
                        #Right lift#
                        angle = detector.findAngle(img, 12, 14, 16,False)
                        #print(angle)
                        per_r_Lift = np.interp(angle, (50, 150), (100, 0))
                        bar_r_Lift = np.interp(angle, (50, 140), (165, 450))
                        
                        #Check for the dumbbell curls
                        color_r_Lift = (200, 200, 200)
                        if per_r_Lift == 100:
                            color_r_Lift = (0,255,255)
                            if dir1 == 0:
                                count_r_Lift += 0.5
                                dir1 = 1
                        if per_r_Lift == 0:
                            color_r_Lift = (156, 156, 156)
                            if dir1 == 1:
                                count_r_Lift += 0.5
                                dir1 = 0
                        
                        #########################################################
                        
                        #Right squat
                        angle = detector.findAngle(img, 12,24,26,False)
                        per_Squat_1 = np.interp(angle, (90, 160), (100, 0))
                        bar_Squat_1 = np.interp(angle, (90, 160), (165, 450))
                        
                        angle = detector.findAngle(img, 24,26,28, False)
                        per_Squat_2 = np.interp(angle, (90, 160), (100, 0))
                        #print(per_Squat_1,per_Squat_2)
                        bar_Squat_2 = np.interp(angle, (90, 160), (165, 450))
                        #print(angle, per, bar)
                        per_Squat = (per_Squat_1 + per_Squat_2) / 2
                        bar_Squat = (bar_Squat_1 + bar_Squat_2) / 2
                        # Check for the dumbbell curls
                        color_Squat = (200, 200, 200)
                        if per_Squat == 100:
                            color_Squat = (0,255,255)
                            if dir2 == 0:
                                count_Squat += 0.5
                                dir2 = 1
                        if per_Squat == 0:
                            color_Squat = (156, 156, 156)
                            if dir2 == 1:
                                count_Squat += 0.5
                                dir2 = 0
                        
                else:
                    if lmList[7][1:2] > lmList[8][1:2]:
                        cv2.putText(img, "Front_side", (245, 35), cv2.FONT_HERSHEY_DUPLEX, 1,
                                    (0,0,255), 2)
                        angle = detector.findAngle(img, 11,23,25, False)
                        per_Squat_1 = np.interp(angle, (100, 160), (100, 0))
                        bar_Squat_1 = np.interp(angle, (100, 160), (165, 450))
                        
                        angle = detector.findAngle(img, 23,25,27, False)
                        per_Squat_2 = np.interp(angle, (100, 160), (100, 0))
                        #print(per_Squat_1,per_Squat_2)
                        bar_Squat_2 = np.interp(angle, (100, 160), (165, 450))
                        #print(angle, per, bar)
                        angle = detector.findAngle(img, 12,24,26, False)
                        per_Squat_3 = np.interp(angle, (100, 160), (100, 0))
                        bar_Squat_3 = np.interp(angle, (100, 160), (165, 450))
                        
                        angle = detector.findAngle(img, 24,26,28, False)
                        per_Squat_4 = np.interp(angle, (100, 160), (100, 0))
                        #print(per_Squat_1,per_Squat_2)
                        bar_Squat_4 = np.interp(angle, (100, 160), (165, 450))
                        per_Squat = (per_Squat_1 + per_Squat_2 + per_Squat_3 + per_Squat_4) / 4
                        bar_Squat = (bar_Squat_1 + bar_Squat_2 + bar_Squat_3 + bar_Squat_4) / 4
                        # Check for the dumbbell curls
                        color_Squat = (200, 200, 200)
                        if per_Squat == 100:
                            color_Squat = (0,255,255)
                            if dir2 == 0:
                                count_Squat += 0.5
                                dir2 = 1
                        if per_Squat == 0:
                            color_Squat = (156, 156, 156)
                            if dir2 == 1:
                                count_Squat += 0.5
                                dir2 = 0
                    else:
                        per_l_Lift,per_r_Lift,per_Squat = 0,0,0
                        cv2.putText(img, "Back_side", (245, 35), cv2.FONT_HERSHEY_DUPLEX, 1,
                                      (0,0,255), 2)
                        cv2.rectangle(img,(220,190),(420,290),(0 ,0 ,255),10)
                        cv2.rectangle(img,(220,190),(420,290),(79 ,79 ,60), cv2.FILLED)
                        cv2.putText(img, "Don't turn", (237, 227), cv2.FONT_HERSHEY_DUPLEX, 1, (255,255,255), 2)
                        cv2.putText(img, "your back!", (237, 267), cv2.FONT_HERSHEY_DUPLEX, 1, (255,255,255), 2)
                        #cv2.imshow("Image", img)
                        
                
                cv2.rectangle(img, (0,0), (120, 50),(79 ,79 ,60), cv2.FILLED)
                cv2.putText(img, "fps:"+str(int(fps)), (10, 35), cv2.FONT_HERSHEY_DUPLEX, 1,
                      (200, 200, 200), 2)
                #print("count_Lift:",count_Lift)
                canvas = draw.drawPlot(count_l_Lift,per_l_Lift,bar_l_Lift,color_l_Lift,"Left Lift")
                # cv2.namedWindow("Left Lift")
                # cv2.imshow("Left Lift",canvas_l_lift)
                canvas = draw.drawPlot(count_r_Lift,per_r_Lift,bar_r_Lift,color_r_Lift,"Right Lift")
                #print("count_Spuat",count_Squat)
                canvas = draw.drawPlot(count_Squat,per_Squat,bar_Squat,color_Squat,"Squat")
                #cv2.namedWindow("Squat")
                #cv2.imshow("Squat",canvas)
                
                drawList = draw.drawList(lmList)
                # cv2.namedWindow("X Y")
                # cv2.imshow("X Y",drawList)
                
        else:
            cv2.rectangle(img, (0,0), (120, 50),(79 ,79 ,60), cv2.FILLED)
            cv2.putText(img, "fps:"+str(int(fps)), (10, 35), cv2.FONT_HERSHEY_DUPLEX, 1,
                      (200, 200, 200), 2)
            
        cv2.namedWindow("Image")
        if using == True:
            img = np.hstack([img,canvas,drawList])
            cv2.imshow("Image", img)
        else:
            cv2.imshow("Image", img)
        #out.write(img)
    else:
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
     
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
     
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
         
        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            
            #name = "Unknown"
            
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
            #print(faceDis)
            matchIndex = np.argmin(faceDis)
            
            
            if matches[matchIndex]:
                name = classNames[matchIndex]
                if detect_USER == name:
                    start_count += 1
                else:
                    start_count = 0
                    detect_USER = name 
                
                #print(name)
                y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

        
        cv2.rectangle(img, (0,0), (120, 50),(79 ,79 ,60), cv2.FILLED)
        cv2.putText(img, "fps:"+str(int(fps)), (10, 35), cv2.FONT_HERSHEY_DUPLEX, 1,
                    (200, 200, 200), 2)
        cv2.namedWindow("Image")
        cv2.imshow("Image", img)
        
        if start_count == 5:
            User = name
            winsound.Beep(440, 400)
        
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
count_Squat = math.floor(count_Squat)
count_l_Lift = math.floor(count_l_Lift)
count_r_Lift = math.floor(count_r_Lift)
print(count_Squat)
print(count_l_Lift)
print(count_r_Lift)

# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()
