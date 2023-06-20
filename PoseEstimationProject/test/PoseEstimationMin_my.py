import cv2
import time
import mediapipe as mp
import sys
sys.path.append("..")
import PoseModule_new as pm
import Draw as dr
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()


cap = cv2.VideoCapture("./input/29.mp4")

pTime = 0
# pixel_x = int(cap.get(3))
# pixel_y = int(cap.get(4))

# pixel_x = 980
# pixel_y = 654

count_l_Lift = 0
dir1 = 0
dir2 = 0
success = True
detector = pm.poseDetector()
Face = ""
#lmList[7][1:2]
#cv2.circle(img, (cx,cy), 5, (255,0,0), cv2.FILLED)
per_l_Lift,dir_l_Lift = 0,0
start = time.time()
while True:
    #img = cv2.imread('./input/cross.jpg')
    success, img = cap.read()
    #img = cv2.resize(img, (552,739))
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    
    cv2.namedWindow("Image")
    if success:

        img = detector.findPose(img)
        img = detector.DrawPose(img, True)
        lmList = detector.findPosition(img, False)
        if len(lmList) != 0:
            angle = detector.findAngle(img, 26,24,25, True)   
            # Face = detector.Face()
            per_l_Lift = np.interp(angle, (15, 80), (100, 0))
            
            #Check for the dumbbell curls
            if per_l_Lift == 100:
                if dir_l_Lift == 0:
                    count_l_Lift += 0.5
                    dir_l_Lift = 1
            if per_l_Lift == 0:
                if dir_l_Lift == 1:
                    count_l_Lift += 0.5
                    dir_l_Lift = 0
            
            
            

            
            
            
            
            
            cv2.putText(img, "step:"+str(int(count_l_Lift)), (10, 35), cv2.FONT_HERSHEY_DUPLEX, 1,
                  (0, 0, 0), 2)
        #img = np.vstack([img,skeletion])
        cv2.namedWindow("Image")
        cv2.imshow('Image', img)
        #cv2.namedWindow("Image2")
        #cv2.imshow('Image2', skeletion)
        #cv2.imshow('skeletion', skeletion)
        #cv2.waitKey(10)
      
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break
#cap.release()    
cv2.destroyAllWindows()
end = time.time()    
