import cv2
import time
import PoseModule as pm
import numpy as np
import random
from queue import Queue



def gaming_3_start(cap,use_Flask,use_socket,q_flask,q_all):
    
    if use_socket == False:
        #cap = cv2.VideoCapture("./input/25.mp4")
        # cap = cv2.VideoCapture(0)
        pixel_x = int(cap.get(3))
        pixel_y = int(cap.get(4))
        print(pixel_x,pixel_y)
    if use_Flask == False:
        cv2.namedWindow("GAME")
    

    detector = pm.poseDetector()
      
    back_per = 0
    pTime = 0
    set_count = 0
    success = True
    circle_count = 3
    point_count = 3
    point_deduction = 2
    score = 0
    score_show_Time = np.empty((0,5))
    continue_count = 0
    leave_count = 0 
    back_count = 0
    game_time = 60
    Finish = False

    point_position = np.empty((0,2))
    point_field_left = np.empty((0,2))
    point_field_right = np.empty((0,2))
    point_time = np.array([])
    
    #起始自訂義
    previous_per_Squat = 0
    per_Squat = 0
    bar_Squat = 25
    
    already_get = [0,0]
    
    #起使運動方向
    dir_Spuat = 0
    
    start_hoding_time = 0
    keep_hoding_time = 0
    
    
    
    
    #起始準備動作偵數
    set_count = 0
    
    #起始定義位置
    strat1 = 0
    strat2 = 0
        
    #起始動作次數
    count_Squat = 0
    
    
    
    while True:
        if use_socket:
            img = q_all.get()
        else:
            success, img = cap.read()
       
        img = cv2.flip(img,1)
        img = detector.findPose(img)
        img = detector.DrawPose(img, True)
        lmList = detector.findPosition(img, False)
        #計算fps
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        
        #fps框
        cv2.putText(img, "fps:"+str(int(fps)), (520, 460), cv2.FONT_HERSHEY_DUPLEX, 1,
              (200, 200, 200), 2)
        
        
        if Finish == False:
            #離開框
            cv2.rectangle(img,(0,180),(30,300),(0,0,0),10)#34 139 34#	139 71 38
            cv2.rectangle(img,(0,180),(30,300),(19 ,69 ,139), cv2.FILLED)#255 211 155
            cv2.putText(img, "B", (5, 210), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0), 2)#205 55 0
            cv2.putText(img, "A", (5, 235), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0), 2)#205 55 0
            cv2.putText(img, "C", (5, 260), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0), 2)#205 55 0
            cv2.putText(img, "K", (5, 285), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0), 2)#205 55 0 139 69 19
            if len(lmList) != 0:
                right_wrist_x,right_wrist_y = lmList[19][1:3]
                left_wrist_x ,left_wrist_y  = lmList[20][1:3]
                
                if (0 < right_wrist_x < 30 and 180 < right_wrist_y < 300)\
                or (0 < left_wrist_x <  30 and 180 < left_wrist_y < 300):
                    back_count+= 1
                else:
                    back_count = 0
                
                back_bar = np.interp(back_count, (0, 49), (300, 180))  
                back_per= np.interp(back_count, (0, 50), (0, 100))
        
                cv2.rectangle(img, (0,int(back_bar)),(30,300), (0,0,0), cv2.FILLED)
        
            if back_per == 100:
                break
        
        
        
        
        if set_count <= 50:
            #準備姿勢框
            per= np.interp(set_count, (0, 50), (0, 100))
            bar = np.interp(set_count, (0, 50), (10, 200))
            
            color = (180,180,180)
            if per > 90:
                color = (0,255,255)
            cv2.rectangle(img, (0,0), (280, 80),(79 ,79 ,60), cv2.FILLED)        
            cv2.putText(img, "Get ready Pose", (10, 35), cv2.FONT_HERSHEY_DUPLEX, 1,color, 2)    	
            cv2.rectangle(img, (10, 50), (200, 70), color, 3)
            cv2.rectangle(img, (10,50), (int(bar), 70), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)}%', (205, 70), cv2.FONT_HERSHEY_DUPLEX, 1,color, 1)
        
     
        
        if len(lmList) != 0:
            if set_count <= 50:
                
                #人體框
                # x_1 = lmList[12][1] -50
                # y_1 = lmList[5][2] 
                # x_2 = lmList[11][1] + 50
                # y_2 = lmList[29][2] 
                
                
                # topleft = [x_1,y_1]
                # downright = [x_2,y_2]
                # color=(255,0,0)  #蓝色
                # cv2.rectangle(img,topleft, downright, color, 2)
                
                set1 = detector.findAngle(img, 14,12,24, False)
                set2 = detector.findAngle(img, 13,11,23, False)
                set3 = detector.findAngle(img, 23,24,26, False)
                set4 = detector.findAngle(img, 24,23,25, False)
                
                if 70 <= set1  and 70 <= set2  and 90 <= set3 <= 115 and 90 <= set4 <= 115:
                    
                    set_count += 1
                    #print(set_count)
                else:
                    set_count = 0
                    
                
                if set_count == 51:  
                    
                    strat1 = detector.findLen(img, 11,12,False)
                    strat2 = detector.findLen(img, 23,24,False)
                   
             
                    #設定遊戲結束時間
                    FTime = time.time() + game_time
                    
            elif set_count > 50 and FTime - cTime > 0:
                
                #計算剩餘時間
                game_time_left = int(FTime - cTime)
                m, s = divmod(game_time_left, 60)
                min_sec_format = '{:02d}:{:02d}'.format(m, s)
                
                
                #剩餘時間框
                cv2.rectangle(img, (500,0), (640, 50),(79 ,79 ,60), cv2.FILLED)  
                cv2.putText(img, min_sec_format, (520, 35), cv2.FONT_HERSHEY_DUPLEX, 1,(180,180,180), 2)   

                #分數框
                #color=(0,255,255)  #蓝色
                
                cv2.rectangle(img, (0,0), (230, 50),(79 ,79 ,60), cv2.FILLED)  
                cv2.putText(img, "Score :", (10, 35), cv2.FONT_HERSHEY_DUPLEX, 1,(180,180,180), 2)    	
                cv2.putText(img, str(score), (140, 35), cv2.FONT_HERSHEY_DUPLEX, 1,(180,180,180), 2)    
                

 
                #產生加分動畫
                dele = []
                for i in range(len(score_show_Time)):
                    c_time = time.time()
                    if score_show_Time[i][0] - c_time > 0:
                        if score_show_Time[i][4] == 1:
                            cv2.putText(img, '+'+str(int(score_show_Time[i][3])), (int(score_show_Time[i][1])-15,\
                                        int(score_show_Time[i][2])), cv2.FONT_HERSHEY_DUPLEX, 1.3,(71 ,130 ,255), 2)
                        else:
                            cv2.putText(img, '-'+str(int(score_show_Time[i][3])), (int(score_show_Time[i][1])-15,\
                                        int(score_show_Time[i][2])), cv2.FONT_HERSHEY_DUPLEX, 1,(0 ,0 ,255), 2)
                    else:
                        dele.append(i)
                                              
                score_show_Time  = np.delete(score_show_Time,dele,axis = 0)#刪除a的第二行。
 

                #刪除超出時間的球
                dele_bal = []
                
                c_time = time.time()
                for i in range(len(point_time)):
                    if point_time[i] - c_time < 0: 
                        dele_bal.append(i)
                        cir_x,cir_y = point_position[i][:]
                        score_show_Time = np.append(score_show_Time, np.array([[time.time() + 0.3, cir_x, cir_y,point_deduction,0]]), axis=0)
                        score -= 2
                #print("del",dele_bal)
                point_field_left  = np.delete(point_field_left,dele_bal,axis = 0)
                point_field_right = np.delete(point_field_right,dele_bal,axis = 0)
                point_position = np.delete(point_position,dele_bal,axis = 0) 
                point_time = np.delete(point_time,dele_bal) 
                
                
                #獲取使用者面向
                Face = detector.Face()
                #計算肩膀與肩膀之間距離、骨盆與骨盆之間距離 結合face來決定使用者面向
                distance1 = detector.findLen(img, 11,12,False)
                distance2 = detector.findLen(img, 23,24,False)
                per_distance1 = np.interp(distance1, (0, strat1), (0, 100))
                per_distance2 = np.interp(distance2, (0, strat2), (0, 100))
                
                if per_distance1 < 65 and per_distance2 < 70:
                    #使用者面向左邊
                    if Face == "L":
                        
                        #####################################################

                        #left squat#
                        angle = detector.findAngle(img, 11,23,25,False)
                        per_Squat_1 = np.interp(angle, (90, 160), (100, 0))
                        bar_Squat_1 = np.interp(angle, (90, 160), (210, 25))
                        
                        angle = detector.findAngle(img, 23,25,27, False)
                        per_Squat_2 = np.interp(angle, (90, 160), (100, 0))
                        bar_Squat_2 = np.interp(angle, (90, 160), (210, 25))
                        
                        per_Squat = (per_Squat_1 + per_Squat_2) / 2
                        bar_Squat = (bar_Squat_1 + bar_Squat_2) / 2

                        # Check for the Spuat curls
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
                                #Step     
            
                       
                    else:
                         #Right squat
                        angle = detector.findAngle(img, 12,24,26,False)
                        per_Squat_1 = np.interp(angle, (90, 160), (100, 0))
                        bar_Squat_1 = np.interp(angle, (90, 160), (210, 25))
                        
                        angle = detector.findAngle(img, 24,26,28, False)
                        per_Squat_2 = np.interp(angle, (90, 160), (100, 0))
                        bar_Squat_2 = np.interp(angle, (90, 160), (210, 25))
 
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
                else:
                    #使用者面向正面
                    if lmList[7][1:2] > lmList[8][1:2]:
                        
                        #squat
                        angle = detector.findAngle(img, 11,23,25, True)
                        per_Squat_1 = np.interp(angle, (145, 160), (100, 0))
                        bar_Squat_1 = np.interp(angle, (130, 160), (210, 25))
                        
                        angle = detector.findAngle(img, 23,25,27, True)
                        per_Squat_2 = np.interp(angle, (145, 160), (100, 0))
                        bar_Squat_2 = np.interp(angle, (130, 160), (210, 25))

                        angle = detector.findAngle(img, 12,24,26, True)
                        per_Squat_3 = np.interp(angle, (145, 160), (100, 0))
                        bar_Squat_3 = np.interp(angle, (120, 160), (210, 25))
                        
                        angle = detector.findAngle(img, 24,26,28, True)
                        per_Squat_4 = np.interp(angle, (145, 160), (100, 0))
                        bar_Squat_4 = np.interp(angle, (120, 160), (210, 25))
                        
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
                         #####################################################
                       
                        #########################################################
                    else:
                        #使用者面向後面，顯示"Don't turn your back"
                        per_Squat = 0
                        cv2.putText(img, "Back_side", (245, 35), cv2.FONT_HERSHEY_DUPLEX, 1,
                                      (0,0,255), 2)
                        cv2.rectangle(img,(220,190),(420,290),(0 ,0 ,255),10)
                        cv2.rectangle(img,(220,190),(420,290),(79 ,79 ,60), cv2.FILLED)
                        cv2.putText(img, "Don't turn", (237, 227), cv2.FONT_HERSHEY_DUPLEX, 1, (255,255,255), 2)
                        cv2.putText(img, "your back!", (237, 267), cv2.FONT_HERSHEY_DUPLEX, 1, (255,255,255), 2)    
                
                # print("per",per_Squat)
                # print("count",count_Squat)
                
                if count_Squat == 1:
                    score += 10
                    count_Squat = 0
                
                if per_Squat == 100 and previous_per_Squat != 100:
                    start_hoding_time = time.time()
                    
                if per_Squat and previous_per_Squat == 100:
 
                    keep_hoding_time = cTime - start_hoding_time
                    
                    
                    get_s = 3 + ((keep_hoding_time-1)//3)
                    already_get[0],already_get[1] = int(keep_hoding_time),get_s
                    print("already_get",already_get)
                
               
                previous_per_Squat = per_Squat
               
                # start_hoding_time = 0
                # keep_hoding_time = 0
                    
                # #Time_left = int(finish_Time - cur_time)
                # right_wrist_x,right_wrist_y = lmList[19][1:3]
                # left_wrist_x ,left_wrist_y  = lmList[20][1:3]
                
                # right_ankle_x,right_ankle_y = lmList[27][1:3]
                # left_ankle_x ,left_ankle_y  = lmList[28][1:3]
                
                # right_foot_x,right_foot_y = lmList[31][1:3]
                # left_foot_x ,left_foot_y  = lmList[32][1:3]
                
            
                # touch = []
                # cur_time = time.time()

                # for i in range(len(point_position)):
                #     Time_left = int(point_time[i] - cur_time)
                #     cir_x,cir_y = point_position[i][:]
                #     if (point_field_left[i][0] < right_wrist_x < point_field_right[i][0] and point_field_left[i][1] < right_wrist_y < point_field_right[i][1])\
                #     or (point_field_left[i][0] < left_wrist_x <  point_field_right[i][0] and point_field_left[i][1] < left_wrist_y < point_field_right[i][1])\
                #     or (point_field_left[i][0] < right_ankle_x <  point_field_right[i][0] and point_field_left[i][1] < right_ankle_y < point_field_right[i][1])\
                #     or (point_field_left[i][0] < left_ankle_x <  point_field_right[i][0] and point_field_left[i][1] < left_ankle_y < point_field_right[i][1])\
                #     or (point_field_left[i][0] < right_foot_x <  point_field_right[i][0] and point_field_left[i][1] < right_foot_y < point_field_right[i][1])\
                #     or (point_field_left[i][0] < left_foot_x <  point_field_right[i][0] and point_field_left[i][1] < left_foot_y < point_field_right[i][1]):
                        

                #         touch.append(i)
                #                               # game_round = 0
                #         # game_level = 0
                #         # circle_count = [1,2,3,4,5]
                #         # point_count = [2,3,4,5,6]

                #         score += 3
                          
                #         score_show_Time = np.append(score_show_Time, np.array([[time.time() + 0.3, cir_x, cir_y,point_count,1]]), axis=0)
                        
                #     else:   
                #         # 255 20 147
                #         # 0,255,255
                #         cv2.circle(img, (int(cir_x),int(cir_y)), 20, (0,255,255), cv2.FILLED)
                #         cv2.circle(img, (int(cir_x),int(cir_y)), 25, (50,205,50), 2) 
                #         cv2.putText(img, str(Time_left+1), (int(cir_x-7),int(cir_y+7)), cv2.FONT_HERSHEY_DUPLEX, 0.7,(255 ,0 ,0), 2)

                # point_field_left  = np.delete(point_field_left,touch,axis = 0)
                # point_field_right = np.delete(point_field_right,touch,axis = 0)
                # point_position = np.delete(point_position,touch,axis = 0) 
                # point_time = np.delete(point_time,touch) 
                

         
                    
                #----------------------------
                #結束三條命
        if set_count > 50 and FTime - cTime < 0:
            Finish = True    
            #分數框           
            cv2.rectangle(img,(230,185),(410,290),(38,71,139),10)#34 139 34#	139 71 38
            cv2.rectangle(img,(230,185),(410,290),(155 ,211 ,255), cv2.FILLED)#255 211 155
            cv2.putText(img, "Score:", (275, 220), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0,0,0), 2)#24 116 205
            cv2.putText(img, str(score), (260, 270), cv2.FONT_HERSHEY_DUPLEX, 1.5, (0,0,0), 2)
            
            #繼續框
            cv2.rectangle(img,(80,70),(240,120),(38,71,139),10)#34 139 34#	139 71 38
            cv2.rectangle(img,(80,70),(240,120),(155 ,211 ,255), cv2.FILLED)#255 211 155
            cv2.putText(img, "continue", (95, 105), cv2.FONT_HERSHEY_DUPLEX, 1, (0,55,205), 2)#24 116 205
            
            #結束框
            cv2.rectangle(img,(400,70),(560,120),(38,71,139),10)#34 139 34#	139 71 38
            cv2.rectangle(img,(400,70),(560,120),(155 ,211 ,255), cv2.FILLED)#255 211 155
            cv2.putText(img, "Menu", (438, 105), cv2.FONT_HERSHEY_DUPLEX, 1, (0,55,205), 2)#205 55 0
            
            #提示語
            cv2.rectangle(img,(100,340),(540,430),(38,71,139),10)#34 139 34#	139 71 38
            cv2.rectangle(img,(100,340),(540,430),(155 ,211 ,255), cv2.FILLED)#255 211 155
            cv2.putText(img, "Put your hand in the box and", \
                        (120, 375), cv2.FONT_HERSHEY_DUPLEX, 0.8, (139,139,139), 2)#24 116 205
            cv2.putText(img, "choose to continue or leave", \
                        (115, 415), cv2.FONT_HERSHEY_DUPLEX, 0.9, (139,139,139), 2)#24 116 205
            if len(lmList) != 0:
                right_wrist_x,right_wrist_y = lmList[19][1:3]
                left_wrist_x ,left_wrist_y  = lmList[20][1:3]
                
  
                if (80 < right_wrist_x < 240 and 70 < right_wrist_y < 120)\
                or (80 < left_wrist_x <  240 and 70 < left_wrist_y < 120):
                    continue_count+= 1
                    leave_count = 0
                
                elif (400 < right_wrist_x < 560 and 70 < right_wrist_y < 120)\
                or (400 < left_wrist_x <  560 and 70 < left_wrist_y < 120):
                    leave_count+= 1
                    continue_count = 0
                else:
                    continue_count = 0
                    leave_count = 0
                
                    
                leave_bar = np.interp(leave_count, (0, 50), (120, 70))  
                leave_per= np.interp(leave_count, (0, 50), (0, 100))
                
                continue_bar = np.interp(continue_count, (0, 50), (120, 70))
                continue_per= np.interp(continue_count, (0, 50), (0, 100))
                
                cv2.rectangle(img, (80,int(continue_bar)),(240,120), (38,71,139), cv2.FILLED)
                cv2.rectangle(img, (400,int(leave_bar)),(560,120), (38,71,139), cv2.FILLED)
            
            if leave_per == 100:
                break
            if continue_per == 100:
                set_count = 0
                score = 0
                continue_count = 0
                leave_count = 0
                point_position = np.empty((0,2))
                point_field_left = np.empty((0,2))
                point_field_right = np.empty((0,2))
                point_time = np.array([])
                Finish = False
            #cv2.rectangle(img, (10,50), (int(bar), 70), color, cv2.FILLED)
   
        

        if use_Flask:
            q_flask.put(img)
        else:
            cv2.imshow("GAME",img)
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
        
    return score
    
    # cv2.destroyAllWindows()
if __name__ == '__main__':   
    cap = cv2.VideoCapture(0)
    #cap = cv2.VideoCapture("./input/25.mp4")
    use_Flask,use_socket,video_save = False,False,True
  
    q_flask = Queue()
    q_all = Queue()
    gaming_3_start(cap,use_Flask,use_socket,q_flask,q_all)
    cap.release()  
    cv2.destroyAllWindows()