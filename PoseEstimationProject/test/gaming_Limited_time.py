import cv2
import time
import PoseModule as pm
import numpy as np
import random
from queue import Queue

def Feasible_position(lmList,field_left,field_right):
    left_hand_mark_x , left_hand_mark_y = lmList[15][1:3] 
    right_hand_mark_x ,  right_hand_mark_y = lmList[16][1:3] 
    game_square = np.ones(7)
    for i in range(7):
        if (field_left[i][0] < right_hand_mark_x < field_right[i][0] and field_left[i][1] < right_hand_mark_y < field_right[i][1])\
        or (field_left[i][0] < left_hand_mark_x <  field_right[i][0] and field_left[i][1] < left_hand_mark_y < field_right[i][1]):
            game_square[i] = 0  

        else: 
            game_square[i] = 1
    # print(game_square)
    
    lst = [i for i in range(len(game_square)) if game_square[i]== 1]
    
    return lst

def gaming_2_make_circle(img,position,cir_sum,field_left,field_right):
    choose_where_make = random.sample(position,cir_sum)
    
    point_position = np.empty((0,2))
    point_field_left = np.empty((0,2))
    point_field_right = np.empty((0,2))

    
    for i in choose_where_make:
        cir_x = random.randint(field_left[i][0],field_right[i][0])
        cir_y = random.randint(field_left[i][1],field_right[i][1])
        point_position = np.append(point_position,np.array([[cir_x,cir_y]]), axis = 0) 
        point_field_left = np.append(point_field_left, np.array([[cir_x-25,cir_y-25]]),axis = 0)
        point_field_right = np.append(point_field_right, np.array([[cir_x+25,cir_y+25]]), axis = 0)
    
   
    
    return point_position,point_field_left,point_field_right


def gaming_2_start(cap,use_Flask,use_socket,q_flask,q_all):
    if use_socket == False:
        #cap = cv2.VideoCapture("./input/25.mp4")
        # cap = cv2.VideoCapture(0)
        pixel_x = int(cap.get(3))
        pixel_y = int(cap.get(4))
        print(pixel_x,pixel_y)
    if use_Flask == False:
        cv2.namedWindow("GAME")
   
    
    life = 3
    
    detector = pm.poseDetector()
    
    success, img = cap.read()
    pixel_y,pixel_x = img.shape[0:2]
    
    
    pTime = 0
    set_count = 0
    success = True
    playing = False
    waiting = False
    making  = True
    Finish = False
    game_round = 0
    game_level = 0
    circle_count = [1,2,3,4,5]
    point_count = [2,3,4,5,6]
    score = 0
    score_show_Time = np.empty((0,4))
    continue_count = 0
    leave_count = 0
    back_count = 0

    

    while True:
        if use_socket:
            img = q_all.get()
        else:
            success, img = cap.read()
        
        img = cv2.flip(img,1)
        img = detector.findPose(img)
        img = detector.DrawPose(img, False)
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
                x_1 = lmList[12][1] -50
                y_1 = lmList[5][2] 
                x_2 = lmList[11][1] + 50
                y_2 = lmList[29][2] 
                
                
                topleft = [x_1,y_1]
                downright = [x_2,y_2]
                color=(255,0,0)  #蓝色
                cv2.rectangle(img,topleft, downright, color, 2)
                
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
                    left_len = detector.findLen(img, 11,19,False)
                    right_len = detector.findLen(img, 12,20,False)
                    
                    # play_left = [x_1-left_len,y_1-left_len]
                    # play_right = [x_2+right_len,y_2]
                    
                    field_left = []
                    field_right = []
                    
                    if y_1-left_len < 35:
                        top_limit = 35
                    else:
                        top_limit = y_1-left_len
                             
                    if x_1-left_len < 10:
                        left_limit = 10
                    else:
                        left_limit = x_1-left_len
                        
                    if x_2+right_len > 630:
                        right_limit = 630
                    else:
                        right_limit = x_2+right_len
                        
                        
                    field_left.append([left_limit,top_limit]) 
                    field_right.append([x_1,y_1])
                    
                    field_left.append([x_1,top_limit])
                    field_right.append([x_2,y_1])
                    
                    field_left.append([x_2,top_limit])
                    field_right.append([right_limit,y_1])
                    
                    field_left.append([left_limit,y_1])
                    field_right.append([x_1,int((y_1+y_2)/2)])
                
                    field_left.append([x_2,y_1])
                    field_right.append([right_limit,int((y_1+y_2)/2)])
                    
                     
                    field_left.append([left_limit,int((y_1+y_2)/2)])
                    field_right.append([x_1,y_2])
                    
                     
                    field_left.append([x_2,int((y_1+y_2)/2)])
                    field_right.append([right_limit,y_2])
                    
                     
                   
                    
            elif set_count > 50 and life > 0:
 
                # 生命位置
                heart_position = []
                midd = (lmList[4][1] + lmList[1][1] )/ 2
  
                heart_position.append([int(midd - 20), lmList[3][2] -40])
                heart_position.append([int(midd), lmList[3][2] -40])
                heart_position.append([int(midd + 20),lmList[3][2] -40])
  
                #畫生命
  
                for i in range(life):
                    cir_x , cir_y = heart_position[i][:]
                    cv2.circle(img, (cir_x,cir_y), 7, (0,0,255), cv2.FILLED)
                    cv2.circle(img, (cir_x,cir_y), 9, (0,0,0), 2) 

                #分數框
                #color=(0,255,255)  #蓝色
                
                cv2.rectangle(img, (0,0), (230, 50),(79 ,79 ,60), cv2.FILLED)  
                cv2.putText(img, "Score :", (10, 35), cv2.FONT_HERSHEY_DUPLEX, 1,(180,180,180), 2)    	
                cv2.putText(img, str(score), (140, 35), cv2.FONT_HERSHEY_DUPLEX, 1,(180,180,180), 2)    
                
                #關卡欄
                
                cv2.rectangle(img, (140,430), (500, 470),(149 ,175 ,205), cv2.FILLED)#205 175 149
                cv2.putText(img, "lV", (153, 460), cv2.FONT_HERSHEY_DUPLEX, 1,(38,71,139), 2)    	
                cv2.putText(img, str(game_level+1)+':', (180, 460), cv2.FONT_HERSHEY_DUPLEX, 1,(38,71,139), 2)  
                
                if game_round == 3:
                    cv2.rectangle(img,(240,440),(240+int((game_round)*80),460), (0,140,255), cv2.FILLED)#	255 140 0
                else:
                    cv2.rectangle(img,(240,440),(240+int((game_round)*80),460), (38,71,139), cv2.FILLED)
                    
                cv2.rectangle(img,(240,440),(480,460),(38,71,139),3)
       
                
                
                # 顯示7個可生成位置
                # cv2.rectangle(img,play_left, play_right, color, 2)
                # for i in range(7):
                #     cv2.rectangle(img,tuple(field_left[i][:]),tuple(field_right[i][:]), color, 2)
                
                
                
 
                #產生加分動畫
                dele = []
                for i in range(len(score_show_Time)):
                    c_time = time.time()
                    if score_show_Time[i][0] - c_time > 0:
                        cv2.putText(img, '+'+str(int(score_show_Time[i][3])), (int(score_show_Time[i][1])-15,int(score_show_Time[i][2])), cv2.FONT_HERSHEY_DUPLEX, 1.3,(71 ,130 ,255), 2)
                    else:
                        dele.append(i)
                                              
                score_show_Time  = np.delete(score_show_Time,dele,axis = 0)#刪除a的第二行。
 
                
                #獲取可產生circle位置
                position = Feasible_position(lmList,field_left,field_right)
                #--------------------
                #遊戲執行順序
                #making --> playing --> waiting --> making 輪迴 
                if making == True:
                    # game_round = 0
                    # game_level = 0
                    # circle_count = [1,2,3,4,5]
                    # point_count = [2,3,4,5,6]
                    if game_round == 3:
                        game_level += 1
                        game_round = 0
                       
                    if game_level > 4 :
                        cir_sum = circle_count[4]
                        finish_Time = time.time() + 3 - (0.2 * (game_level-3))
                    else:
                        cir_sum = circle_count[game_level]
                        finish_Time = time.time() + 3
                    
                        
                    point_position,point_field_left,point_field_right = gaming_2_make_circle(img,position,cir_sum,field_left,field_right)
                    
                    
                    making  = False
                    playing = True
                   
                    
                if playing == True:                
                    cur_time = time.time()
                    if finish_Time - cur_time > 0 and len(point_field_left) > 0:
                        Time_left = int(finish_Time - cur_time)
                        right_wrist_x,right_wrist_y = lmList[19][1:3]
                        left_wrist_x ,left_wrist_y  = lmList[20][1:3]
                    
                        touch = []
                        for i in range(len(point_position)):
                            cir_x,cir_y = point_position[i][:]
                            if (point_field_left[i][0] < right_wrist_x < point_field_right[i][0] and point_field_left[i][1] < right_wrist_y < point_field_right[i][1])\
                            or (point_field_left[i][0] < left_wrist_x <  point_field_right[i][0] and point_field_left[i][1] < left_wrist_y < point_field_right[i][1]):

                                touch.append(i)
                                                     # game_round = 0
                                # game_level = 0
                                # circle_count = [1,2,3,4,5]
                                # point_count = [2,3,4,5,6]
                                if game_level > 5:
                                    s = 6 + ((game_level-4)//2) 
                                else:
                                    s = point_count[cir_sum-1]
                                score += s
                                
                                
                                score_show_Time = np.append(score_show_Time, np.array([[time.time() + 0.3, cir_x, cir_y,s]]), axis=0)
                                
                                
                                
                                
                            
                            else:   
                               # 255 20 147
                               # 0,255,255
                                cv2.circle(img, (int(cir_x),int(cir_y)), 20, (0,255,255), cv2.FILLED)
                                cv2.circle(img, (int(cir_x),int(cir_y)), 25, (50,205,50), 2) 
                                cv2.putText(img, str(Time_left+1), (int(cir_x-7),int(cir_y+7)), cv2.FONT_HERSHEY_DUPLEX, 0.7,(255 ,0 ,0), 2)
                        

                                                    
                        point_field_left  = np.delete(point_field_left,touch,axis = 0)
                        point_field_right = np.delete(point_field_right,touch,axis = 0)
                        point_position = np.delete(point_position,touch,axis = 0) 
                    
                    else:
                        if len(point_field_left) != 0:
                            life -= 1
                        else:
                            game_round += 1
                            
                        playing = False
                        waiting = True
                        print("finish round!")
                        #設定間格時間
                        wait_Time = time.time() + 1.5
                    
                if waiting == True:
                    #print("waiting....")
                    cur_time = time.time()
                    if wait_Time - cur_time < 0:
                        cur_time = time.time()
                        waiting = False
                        making = True
                        print("new round!")
         
                    
                #----------------------------
                #結束三條命
        if life <= 0:
            playing = False
            waiting = False
            making  = True
            Finish =True
            
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
                life = 3
                set_count = 0
                score = 0
                continue_count = 0
                leave_count = 0
                game_round = 0
                game_level = 0
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
    gaming_2_start(cap,use_Flask,use_socket,q_flask,q_all)
    cap.release()  
    cv2.destroyAllWindows()