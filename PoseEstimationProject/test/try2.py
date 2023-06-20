import cv2

def job(q):
    #global q
    cv2.namedWindow("frame")
    while True:
        if q.qsize()>0:
            frame = q.get()
            #print("{0}: {1}".format(i,frame))
            cv2.imshow('frame', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cv2.destroyAllWindows()
    
