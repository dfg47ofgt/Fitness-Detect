import time
import cv2
import os

#儲存影檔
#fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
path = './outputt'
if not os.path.isdir(path):
    os.makedirs(path)
    
Filename = path+'/'+time.strftime('%Y%m%d_%H%M%S', time.localtime())+'.avi'
out = cv2.VideoWriter(Filename,fourcc,30.0,(640,480))

cap = cv2.VideoCapture('./input/25.mp4')







while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()