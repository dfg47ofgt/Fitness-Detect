import cv2
import time
from flask import Flask, render_template, Response
from werkzeug.serving import make_server
import threading
from queue import Queue


#影檔調整
# pixel_x = int(cap.get(3))
# pixel_y = int(cap.get(4))
# print(pixel_x,pixel_y)
# resize = 1

app = Flask("Fitness_detect")
@app.route('/')  # 主页
def index():
    # jinja2模板，具体格式保存在index.html文件中
    return render_template('Preview.html')

def gen():
    while True:
        if q.qsize() > 0:
            img = q.get()
            imgs = cv2.resize(img,(0,0),fx=0.90,fy=0.90)
            frame = cv2.imencode('.jpg', imgs)[1].tobytes()
            yield (b'--frame\r\n'
                      b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')        
            

@app.route('/video_feed')# 这个地址返回视频流响应
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')   

class ServerThread(threading.Thread):

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
    server = ServerThread(app)
    server.setDaemon(True)
    server.start()
    print("start system")

def stop_server():
    global server
    
    server.shutdown()
    print("End system")

if __name__ == '__main__':
    q = Queue() # 佇列
    start_server()
    
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('frame', frame)
            q.put(frame)
            print(q.qsize())
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                cap.release()
                break
        else:
            break
    server.shutdown()
    print("finish movie")
    
    # time.sleep(5)
    # stop_server()
    

    # 
    # stop_server()
    
    
