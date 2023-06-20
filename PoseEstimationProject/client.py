import cv2
import socket
import struct
import pickle


cap=cv2.VideoCapture(0)
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('192.192.156.46',10100))
while(cap.isOpened()):
    ret,frame=cap.read()
    data = pickle.dumps(frame) ### new code
    
    clientsocket.sendall(struct.pack("L", len(data))+data)
    cv2.imshow("Image",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
