# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 16:51:08 2021

@author: User
"""

#Extreme Challenge
#Limited time Challenge


#pixel_x = 640
#pixel_y = 480
import cv2
import PoseModule as pm
import numpy as np
from queue import Queue

from gaming_Limited_time import gaming_1_start
from gaming_Extreme import gaming_2_start
from gaming_Fitness import gaming_3_start
#from connect_mssql import get_game_score



def game_main_page(ID,use_Flask,use_socket,q_flask,q_all):
    cap = None
    detector = pm.poseDetector()
    if use_socket == False:
        #cap = cv2.VideoCapture("./input/25.mp4")
        cap = cv2.VideoCapture(0)
        pixel_x = int(cap.get(3))
        pixel_y = int(cap.get(4))
        print(pixel_x,pixel_y)
    if use_Flask == False:
        cv2.namedWindow("GAME")
    
    game1_count = 0
    game2_count = 0
    game3_count = 0
    game1_per = 0
    game2_per = 0
    game3_per = 0
    
    exit_per = 0
    exit_count = 0
    #best_score_game1,best_score_game2,best_score_game3 = get_game_score(ID)
    best_score_game1,best_score_game2,best_score_game3 = 0,0,0
    while True:
        if use_socket:
            img = q_all.get()
        else:
            success, img = cap.read()
    
        img = cv2.flip(img,1)
        img = detector.findPose(img)
        img = detector.DrawPose(img, False)
        lmList = detector.findPosition(img, False)
        
        
        #遊戲1框 : 限時
        cv2.rectangle(img,(40,20),(200,180),(38,71,139),10)#34 139 34#	139 71 38
        cv2.rectangle(img,(40,20),(200,180),(155 ,211 ,255), cv2.FILLED)#255 211 155
        cv2.putText(img, "Best:", (44, 62), cv2.FONT_HERSHEY_DUPLEX, 1, (34,139,34), 2)#34 139 34
        cv2.putText(img, str(best_score_game1), (120, 62), cv2.FONT_HERSHEY_DUPLEX, 1, (34,139,34), 2)#34 139 34
        cv2.putText(img, "Limited ", (60, 105), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0), 2)
        cv2.putText(img, "time", (82, 137), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0), 2) 
        cv2.putText(img, "Challenge", (44, 170), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0), 2)  
        
        
            
        #遊戲2框 : 極限
        cv2.rectangle(img,(240,20),(400,180),(38,71,139),10)#34 139 34#	139 71 38
        cv2.rectangle(img,(240,20),(400,180),(155 ,211 ,255), cv2.FILLED)#255 211 155
        cv2.putText(img, "Best:", (244, 62), cv2.FONT_HERSHEY_DUPLEX, 1, (34,139,34), 2)#34 139 34
        cv2.putText(img, str(best_score_game2), (320, 62), cv2.FONT_HERSHEY_DUPLEX, 1, (34,139,34), 2)#34 139 34
        cv2.putText(img, "Extreme", (255, 115), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0), 2)#24 116 205
        cv2.putText(img, "Challenge", (243, 160), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0), 2)
        
       
        #遊戲3框 : 運動
        cv2.rectangle(img,(440,20),(600,180),(38,71,139),10)#34 139 34#	139 71 38
        cv2.rectangle(img,(440,20),(600,180),(155 ,211 ,255), cv2.FILLED)#255 211 155
        cv2.putText(img, "Best:", (444, 62), cv2.FONT_HERSHEY_DUPLEX, 1, (34,139,34), 2)#34 139 34
        cv2.putText(img, str(best_score_game3), (520, 62), cv2.FONT_HERSHEY_DUPLEX, 1, (34,139,34), 2)#34 139 34
        cv2.putText(img, "Fitness", (465, 115), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0), 2)#24 116 205
        cv2.putText(img, "Challenge", (443, 160), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0), 2)
        
        
        
        #提示語
        cv2.rectangle(img,(100,340),(540,430),(38,71,139),10)#34 139 34#	139 71 38
        cv2.rectangle(img,(100,340),(540,430),(155 ,211 ,255), cv2.FILLED)#255 211 155
        cv2.putText(img, "Put your hand in the box to", \
                    (120, 375), cv2.FONT_HERSHEY_DUPLEX, 0.8, (139,139,139), 2)#24 116 205
        cv2.putText(img, "choose The GameMode", \
                    (140, 415), cv2.FONT_HERSHEY_DUPLEX, 0.9, (139,139,139), 2)#24 116 205
            
        #離開
        cv2.rectangle(img,(270,220),(370,280),(0,0,0),10)#34 139 34#	139 71 38
        cv2.rectangle(img,(270,220),(370,280),(19 ,69 ,139), cv2.FILLED)#255 211 155
        cv2.putText(img, "EXIT", \
                    (295, 257), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0,0,0), 2)#24 116 205
      
            
        if len(lmList) != 0:
            
            right_wrist_x,right_wrist_y = lmList[19][1:3]
            left_wrist_x ,left_wrist_y  = lmList[20][1:3]
            
  
            if (40 < right_wrist_x < 200 and 20 < right_wrist_y < 180)\
            or (40 < left_wrist_x <  200 and 20 < left_wrist_y < 180):
                game1_count+= 1
                game2_count = 0
                game3_count = 0
                exit_count  = 0 
            
            elif (240 < right_wrist_x < 400 and 20 < right_wrist_y < 180)\
            or (240 < left_wrist_x <  400 and 20 < left_wrist_y < 180):
                game2_count+= 1
                game1_count = 0
                game3_count = 0
                exit_count  = 0
                
            elif (440 < right_wrist_x < 600 and 20 < right_wrist_y < 180)\
            or (440 < left_wrist_x <  600 and 20 < left_wrist_y < 180):
                game3_count+= 1
                game1_count = 0
                game2_count = 0
                exit_count  = 0
           
            
            elif (270 < right_wrist_x < 370 and 220 < right_wrist_y < 280)\
            or (270 < left_wrist_x <  370 and 220 < left_wrist_y < 280):
                exit_count+= 1
                game2_count = 0
                game2_count = 0
                game3_count = 0
            else:
                game1_count = 0
                game2_count = 0
                game3_count = 0
                exit_count  = 0
                
            game1_bar = np.interp(game1_count, (0, 49), (180, 20))  
            game1_per= np.interp(game1_count, (0, 50), (0, 100))
            
            game2_bar = np.interp(game2_count, (0, 49), (180, 20))
            game2_per= np.interp(game2_count, (0, 50), (0, 100))
            
            game3_bar = np.interp(game3_count, (0, 49), (180, 20))
            game3_per= np.interp(game3_count, (0, 50), (0, 100))
            
            exit_bar = np.interp(exit_count, (0, 49), (280, 220))
            exit_per= np.interp(exit_count, (0, 50), (0, 100))
            
           
            cv2.rectangle(img, (40,int(game1_bar)),(200,180), (38,71,139), cv2.FILLED)
            cv2.rectangle(img, (240,int(game2_bar)),(400,180), (38,71,139), cv2.FILLED)
            cv2.rectangle(img, (440,int(game3_bar)),(600,180), (38,71,139), cv2.FILLED)
            cv2.rectangle(img, (270,int(exit_bar)),(370,280), (0,0,0), cv2.FILLED)
        
        
        if use_Flask:
            q_flask.put(img)
        else:
            cv2.imshow("GAME",img)
        
        if game1_per == 100:
            # cap.release()    
            # cv2.destroyAllWindows()
            game1_count = 0
            game1_per = 0
            game1_score = gaming_1_start(cap,use_Flask,use_socket,q_flask,q_all)
            if game1_score > best_score_game1:
                best_score_game1 = game1_score
            
        if game2_per == 100:
            
            game2_count = 0
            game2_per = 0
            game2_score = gaming_2_start(cap,use_Flask,use_socket,q_flask,q_all)
            if game2_score > best_score_game2:
                best_score_game2 = game2_score
        if game3_per == 100:
            
            game3_count = 0
            game3_count = 0
            game3_per = 0
            game3_score = gaming_3_start(cap,use_Flask,use_socket,q_flask,q_all)
            if game3_score > best_score_game3:
                best_score_game3 = game3_score
            #cv2.rectangle(img, (10,50), (int(bar), 70), color, cv2.FILLED)

        if cv2.waitKey(1) & 0xFF == ord('q') or exit_per == 100:
            break

    
    print('Extreme Challenge:',best_score_game1)
    print('Limited time Challenge:',best_score_game2)
    if use_socket == False:
        cap.release()
    # 關閉所有 OpenCV 視窗 
    cv2.destroyAllWindows()
    
    return best_score_game1,best_score_game2,best_score_game3
    
    

    
    #return score

if __name__ == '__main__':   
    use_Flask,use_socket,video_save = False,False,True
    q_flask = Queue()
    q_all = Queue()
    ID = 17
    best_score_game1,best_score_game2,best_score_game3  = game_main_page(ID,use_Flask,use_socket,q_flask,q_all)