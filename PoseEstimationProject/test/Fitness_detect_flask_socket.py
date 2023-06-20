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
draw = dr.Draw()

#影檔調整
# pixel_x = int(cap.get(3))
# pixel_y = int(cap.get(4))
# print(pixel_x,pixel_y)
# resize = 1


def Fitness_detect(use_Flask,use_socket,video_save,User,camera,q_flask,q_all,ID):
    jpeg = None
    print("go")
    if use_socket == False:
        #cap = cv2.VideoCapture("./input/25.mp4")
        cap = cv2.VideoCapture(0)
        pixel_x = int(cap.get(3))
        pixel_y = int(cap.get(4))
        print(pixel_x,pixel_y)
    if use_Flask == False:
        cv2.namedWindow("Image")
        
    if video_save:
        #儲存影檔
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        path = './output/'+str(ID)
        if not os.path.isdir(path):
            os.makedirs(path)
        Filename = path +'/'+time.strftime('%Y%m%d_%H%M%S', time.localtime())+'.avi'
        print("Save video place:",Filename)
        out = cv2.VideoWriter(Filename,fourcc,30.0,(940,480))
        #out = cv2.VideoWriter(Filename,fourcc,30.0,(480,940))
    #起始自訂義
    per_l_Lift,per_r_Lift,per_Squat,per_Pussup,per_Step = 0,0,0,0,0
    
    bar_l_Lift,bar_r_Lift,bar_Squat,bar_Pussup = 25,25,25,25
    color_l_Lift,color_r_Lift,color_Squat,color_Pussup\
    = (200, 200, 200),(200, 200, 200),(200, 200, 200),(200, 200, 200)
    
    #使用狀態
    status_of_use = "Still using"
    
    #起始時間
    pTime = 0
    
    #起使運動方向
    dir_l_Lift = 0
    dir_r_Lift = 0
    dir_Spuat = 0
    dir_Pussup = 0
    dir_Step = 0
    
    #起始準備動作偵數
    set_count = 0
    
    #起始定義位置
    strat1 = 0
    strat2 = 0
        
    #起始動作次數
    count_Squat,count_l_Lift,count_r_Lift,count_Pussup,count_Step, = 0,0,0,0,0
    
    #多久檢查一次使用者是否還在運動
    checktime = time.time()
    
    canvas = draw.drawPlot(count_l_Lift,per_l_Lift,bar_l_Lift,color_l_Lift,"Left Lift")
    canvas = draw.drawPlot(count_r_Lift,per_r_Lift,bar_r_Lift,color_r_Lift,"Right Lift")
    canvas = draw.drawPlot(count_Squat,per_Squat,bar_Squat,color_Squat,"Squat")
    canvas = draw.drawPlot(count_Pussup,per_Pussup,bar_Pussup,color_Pussup,"Puss up")
    canvas = draw.drawPlot(count_Step,per_Step,0,(200, 200, 200),"Step Count")
    
    Face=""
    using = False
    while True:
        if use_socket:
            img = q_all.get()
        else:
            success, img = cap.read()
        
        #關節顯示圖
        skeletion = np.zeros((pixel_y,pixel_x,3),dtype="uint8")
        
        #影項讀取與調整
        #img = cv2.resize(img, (int(pixel_x/resize),int(pixel_y/resize)))
        #img = cv2.resize(img, (640,480))
        
        #獲取關節圖
        img = detector.findPose(img)
        skeletion = detector.DrawPose(skeletion, True)
        #獲取關節點位
        lmList = detector.findPosition(img, False)
        
        #計算fps
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.rectangle(skeletion, (520,0), (640, 50),(79 ,79 ,60), cv2.FILLED)
        cv2.putText(skeletion, "fps:"+str(int(fps)), (530, 35), cv2.FONT_HERSHEY_DUPLEX, 1,
              (200, 200, 200), 2)
        #box for User
        cv2.rectangle(img, (490,0), (640, 50),(79 ,79 ,60), cv2.FILLED) 
        cv2.putText(img, User, (500, 35), cv2.FONT_HERSHEY_DUPLEX, 0.7,
                        (255 ,206 ,135), 2)

        
        if len(lmList) != 0:
            Face = detector.Face()
            
        
            if set_count <= 50:
                
                set1 = detector.findAngle(img, 14,12,24, False)
                set2 = detector.findAngle(img, 13,11,23, False)
                set3 = detector.findAngle(img, 23,24,26, False)
                set4 = detector.findAngle(img, 24,23,25, False)
                
                if 70 <= set1  and 70 <= set2  and 90 <= set3 <= 115 and 90 <= set4 <= 115:
                    
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
                    
                cv2.rectangle(img, (0,0), (280, 80),(79 ,79 ,60), cv2.FILLED)    
                # cv2.putText(img, "fps:"+str(int(fps)), (10, 35), cv2.FONT_HERSHEY_DUPLEX, 1,
                #       (200, 200, 200), 2)
                cv2.putText(img, "Get ready Pose", (10, 35), cv2.FONT_HERSHEY_DUPLEX, 1,color, 2)    	
                cv2.rectangle(img, (10, 50), (200, 70), color, 3)
                cv2.rectangle(img, (10,50), (int(bar), 70), color, cv2.FILLED)
                cv2.putText(img, f'{int(per)}%', (205, 70), cv2.FONT_HERSHEY_DUPLEX, 1,color, 1)
                if set_count == 51:  
                    #winsound.Beep(440, 400)
                    strat1 = detector.findLen(img, 11,12,True)
                    strat2 = detector.findLen(img, 23,24,True)
                    using = True

            if set_count > 50:
                
                #box for Face
                cv2.rectangle(skeletion,(220,0),(420,50),(79 ,79 ,60), cv2.FILLED)
                
              
                
                distance1 = detector.findLen(img, 11,12,False)
                distance2 = detector.findLen(img, 23,24,False)
                per_distance1 = np.interp(distance1, (0, strat1), (0, 100))
                per_distance2 = np.interp(distance2, (0, strat2), (0, 100))
                # per_distance = (per_distance1 + per_distance2) / 2
                # print("distance:",per_distance1)
                
                # Face == "R"
                # per_distance1 = 50
                # per_distance2 = 50
                #if per_distance < 55:
                if per_distance1 < 65 and per_distance2 < 70:
                    if Face == "L":

                        cv2.putText(skeletion, "Left_side", (245, 35), cv2.FONT_HERSHEY_DUPLEX, 1,
                                    (0,0,255), 2)
                        #per_l_Lift,per_r_Lift,per_Squat = 0,0,0
                        
                        #####################################################
                        #left lift#
                        angle = detector.findAngle(img, 11, 13, 15,False)
                        #print(angle)
                        per_l_Lift = np.interp(angle, (50, 150), (100, 0))
                        bar_l_Lift = np.interp(angle, (50, 140), (210, 25))
                        
                        #Check for the dumbbell curls
                        color_l_Lift = (200, 200, 200)
                        if per_l_Lift == 100:
                            color_l_Lift = (0,255,255)
                            if dir_l_Lift == 0:
                                count_l_Lift += 0.5
                                dir_l_Lift = 1
                        if per_l_Lift == 0:
                            color_l_Lift = (156, 156, 156)
                            if dir_l_Lift == 1:
                                count_l_Lift += 0.5
                                dir_l_Lift = 0
                        
                        #########################################################
                        
                        #left squat#
                        angle = detector.findAngle(img, 11,23,25,False)
                        per_Squat_1 = np.interp(angle, (90, 160), (100, 0))
                        bar_Squat_1 = np.interp(angle, (90, 160), (210, 25))
                        
                        angle = detector.findAngle(img, 23,25,27, False)
                        per_Squat_2 = np.interp(angle, (90, 160), (100, 0))
                        #print(per_Squat_1,per_Squat_2)
                        bar_Squat_2 = np.interp(angle, (90, 160), (210, 25))
                        #print(angle, per, bar)
                        per_Squat = (per_Squat_1 + per_Squat_2) / 2
                        bar_Squat = (bar_Squat_1 + bar_Squat_2) / 2
                        #print(per_Squat)
                        # Check for the dumbbell curls
                        color_Squat = (200, 200, 200)
                        if per_Squat == 100:
                            color_Squat = (0,255,255)
                            if dir_Spuat == 0:
                                count_Squat += 0.5
                                dir_Spuat = 1
                        if per_Squat == 0:
                            color_Squat = (156, 156, 156)
                            if dir_Spuat == 1:
                                count_Squat += 0.5
                                dir_Spuat = 0
                        
                                  

                        
                        ############################################################
                        #push up
                        puss_angle = detector.findAngle(skeletion, 23,31,33, False)
                        if puss_angle < 45:
                            angle = detector.findAngle(skeletion, 11,13,15, False)
                            per_Pussup_1 = np.interp(angle, (80, 150), (100, 0))
                            bar_Pussup_1 = np.interp(angle, (80, 150), (210, 25))
                            
                            
                            angle = detector.findAngle(skeletion, 23,11,13, False)
                            per_Pussup_2 = np.interp(angle, (20, 50), (100, 0))
                            bar_Pussup_2 = np.interp(angle, (20, 50), (210, 25))
                            
                            
                            per_Pussup = (per_Pussup_1 + per_Pussup_2) / 2
                            bar_Pussup = (bar_Pussup_1 + bar_Pussup_2) / 2
                            #print(bar_Pussup)
                            
                            color_Pussup = (200, 200, 200)
                            if per_Pussup == 100:
                                color_Pussup = (0,255,255)
                                if dir_Pussup == 0:
                                    count_Pussup += 0.5
                                    dir_Pussup = 1
                            if per_Pussup == 0:
                                color_Pussup = (156, 156, 156)
                                if dir_Pussup == 1:
                                    
                                    count_Pussup += 0.5
                                    dir_Pussup = 0
                        #########################################################
                        #Step     
            
                        angle = detector.findAngle(skeletion, 26,24,25, True)
                        per_Step = np.interp(angle, (10, 40), (0, 100))
                        if per_Step == 100:
                            if dir_Step == 0:
                                count_Step += 0.5
                                dir_Step = 1
                        if per_Step == 0:
                            if dir_Step == 1:
                                count_Step += 0.5
                                dir_Step = 0 
                        
                        
                        ############################################################
                    else:
                        cv2.putText(skeletion, "Right_side", (245, 35), cv2.FONT_HERSHEY_DUPLEX, 1,
                                    (0,0,255), 2)
                        
                        #####################################################
                        #Right lift#
                        angle = detector.findAngle(img, 12, 14, 16,False)
                        #print(angle)
                        per_r_Lift = np.interp(angle, (50, 150), (100, 0))
                        bar_r_Lift = np.interp(angle, (50, 140), (210, 25))
                        
                        #Check for the dumbbell curls
                        color_r_Lift = (200, 200, 200)
                        if per_r_Lift == 100:
                            color_r_Lift = (0,255,255)
                            if dir_r_Lift == 0:
                                count_r_Lift += 0.5
                                dir_r_Lift = 1
                        if per_r_Lift == 0:
                            color_r_Lift = (156, 156, 156)
                            if dir_r_Lift == 1:
                                count_r_Lift += 0.5
                                dir_r_Lift = 0
                  
                        #########################################################
                        
                        #Right squat
                        angle = detector.findAngle(img, 12,24,26,False)
                        per_Squat_1 = np.interp(angle, (90, 160), (100, 0))
                        bar_Squat_1 = np.interp(angle, (90, 160), (210, 25))
                        
                        angle = detector.findAngle(img, 24,26,28, False)
                        per_Squat_2 = np.interp(angle, (90, 160), (100, 0))
                        #print(per_Squat_1,per_Squat_2)
                        bar_Squat_2 = np.interp(angle, (90, 160), (210, 25))
                        #print(angle, per, bar)
                        per_Squat = (per_Squat_1 + per_Squat_2) / 2
                        bar_Squat = (bar_Squat_1 + bar_Squat_2) / 2
                        # Check for the dumbbell curls
                        color_Squat = (200, 200, 200)
                        if per_Squat == 100:
                            color_Squat = (0,255,255)
                            if dir_Spuat == 0:
                                count_Squat += 0.5
                                dir_Spuat = 1
                        if per_Squat == 0:
                            color_Squat = (156, 156, 156)
                            if dir_Spuat == 1:
                                count_Squat += 0.5
                                dir_Spuat = 0
                        #########################################################
                        #push up
                        puss_angle = detector.findAngle(skeletion, 24,32,33, False)
                        if puss_angle < 45:
                            angle = detector.findAngle(skeletion, 16,14,12, False)
                            per_Pussup_1 = np.interp(angle, (80, 150), (100, 0))
                            bar_Pussup_1 = np.interp(angle, (80, 150), (210, 25))
                            
                            
                            angle = detector.findAngle(skeletion, 14,12,24, False)
                            per_Pussup_2 = np.interp(angle, (20, 50), (100, 0))
                            bar_Pussup_2 = np.interp(angle, (20, 50), (210, 25))
                            
                            
                            per_Pussup = (per_Pussup_1 + per_Pussup_2) / 2
                            bar_Pussup = (bar_Pussup_1 + bar_Pussup_2) / 2
                            #print(bar_Pussup)
                            
                            color_Pussup = (200, 200, 200)
                            if per_Pussup == 100:
                                color_Pussup = (0,255,255)
                                if dir_Pussup == 0:
                                    count_Pussup += 0.5
                                    dir_Pussup = 1
                            if per_Pussup == 0:
                                color_Pussup = (156, 156, 156)
                                if dir_Pussup == 1:
                                    count_Pussup += 0.5
                                    dir_Pussup = 0
                       #########################################################
                        #Step     
            
                        angle = detector.findAngle(skeletion, 26,24,25, True)
                        per_Step = np.interp(angle, (10, 40), (0, 100))
                        if per_Step == 100:
                            if dir_Step == 0:
                                count_Step += 0.5
                                dir_Step = 1
                        if per_Step == 0:
                            if dir_Step == 1:
                                count_Step += 0.5
                                dir_Step = 0
                else:
                    if lmList[7][1:2] > lmList[8][1:2]:
                        cv2.putText(skeletion, "Front_side", (245, 35), cv2.FONT_HERSHEY_DUPLEX, 1,
                                    (0,0,255), 2)
                        angle = detector.findAngle(img, 11,23,25, False)
                        per_Squat_1 = np.interp(angle, (100, 160), (100, 0))
                        bar_Squat_1 = np.interp(angle, (100, 160), (210, 25))
                        
                        angle = detector.findAngle(img, 23,25,27, False)
                        per_Squat_2 = np.interp(angle, (100, 160), (100, 0))
                        #print(per_Squat_1,per_Squat_2)
                        bar_Squat_2 = np.interp(angle, (100, 160), (210, 25))
                        #print(angle, per, bar)
                        angle = detector.findAngle(img, 12,24,26, False)
                        per_Squat_3 = np.interp(angle, (100, 160), (100, 0))
                        bar_Squat_3 = np.interp(angle, (100, 160), (210, 25))
                        
                        angle = detector.findAngle(img, 24,26,28, False)
                        per_Squat_4 = np.interp(angle, (100, 160), (100, 0))
                        #print(per_Squat_1,per_Squat_2)
                        bar_Squat_4 = np.interp(angle, (100, 160), (210, 25))
                        per_Squat = (per_Squat_1 + per_Squat_2 + per_Squat_3 + per_Squat_4) / 4
                        bar_Squat = (bar_Squat_1 + bar_Squat_2 + bar_Squat_3 + bar_Squat_4) / 4
                        # Check for the dumbbell curls
                        color_Squat = (200, 200, 200)
                        if per_Squat == 100:
                            color_Squat = (0,255,255)
                            if dir_Spuat == 0:
                                count_Squat += 0.5
                                dir_Spuat = 1
                        if per_Squat == 0:
                            color_Squat = (156, 156, 156)
                            if dir_Spuat == 1:
                                count_Squat += 0.5
                                dir_Spuat = 0
                    else:
                        per_l_Lift,per_r_Lift,per_Squat,per_Pussup,per_Step = 0,0,0,0,0
                        cv2.putText(skeletion, "Back_side", (245, 35), cv2.FONT_HERSHEY_DUPLEX, 1,
                                      (0,0,255), 2)
                        cv2.rectangle(skeletion,(220,190),(420,290),(0 ,0 ,255),10)
                        cv2.rectangle(skeletion,(220,190),(420,290),(79 ,79 ,60), cv2.FILLED)
                        cv2.putText(skeletion, "Don't turn", (237, 227), cv2.FONT_HERSHEY_DUPLEX, 1, (255,255,255), 2)
                        cv2.putText(skeletion, "your back!", (237, 267), cv2.FONT_HERSHEY_DUPLEX, 1, (255,255,255), 2)
                        #cv2.imshow("Image", img)
                        
                

                canvas = draw.drawPlot(count_l_Lift,per_l_Lift,bar_l_Lift,color_l_Lift,"Left Lift")
                canvas = draw.drawPlot(count_r_Lift,per_r_Lift,bar_r_Lift,color_r_Lift,"Right Lift")
                canvas = draw.drawPlot(count_Squat,per_Squat,bar_Squat,color_Squat,"Squat")
                canvas = draw.drawPlot(count_Pussup,per_Pussup,bar_Pussup,color_Pussup,"Puss up")
                canvas = draw.drawPlot(count_Step,per_Step,0,(200, 200, 200),"Step Count")

        
        img_flask = np.hstack([img,skeletion]) 
        
        if using == True:
            img_save = np.hstack([img,canvas]) 
            if video_save:
                out.write(img_save)
            if use_Flask == False:
                cv2.namedWindow("Count")
                cv2.imshow("Count",img_save)
        
        if use_Flask:
            q_flask.put(img_flask)
        else:
            cv2.imshow("Image",img_flask)
        #print(q.qsize())
        # if cTime - checktime > 5:
        #     checktime = cTime
        #     status_of_use,User = user_status(camera)
        #     print(status_of_use)
        
        
        #按Q或停止運動結束迴圈
        if cv2.waitKey(1) & 0xFF == ord('q') or status_of_use =='Finish':
            break
        
        
    count_Squat = math.floor(count_Squat)
    count_l_Lift = math.floor(count_l_Lift)
    count_r_Lift = math.floor(count_r_Lift)
    print(count_Squat)
    print(count_l_Lift)
    print(count_r_Lift)
    
    # 釋放攝影機
    if use_socket == False:
        cap.release()
    # 關閉所有 OpenCV 視窗
    cv2.destroyAllWindows()
    
    
    return count_Squat,count_l_Lift,count_r_Lift

if __name__ == '__main__':   
    use_Flask,use_socket,video_save = False,False,False
    ID = 17
    global q
    q_flask = Queue()
    q_all = Queue()
    camera = 0
    User = "A107221055"
    Fitness_detect(use_Flask,use_socket,video_save,User,camera,q_flask,q_all,ID)