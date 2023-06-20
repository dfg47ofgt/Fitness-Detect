import threading
from queue import Queue
import cv2
#import time

def job():
    global q
    cv2.namedWindow("frame")
    while True:
        if q.qsize()>0:
            #print("go")
            frame = q.get()
            #print("{0}: {1}".format(i,frame))
            cv2.imshow('frame', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cv2.destroyAllWindows()
    
    
def multithreading():
    global q
    q = Queue() # 佇列
    t = threading.Thread(target = job)
    t.start()
    #cap = cv2.VideoCapture("./input/3.mp4")
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret == True:
            #cv2.imshow('frame', frame)
            q.put(frame)
            print(q.qsize())
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
        
    print("finish movie")
    
    # 對主執行緒中的每一個執行緒都執行join()
    t.join()
    
    
    cap.release()
    
if __name__ == '__main__':
    
    multithreading()
    print("end")

    
