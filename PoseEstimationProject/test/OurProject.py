import cv2
import time
import PoseModule as pm

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('./input/3.mp4')
pTime = 0
detector = pm.poseDetector()
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
out = cv2.VideoWriter('./output/test.avi', fourcc,25.0,(int(cap.get(3)),int(cap.get(4))))
while True:
    sucess, img = cap.read()
    img = detector.findPose(img)
    #lmList = detector.findPosition(img,draw=False)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        print(lmList)
    #print(lmList[14])
    #cv2.circle(img, (lmList[14][1],lmList[14][2]), 10, (255,0,255), cv2.FILLED)
    out.write(img)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    cv2.putText(img, str(int(fps)),(70,50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
    
    cv2.imshow('Image', img)
    
    #cv2.waitKey(1)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()
