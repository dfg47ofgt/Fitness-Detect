# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 13:36:01 2021

@author: User
"""
from queue import Queue
from QRCODE2 import detect
# account_list =["candykucc"]
# Account = detect(account_list)
import threading
import cv2
import socket
import struct
import pickle
import time


class WebSocketThread(threading.Thread):

    def __init__(self,q2):
        threading.Thread.__init__(self)
        self.q2 = q2
        self.s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.doing = False
        print('Socket created')
        
        self.s.bind(('192.168.0.110',10087))
        
        print('Socket bind complete')

    def run(self):
        self.s.listen(10)
        print('Socket now listening')
 
        
        conn,addr= self.s.accept()
        self.doing = True
        print(addr)
        ### new
        data = b""
        payload_size = struct.calcsize("L")
        while self.doing == True:
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
            #print(frame)
            #q2.put(frame)
            
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):    
                self.s.close()
                break
        # 關閉所有 OpenCV 視窗
        cv2.destroyAllWindows()
    def stop(self):
        self.s.close()
        self.doing = False
        print("End")


def start_WebSocket():
    global websocket
    websocket = WebSocketThread(q2)
    websocket.start()

def stop_WebSocket():
    global websocket
    websocket.stop()
    #server.shutdown()
    print("End system")
    

if __name__ == '__main__':
    global q2
    q2 = Queue()
    start_WebSocket()
    account_list =["candykucc"]
    #Account = detect(account_list,q2)
    # time.sleep(10)
    # stop_WebSocket()
    
