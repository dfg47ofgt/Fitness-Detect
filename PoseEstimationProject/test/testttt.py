from QRCODE import detect

from Fitness_detect_flask_socket import Fit
from queue import Queue
from flask import Flask, render_template, Response
import cv2
import time
from werkzeug.serving import make_server
import threading
import socket
import struct
import pickle

app = Flask(__name__)
@app.route('/')  # 主页
def index():
    # jinja2模板，具体格式保存在index.html文件中
    return render_template('Preview.html')

# def gen():
#     while True:
#         if q_flask.qsize() > 0:
#             img = q_flask.get()
#             imgs = cv2.resize(img,(0,0),fx=0.90,fy=0.90)
#             frame = cv2.imencode('.jpg', imgs)[1].tobytes()
#             yield (b'--frame\r\n'
#                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
def gen():

    while True:       
        if RUN.streaming:
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + RUN.get_jpeg() + b'\r\n\r\n')
        else:
            img = cv2.imread("./input/white.jpg")
            frame = cv2.imencode('.jpg', img)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 
            time.sleep(1)
            

@app.route('/video_feed')# 这个地址返回视频流响应
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')   

class FlaskServerThread(threading.Thread):

    def __init__(self, app):
        threading.Thread.__init__(self)
        #self.srv = app.run(host = '0.0.0.0',port = 5000)
        self.srv = make_server('0.0.0.0', 5000,app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        self.srv.serve_forever()
        
    def shutdown(self):
        self.srv.shutdown()

def start_server():
    global server
    server = FlaskServerThread(app)
    server.setDaemon(True)
    server.start()
    print("start flask system")

def stop_server():
    global server
    server.shutdown()
    print("End flask system")

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
            #frame = np.array(frame)
            #print(frame)
            q_all.put(frame)
            #q_flask.put(frame)
            # cv2.imshow('frame',frame)
            # if cv2.waitKey(1) & 0xFF == ord('q'):    
            #     self.s.close()
            #     break
        # 關閉所有 OpenCV 視窗
        # cv2.destroyAllWindows()
    def stop(self):
        self.s.close()
        self.doing = False
        print("End")


def start_WebSocket():
    global websocket
    websocket = WebSocketThread(q_all)
    websocket.start()
    print("start WebSocket system")

def stop_WebSocket():
    global websocket
    websocket.stop()
    #server.shutdown()
    print("End WebSocket system")

if __name__ == '__main__':
    use_Flask = True
    use_socket = True
    video_save = False
    q_flask = Queue()
    q_all = Queue()
    camera = 0
    if use_Flask == True: 
        start_server()
    if use_socket == True:
        start_WebSocket()
    RUN = Fit()
    Sport1,Sport2,Sport3 = RUN.Fitness_detect(use_Flask,use_socket,video_save,"candykucc",camera,q_all,17)    
        
        