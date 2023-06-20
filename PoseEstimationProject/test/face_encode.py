import face_recognition
import pickle
import os
import cv2
import time
path = 'images_id/img'
images = []
classNames = []
myList = os.listdir(path)

print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
    print(classNames)
    

def findEncodings(images,classNames):
    encodeList = {}
    for img,name in zip(images,classNames):
        print(name)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        size = img.shape
        print(size[0:2])
        #img = cv2.resize(img, (640,480))
        encodeList[name] = face_recognition.face_encodings(img)[0]
    return encodeList



encodeListKnown = findEncodings(images,classNames)


# # ... etc ...
with open('./images_id/id/dataset_faces.dat', 'wb') as f:
    pickle.dump(encodeListKnown, f)
    
print("Finish!")