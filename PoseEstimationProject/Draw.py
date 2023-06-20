import cv2
import numpy as np

class Draw():
    def __init__(self):
        #self.canvas = np.zeros((480,570,3),dtype="uint8")
        self.canvas = np.zeros((480,300,3),dtype="uint8")
    def drawPlot(self,count,per,bar,color,sports_posture):
        
        if sports_posture == "Left Lift":
            
            cv2.rectangle(self.canvas,(10,10),(290,94),(79 ,79 ,60), cv2.FILLED)
            
            #sport
            cv2.putText(self.canvas, "Left Lift : " , (40, 45), cv2.FONT_HERSHEY_DUPLEX,0.85, (180,180,180), 2)
            
            # Curl Count
            cv2.putText(self.canvas, str(int(count)), (180, 45), cv2.FONT_HERSHEY_DUPLEX, 0.8, (230,230,230), 2)
            # Draw Bar
            cv2.rectangle(self.canvas, (25, 63), (210, 75), color, 3)
            cv2.rectangle(self.canvas, (25, 63), (int(bar), 75), color, cv2.FILLED)
            cv2.putText(self.canvas, f'{int(per)} %', (225, 75), cv2.FONT_HERSHEY_DUPLEX, 0.6,color, 1)
            
            # cv2.rectangle(self.canvas,(15,15),(185,465),(79 ,79 ,60), cv2.FILLED)
        
            # cv2.putText(self.canvas, "Sports posture : " , (25, 55), cv2.FONT_HERSHEY_DUPLEX, 0.55, (180,180,180), 1)
            # cv2.putText(self.canvas, sports_posture , (25, 90), cv2.FONT_HERSHEY_DUPLEX, 0.7, (230,230,230), 2)
            
            # #Draw Curl Count
            # cv2.putText(self.canvas, "count : " , (25, 120), cv2.FONT_HERSHEY_DUPLEX, 0.7, (180,180,180), 1)
            # cv2.putText(self.canvas, str(int(count)), (120, 120), cv2.FONT_HERSHEY_DUPLEX, 0.7, (230,230,230), 2)
            
            # # # Draw Bar
            # cv2.rectangle(self.canvas, (80, 165), (120, 450), color, 3)
            # cv2.rectangle(self.canvas, (80, int(bar)), (120, 450), color, cv2.FILLED)
            # cv2.putText(self.canvas, f'{int(per)} %', (60, 155), cv2.FONT_HERSHEY_DUPLEX, 0.75,color, 1)
            
        if sports_posture == "Right Lift":
           
            cv2.rectangle(self.canvas,(10,104),(290,188),(79 ,79 ,60), cv2.FILLED)
            
            #sport
            cv2.putText(self.canvas, "Right Lift : " , (40, 139), cv2.FONT_HERSHEY_DUPLEX,0.85, (180,180,180), 2)
            
            # Curl Count
            cv2.putText(self.canvas, str(int(count)), (200, 139), cv2.FONT_HERSHEY_DUPLEX, 0.8, (230,230,230), 2)
            
            # Draw Bar
            cv2.rectangle(self.canvas, (25, 157), (210, 169), color, 3)
            cv2.rectangle(self.canvas, (25, 157), (int(bar), 169), color, cv2.FILLED)
            cv2.putText(self.canvas, f'{int(per)} %', (225, 169), cv2.FONT_HERSHEY_DUPLEX, 0.6,color, 1)
      
            # cv2.rectangle(self.canvas,(200,15),(370,465),(79 ,79 ,60), cv2.FILLED)
        
            # cv2.putText(self.canvas, "Sports posture : " , (215, 55), cv2.FONT_HERSHEY_DUPLEX, 0.55, (180,180,180), 1)
            # cv2.putText(self.canvas, sports_posture , (215, 90), cv2.FONT_HERSHEY_DUPLEX, 0.7, (230,230,230), 2)
            
            # #Draw Curl Count
            # cv2.putText(self.canvas, "count : " , (215, 120), cv2.FONT_HERSHEY_DUPLEX, 0.7, (180,180,180), 1)
            # cv2.putText(self.canvas, str(int(count)), (310, 120), cv2.FONT_HERSHEY_DUPLEX, 0.7, (230,230,230), 2)
            
            # # # Draw Bar
            # cv2.rectangle(self.canvas, (270, 165), (310, 450), color, 3)
            # cv2.rectangle(self.canvas, (270, int(bar)), (310, 450), color, cv2.FILLED)
            # cv2.putText(self.canvas, f'{int(per)} %', (250, 155), cv2.FONT_HERSHEY_DUPLEX, 0.75,color, 1)
        
        if sports_posture == "Squat":
            cv2.rectangle(self.canvas,(10,198),(290,282),(79 ,79 ,60), cv2.FILLED)
            
            #sport
            cv2.putText(self.canvas, "Squat : " , (40, 233), cv2.FONT_HERSHEY_DUPLEX,0.85, (180,180,180), 2)
            
            # Curl Count
            cv2.putText(self.canvas, str(int(count)), (200, 233), cv2.FONT_HERSHEY_DUPLEX, 0.8, (230,230,230), 2)
            
            # Draw Bar
            cv2.rectangle(self.canvas, (25, 251), (210, 263), color, 3)
            cv2.rectangle(self.canvas, (25, 251), (int(bar), 263), color, cv2.FILLED)
            cv2.putText(self.canvas, f'{int(per)} %', (225, 263), cv2.FONT_HERSHEY_DUPLEX, 0.6,color, 1)
            
            
            # cv2.rectangle(self.canvas,(385,15),(555,465),(79 ,79 ,60), cv2.FILLED)
        
            # cv2.putText(self.canvas, "Sports posture : " , (395, 55), cv2.FONT_HERSHEY_DUPLEX, 0.55, (180,180,180), 1)
            # cv2.putText(self.canvas, sports_posture , (395, 90), cv2.FONT_HERSHEY_DUPLEX, 0.7, (230,230,230), 2)
            
            # #Draw Curl Count
            # cv2.putText(self.canvas, "count : " , (395, 120), cv2.FONT_HERSHEY_DUPLEX, 0.7, (180,180,180), 1)
            # cv2.putText(self.canvas, str(int(count)), (490, 120), cv2.FONT_HERSHEY_DUPLEX, 0.7, (230,230,230), 2)
            
            # # Draw Bar
            # cv2.rectangle(self.canvas, (450, 165), (490, 450), color, 3)
            # cv2.rectangle(self.canvas, (450, int(bar)), (490, 450), color, cv2.FILLED)
            # cv2.putText(self.canvas, f'{int(per)} %', (430, 155), cv2.FONT_HERSHEY_DUPLEX, 0.75,color, 1)
            
        if sports_posture == "Puss up":
            
            cv2.rectangle(self.canvas,(10,292),(290,376),(79 ,79 ,60), cv2.FILLED)
            
            #sport
            cv2.putText(self.canvas, "Push up : " , (40, 327), cv2.FONT_HERSHEY_DUPLEX,0.85, (180,180,180), 2)
            
            # Curl Count
            cv2.putText(self.canvas, str(int(count)),(200, 327), cv2.FONT_HERSHEY_DUPLEX, 0.8, (230,230,230), 2)
            
            # Draw Bar
            cv2.rectangle(self.canvas, (25, 345), (210, 357), color, 3)
            cv2.rectangle(self.canvas, (25, 345), (int(bar), 357), color, cv2.FILLED)
            cv2.putText(self.canvas, f'{int(per)} %', (225, 357), cv2.FONT_HERSHEY_DUPLEX, 0.6,color, 1)
        
        if sports_posture == "Step Count":
           
           cv2.rectangle(self.canvas,(10,386),(290,470),(79 ,79 ,60), cv2.FILLED)
           
           #sport
           cv2.putText(self.canvas, "Step Count:" , (20, 435), cv2.FONT_HERSHEY_DUPLEX,0.85, (180,180,180), 2)
           
           # Curl Count
           cv2.putText(self.canvas, str(int(count)),(185, 435), cv2.FONT_HERSHEY_DUPLEX, 0.8, (230,230,230), 2)
           

            
            
        return self.canvas
    
    def drawList(self,lmList):
        
        #xyList = np.zeros((650,550,3),dtype="uint8")
        xyList = np.zeros((480,530,3),dtype="uint8")
        cv2.rectangle(xyList,(0,15),(515,465),(79 ,79 ,60), cv2.FILLED)
        cv2.putText(xyList, "X Y position : " ,(10, 45), cv2.FONT_HERSHEY_DUPLEX, 0.85, (180,180,180), 2)
        cv2.putText(xyList, str(lmList[0][0:3])+" "+str(lmList[1][0:3])+" "+str(lmList[2][0:3]), 
                    (10, 80), cv2.FONT_HERSHEY_DUPLEX, 0.65, (180,180,180), 1)
        cv2.putText(xyList, str(lmList[3][0:3])+" "+str(lmList[4][0:3])+" "+str(lmList[5][0:3]), 
                    (10, 117), cv2.FONT_HERSHEY_DUPLEX, 0.65, (180,180,180), 1)
        cv2.putText(xyList, str(lmList[6][0:3])+" "+str(lmList[7][0:3])+" "+str(lmList[8][0:3]), 
                    (10, 154), cv2.FONT_HERSHEY_DUPLEX, 0.65, (180,180,180), 1)
        cv2.putText(xyList, str(lmList[9][0:3])+" "+str(lmList[10][0:3])+" "+str(lmList[11][0:3]), 
                    (10, 191), cv2.FONT_HERSHEY_DUPLEX, 0.65, (180,180,180), 1)
        cv2.putText(xyList, str(lmList[12][0:3])+" "+str(lmList[13][0:3])+" "+str(lmList[14][0:3]), 
                    (10, 228), cv2.FONT_HERSHEY_DUPLEX, 0.65, (180,180,180), 1)
        cv2.putText(xyList, str(lmList[15][0:3])+" "+str(lmList[16][0:3])+" "+str(lmList[17][0:3]), 
                    (10, 265), cv2.FONT_HERSHEY_DUPLEX, 0.65, (180,180,180), 1)
        cv2.putText(xyList, str(lmList[18][0:3])+" "+str(lmList[19][0:3])+" "+str(lmList[20][0:3]), 
                    (10, 302), cv2.FONT_HERSHEY_DUPLEX, 0.65, (180,180,180), 1)
        cv2.putText(xyList, str(lmList[21][0:3])+" "+str(lmList[22][0:3])+" "+str(lmList[23][0:3]), 
                    (10, 339), cv2.FONT_HERSHEY_DUPLEX, 0.65, (180,180,180), 1)
        cv2.putText(xyList, str(lmList[24][0:3])+" "+str(lmList[25][0:3])+" "+str(lmList[26][0:3]), 
                    (10, 376), cv2.FONT_HERSHEY_DUPLEX, 0.65, (180,180,180), 1)
        cv2.putText(xyList, str(lmList[27][0:3])+" "+str(lmList[28][0:3])+" "+str(lmList[29][0:3]), 
                    (10, 413), cv2.FONT_HERSHEY_DUPLEX, 0.65, (180,180,180), 1)
        cv2.putText(xyList, str(lmList[30][0:3])+" "+str(lmList[31][0:3])+" "+str(lmList[32][0:3]), 
                    (10, 450), cv2.FONT_HERSHEY_DUPLEX, 0.65, (180,180,180), 1)
      
        
        return xyList     
  
    