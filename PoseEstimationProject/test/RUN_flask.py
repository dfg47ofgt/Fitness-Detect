# from QRCODE import detect
# from connect_mssql import get_list,change_user,insert_sport_count
# from Fitness_detect_flask import Fitness_detect
# from queue import Queue
from flask import Flask, render_template, Response
import cv2
from werkzeug.serving import make_server
import threading
import time


app = Flask("Fitness_detect")
@app.route('/')  # 主页
def index():
    # jinja2模板，具体格式保存在index.html文件中
    return render_template('Preview.html')

# def gen():
#     counting = 0
#     while True:
#         if q.qsize() > 0:
            
#             counting = 0
#             img = q.get()
#             imgs = cv2.resize(img,(0,0),fx=0.90,fy=0.90)
#             frame = cv2.imencode('.jpg', imgs)[1].tobytes()
#             yield (b'--frame\r\n'
#                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
#         else:
#             counting += 1
#             print("dd")
#         if counting > 300:
#             print("sleep")
#             time.sleep(3)
      
            
def gen():
    img = cv2.imread("./input/white.jpg")
    counting = 0
    # while True:
    #     print("counting",counting)
    #     if q.qsize() > 0:
    #         print("ds")
    #         counting = 0
    #         img = q.get()
    #     else:
            
    #         counting += 1
    #     if counting >= 50:
    #         img = cv2.imread("./input/white.jpg")
    #         time.sleep(3)

    imgs = cv2.resize(img,(0,0),fx=0.7,fy=0.7)
    frame = cv2.imencode('.jpg', imgs)[1].tobytes()
    yield (b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


        
        
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
    print("start system")

def stop_server():
    global server
    #server.close()
    server.shutdown()
    print("End system")



if __name__ == '__main__':
    camera = 0
    start_server()
    # while True:
    #     global q
    #     q = Queue() # 佇列
    #     #獲取所有使用者
    #     user_list = get_list()
    #     account_list = user_list.values()
    #     #讀取使用者qrcode
    #     Account = detect(account_list)
    #     print(Account)
    #     #Account ="candykucc"
    #     #修改使用者狀態
    #     if Account != "":
    #         change_user(Account,"True")
    #         #開啟姿態辨識
    #         ID = list(user_list.keys())[list(user_list.values()).index(Account)]
    #         #Sport1,Sport2,Sport3 = gen(Account)
    #         Sport1,Sport2,Sport3 = Fitness_detect(Account,camera,q)
    #         #Sport1,Sport2,Sport3 = 3,4,5
    #         #結果記錄到資料庫
    #         insert_sport_count(ID,Sport1,Sport2,Sport3)
    #     else:
    #         stop_server()
    #         print("End")
    #         break