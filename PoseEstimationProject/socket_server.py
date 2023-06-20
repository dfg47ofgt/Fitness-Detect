import cv2
import socket
import struct
import pickle

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')

s.bind(('192.168.0.110',10087))

print('Socket bind complete')
s.listen(10)
print('Socket now listening')

conn,addr=s.accept()

data = b""
payload_size = struct.calcsize("L")

while True:
    while len(data) < payload_size:
        incomingData = conn.recv(4096)
        data += incomingData
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0]
    while len(data) < msg_size:
        data += conn.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    ###
    frame=pickle.loads(frame_data)
    #frame = np.array(frame)
    print(frame)
    
    #print(len(frame))#[len(a) for a in my_tuple_2d]
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):    
        s.close()
        break
# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()