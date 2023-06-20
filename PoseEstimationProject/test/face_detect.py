import cv2
import numpy as np
import face_recognition
import pickle
import time
# from PIL import ImageGrab
start_count = 0
pTime = 0
images = []
classNames = []
detect_USER = "Unknown"
User = "None"

with open('./images_id/id/dataset_faces.dat', 'rb') as f:
	all_face_encodings = pickle.load(f)

classNames = list(all_face_encodings.keys())
encodeListKnown = np.array(list(all_face_encodings.values()))


cap = cv2.VideoCapture(0)
 
while True:
    success, img = cap.read()
    #img = captureScreen()
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
    print(detect_USER)   
    print(start_count)
     
    cv2.imshow('Webcam',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# 釋放攝影機
cap.release()
# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()