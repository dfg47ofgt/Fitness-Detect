import cv2
import mediapipe as mp
import time
import math
import numpy as np

class poseDetector():
    
    def __init__(self, mode= False,smooth = True,model_complexity=2,
                 enable_segmentation=False,smooth_segmentation=True,detectionCon=0.3, trackCon=0.5):
        
        self.mode = mode
        self.model_complexity = model_complexity
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.enable_segmentation= enable_segmentation
        self.smooth_segmentation = smooth_segmentation
        
        
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode,self.model_complexity,self.smooth,self.enable_segmentation,
                                      self.smooth_segmentation,self.detectionCon,self.trackCon)
        self.pose = self.mpPose.Pose()
              
               

    
    def findPose(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results =  self.pose.process(imgRGB)
        return img
    
    def DrawPose(self, img, draw=True):
        if draw:
            self.mpDraw.draw_landmarks(img , self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        #self.mpDraw.plot_landmarks(self.results.pose_world_landmarks, self.mpPose.POSE_CONNECTIONS)
        
        return img
    
    def findPosition(self, img, draw=True):
        self.lmList = []
        if self.results.pose_landmarks:
            #print(self.results.pose_landmarks)
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                #print(id,lm.visibility)
                
                cx, cy,cz,vis = int(lm.x * w) , int(lm.y * h) ,int(lm.z * w), lm.visibility
                self.lmList.append([id, cx, cy,cz,vis])
                #print(self.lmList[:][:])
                
                if draw:
                    cv2.circle(img, (cx,cy), 5, (255,0,0), cv2.FILLED)
        return self.lmList
                   
    def Face(self):
        #Face = ""
        left_side = 0
        right_side = 0
        for i in range(13,32,2):
            left_side += self.lmList[i][-1]
        for i in range(14,33,2):
            right_side += self.lmList[i][-1]
        
        #print("\nLeft:%.2f"%left_side)
        #print("Right:%.2f"%right_side)
        if right_side > left_side:
            self.Facee = "R"
            return self.Facee
        else:
            self.Facee = "L"
            return self.Facee
        
    def point(self, img, p1,draw= True):
        #Get the Landmarks
        x1 , y1 = self.lmList[p1][1:3]
        #Draw
        if draw:
            cv2.circle(img, (x1,y1), 5, (0,255,0), cv2.FILLED)
    
    def findAngle(self, img, p1, p2, p3, draw= True):
        #33 腳底中間點
        #34 是33往外延伸點
        #35 骨盆中間點
        #Get the Landmarks
        x1 , y1 = self.lmList[p1][1:3]
        
        if p2 == 33:
            if self.Facee == "R":
                x2 = int((self.lmList[27][1] + self.lmList[28][1]) / 2)
                y2 = self.lmList[28][2]
            else:
                x2 = int((self.lmList[27][1] + self.lmList[28][1]) / 2)
                y2 = self.lmList[27][2]
        elif p2 == 35:
            x2 = int((self.lmList[24][1] + self.lmList[23][1]) / 2)
            y2 = int((self.lmList[24][2] + self.lmList[23][2]) / 2)
          
        else:
            x2 , y2 = self.lmList[p2][1:3]
        
        if p3 == 34:
            #x3 , y3 = self.lmList[p2][1:3]
            x3 , y3 = x2 , y2
            if self.Facee == "R":
                x3 = x3 + 300
             
            else: 
                x3 = x3 - 300
                
 
        else:
            x3 , y3 = self.lmList[p3][1:3]
        # Calculate the Angle
        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                             math.atan2(y1 - y2, x1 - x2))
        
        if angle < 0:
            angle += 360
            
        if angle > 180:
            angle = 360 - angle
        
        #Draw
        if draw:
            cv2.line(img, (x1,y1),(x2,y2),(255,255,255),3)
            cv2.line(img, (x3,y3),(x2,y2),(255,255,255),3)
            cv2.circle(img, (x1,y1), 10, (0,0,255), cv2.FILLED)
            cv2.circle(img, (x1,y1), 15, (0,0,255), 2)
            cv2.circle(img, (x2,y2), 10, (0,0,255), cv2.FILLED)
            cv2.circle(img, (x2,y2), 15, (0,0,255), 2)
            cv2.circle(img, (x3,y3), 10, (0,0,255), cv2.FILLED)
            cv2.circle(img, (x3,y3), 15, (0,0,255), 2)
            cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50),
                       cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        
        return angle
    def findAngle3D(self, img, p1, p2, p3, draw= True):
        #33 腳底中間點
        #34 是33往外延伸點
        #35 骨盆中間點
        #Get the Landmarks
        x1 , y1 , z1= self.lmList[p1][1:4]
        
        # if p2 == 33:
        #     if self.Facee == "R":
        #         x2 = int((self.lmList[27][1] + self.lmList[28][1]) / 2)
        #         y2 = self.lmList[28][2]
        #     else:
        #         x2 = int((self.lmList[27][1] + self.lmList[28][1]) / 2)
        #         y2 = self.lmList[27][2]
        # elif p2 == 35:
        #     x2 = int((self.lmList[24][1] + self.lmList[23][1]) / 2)
        #     y2 = int((self.lmList[24][2] + self.lmList[23][2]) / 2)
          
        
        x2 , y2 ,z2= self.lmList[p2][1:4]
        
        # if p3 == 34:
        #     #x3 , y3 = self.lmList[p2][1:3]
        #     x3 , y3 = x2 , y2
        #     if self.Facee == "R":
        #         x3 = x3 + 300
             
        #     else: 
        #         x3 = x3 - 300
                
 
        # else:
        x3 , y3 ,z3= self.lmList[p3][1:4]
            
        x4,y4,z4 = (x1-x2),(y1-y2),(z1-z2)
        x5,y5,z5 = (x3-x2),(y3-y2),(z3-z2)

        cos = (x4*x5+ y4*y5+z4*z5 ) / (math.sqrt(x4**2+y4**2+z4**2) * (math.sqrt(x5**2+y5**2+z5**2)))
        # Calculate the Angle
        angle = math.degrees(math.acos(cos))
        
        if angle < 0:
            angle += 360
            
        if angle > 180:
            angle = 360 - angle
        
        #Draw
        if draw:
            cv2.line(img, (x1,y1),(x2,y2),(255,255,255),3)
            cv2.line(img, (x3,y3),(x2,y2),(255,255,255),3)
            cv2.circle(img, (x1,y1), 10, (0,0,255), cv2.FILLED)
            cv2.circle(img, (x1,y1), 15, (0,0,255), 2)
            cv2.circle(img, (x2,y2), 10, (0,0,255), cv2.FILLED)
            cv2.circle(img, (x2,y2), 15, (0,0,255), 2)
            cv2.circle(img, (x3,y3), 10, (0,0,255), cv2.FILLED)
            cv2.circle(img, (x3,y3), 15, (0,0,255), 2)
            cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50),
                       cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        
        return angle
    
   
    def findLen(self, img, p1, p2, draw= True):
        
        #Get the Landmarks
        x1 , y1 = self.lmList[p1][1:3]
        x2 , y2 = self.lmList[p2][1:3]
        
        # Calculate the Angle
        distance = int(math.sqrt( ((x1-x2)**2)+((y1-y2)**2)))
        
        #Draw
        if draw:
            cv2.line(img, (x1,y1),(x2,y2),(255,255,255),3)
            cv2.circle(img, (x1,y1), 4, (0,0,255), cv2.FILLED)
            cv2.circle(img, (x2,y2), 4, (0,0,255), cv2.FILLED)
            cv2.putText(img, str(distance), (x2 - 50, y2 + 50),
                       cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        return distance
def main():
    cap = cv2.VideoCapture(0)
    #cap = cv2.VideoCapture('./input/22.mp4')
    
    pTime = 0
    detector = poseDetector()
    while True:
        sucess, img = cap.read()
        img = detector.findPose(img)
        img = detector.DrawPose(img, True)
        lmList = detector.findPosition(img,False)
        if len(lmList) != 0:
            print(lmList)
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        # angle = detector.findAngle(img, 11, 23, 25,True)
        # angle = detector.findAngle(img, 12, 24, 26,True)
        # angle = detector.findAngle(img, 24, 26, 28,True)
        # angle = detector.findAngle(img, 23, 25, 27,True)
        cv2.putText(img, str(int(fps)),(70,50), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3)
        
        cv2.imshow('Image', img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # 釋放攝影機
    cap.release()

    # 關閉所有 OpenCV 視窗
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()