from QRCODE import detect
from connect_mssql import get_list,change_user,insert_sport_count,insert_game_score
from Fitness_detect import Fitness_detect
from choose_game import game_main_page
from queue import Queue
from flask import Flask, render_template, Response
from werkzeug.serving import make_server
import threading
import socket
import struct
import pickle
import cv2
import time

#建立flask server
app = Flask(__name__)
@app.route('/')  # 主页
def index():
    # jinja2模板，具体格式保存在index.html文件中
    return render_template('Preview.html')

#影像輸出至video_feed
def gen():
    img = cv2.imread("./input/white.jpg")
    counting = 0
    while True:
        if q_flask.qsize() > 0:
            counting = 0
            img = q_flask.get()
        else:
            counting += 1
            
        if counting >= 50:
            img = cv2.imread("./input/white.jpg")
            time.sleep(3)

        imgs = cv2.resize(img,(0,0),fx=1.3,fy=1.3)
        frame = cv2.imencode('.jpg', imgs)[1].tobytes()
        yield (b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')    
     
            

@app.route('/video_feed')# 这个地址返回视频流响应
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')   

#新增一個thread負責處理flaskserver
class FlaskServerThread(threading.Thread):

    def __init__(self, app):
        threading.Thread.__init__(self)
        #建立在本機ip上，port口為5000
        self.srv = make_server('0.0.0.0', 5000,app)
        self.ctx = app.app_context()
        self.ctx.push()

 
    def run(self):
        self.srv.serve_forever()
    
    
    def shutdown(self):
        self.srv.shutdown()

#啟動flask server
def start_server():
    global server
    server = FlaskServerThread(app)
    server.setDaemon(True)
    server.start()
    print("start flask system")

#停止flask server
def stop_server():
    global server
    server.shutdown()
    print("End flask system")


#新增一個thread 負責處理接收使用者影像
class WebSocketThread(threading.Thread):

    def __init__(self,q2):
        threading.Thread.__init__(self)
        self.q2 = q2
        self.s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.doing = False
        print('Socket created')
        #绑定地址為本機ip，port口為10100
        self.s.bind(('192.168.50.87',10087))
        print('Socket bind complete')

    def run(self):
        #一次只接收一個使用者的影像輸入
        self.s.listen(1)
        print('Socket now listening')
 
        
        conn,addr= self.s.accept()
        self.doing = True
        
        #收到影像封包後，將其解壓縮，並放入q_all這個queue讓後續做影像處理
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
            frame=pickle.loads(frame_data)
            q_all.put(frame)
            
    def stop(self):
        self.s.close()
        self.doing = False
        print("End")

#啟動WebSocket
def start_WebSocket():
    global websocket
    websocket = WebSocketThread(q_all)
    websocket.start()
    print("start WebSocket system")
    
#結束WebSocket
def stop_WebSocket():
    global websocket
    websocket.stop()
    #server.shutdown()
    print("End WebSocket system")
if __name__ == '__main__':
    #使用flask 、websocket、辨識影像儲存
    use_Flask = True
    use_socket = False
    video_save = True
    
    #建立Queue
    q_flask = Queue()
    q_all = Queue()
    camera = 0
    
    #啟用FLASK、WebSocket
    if use_Flask == True: 
        start_server()
    if use_socket == True:
        start_WebSocket()
    while True:
        
        q_all.queue.clear() # 佇列
        #去資料庫獲取所有使用者
        user_list = get_list()
        
        #account_list = user_list.values()
        account_list = list(user_list.values())
        
        print(account_list)
        account_game_list = [i+'-GAME' for i in account_list]
        
        #呼叫QRCODE程序
        Account_index,mode = detect(account_list,account_game_list,use_socket,q_all)
        print(Account_index)
        if Account_index != None:
            Account = account_list[Account_index]
            print("Account",Account)
            print("Mode",mode)
            #修改使用者狀態
            change_user(Account,"True")
            #獲取該使用者ID
            ID = list(user_list.keys())[list(user_list.values()).index(Account)]
            
            if mode == "fit":
                #開啟姿態辨識
                Sport1,Sport2,Sport3,Sport4,date = Fitness_detect(use_Flask,use_socket,video_save,Account,camera,q_flask,q_all,ID)
                #結果記錄到資料庫
                insert_sport_count(ID,Sport1,Sport2,Sport3,Sport4,date)
                change_user(Account,"False")
            if mode == "game":
                best_score_game1,best_score_game2,best_score_game3 = game_main_page(ID,use_Flask,use_socket,q_flask,q_all)
                insert_game_score(ID,best_score_game1,best_score_game2,best_score_game3)
        else:
            #結束FLASK與WebSocket
            #change_user(Account,"False")
            if use_Flask == True:
                stop_server()
            if use_socket == True:
                stop_WebSocket()
            print("End Fitness Detect!")
            break