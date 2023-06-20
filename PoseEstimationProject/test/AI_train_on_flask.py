import cv2
import numpy as np
import time
import PoseModule as pm
import Draw as dr
import winsound
from flask import Flask, render_template, Response
from werkzeug.serving import make_server
import math
import threading



detector = pm.poseDetector()
draw = dr.Draw()



#影檔調整
# pixel_x = int(cap.get(3))
# pixel_y = int(cap.get(4))
# print(pixel_x,pixel_y)
# resize = 1

app = Flask("Fitness_detect")
@app.route('/')  # 主页
def index():
    # jinja2模板，具体格式保存在index.html文件中
    return render_template('test.html')

def gen():
    cap = cv2.VideoCapture(0)
    #起始自訂義
    count_l_Lift,per_l_Lift,count_r_Lift,per_r_Lift,count_Squat,per_Squat = 0,0,0,0,0,0
    bar_l_Lift,bar_r_Lift,bar_Squat = 450,450,450
    color_l_Lift,color_r_Lift,color_Squat = (200, 200, 200),(200, 200, 200),(200, 200, 200)
    

    
    #起始時間
    pTime = 0
    
    #起使運動方向
    dir1 = 0
    dir2 = 0
    
    #起始準備動作偵數
    set_count = 0
    
    #起始定義位置
    strat1 = 0
    strat2 = 0
        
    #起始動作次數
    count_Squat,count_l_Lift,count_r_Lift = 0,0,0
    

    Face=""
    using = False

    #fourcc = cv2.VideoWriter_fourcc(*'XVID')
    #Filename = './output/'+time.strftime('%Y%m%d_%H%M%S', time.localtime())+'.avi'
    #out = cv2.VideoWriter(Filename,fourcc ,30.0,(1210,480))

    
    while True: 
        success, img = cap.read()
        #img = cv2.imread("./input/20.png")
        #img = cv2.resize(img, (int(pixel_x/resize),int(pixel_y/resize)))
        #img = cv2.resize(img, (640,480))

        img = detector.findPose(img)
        lmList = detector.findPosition(img, False)
        
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        
        if len(lmList) != 0:
            Face = detector.Face()
            if set_count <= 50:
                set1 = detector.findAngle(img, 14,12,24, False)
                set2 = detector.findAngle(img, 13,11,23, False)
                set3 = detector.findAngle(img, 23,24,26, False)
                set4 = detector.findAngle(img, 24,23,25, False)
                
                if 70 <= set1  and 70 <= set2  and 90 <= set3 <= 115 and 90 <= set4 <= 115:
                    img = detector.DrawPose(img, True)
                    set_count += 1
                    #print(set_count)
                else:
                    set_count = 0
                per= np.interp(set_count, (0, 50), (0, 100))
                bar = np.interp(set_count, (0, 50), (10, 200))
                
                # Draw Bar
                color = (180,180,180)
                if per > 90:
                    color = (0,255,255)
                    
                cv2.rectangle(img, (0,0), (270, 110),(79 ,79 ,60), cv2.FILLED)    
                cv2.putText(img, "fps:"+str(int(fps)), (10, 35), cv2.FONT_HERSHEY_DUPLEX, 1,
                      (200, 200, 200), 2)
                cv2.putText(img, "Get ready Pose", (10, 70), cv2.FONT_HERSHEY_DUPLEX, 1,color, 2)    	
                cv2.rectangle(img, (10, 85), (200, 100), color, 3)
                cv2.rectangle(img, (10,85), (int(bar), 100), color, cv2.FILLED)
                cv2.putText(img, f'{int(per)}%', (205, 100), cv2.FONT_HERSHEY_DUPLEX, 1,color, 1)
                if set_count == 51:  
                    winsound.Beep(440, 400)
                    strat1 = detector.findLen(img, 11,12,True)
                    strat2 = detector.findLen(img, 23,24,True)
                    using = True
                #cv2.namedWindow("Image")
                #cv2.imshow("Image", img)
                
                
            if set_count > 50:
                cv2.rectangle(img,(220,0),(420,50),(79 ,79 ,60), cv2.FILLED)
                detector.point(img, 7,False)
                detector.point(img, 8,False)
                img = detector.DrawPose(img, True)
                #cv2.putText(img, "Recording...",(10, 65), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,color, 1)
                
                #cv2.namedWindow("X Y")
                #cv2.imshow("X Y",drawList)
                
                distance1 = detector.findLen(img, 11,12,False)
                distance2 = detector.findLen(img, 23,24,False)
                per_distance1 = np.interp(distance1, (0, strat1), (0, 100))
                per_distance2 = np.interp(distance2, (0, strat2), (0, 100))
                per_distance = (per_distance1 + per_distance2) / 2
                #print("distance:",per_distance)
                
            
                
                if per_distance < 55:
                    if Face == "L":
                        cv2.putText(img, "Left_side", (245, 35), cv2.FONT_HERSHEY_DUPLEX, 1,
                                    (0,0,255), 2)
                        #per_l_Lift,per_r_Lift,per_Squat = 0,0,0
                        
                        #####################################################
                        #left lift#
                        angle = detector.findAngle(img, 11, 13, 15,False)
                        per_l_Lift = np.interp(angle, (50, 150), (100, 0))
                        bar_l_Lift = np.interp(angle, (50, 140), (165, 450))
                        
                        color_l_Lift = (200, 200, 200)
                        if per_l_Lift == 100:
                            color_l_Lift = (0,255,255)
                            if dir1 == 0:
                                count_l_Lift += 0.5
                                dir1 = 1
                        if per_l_Lift == 0:
                            color_l_Lift = (156, 156, 156)
                            if dir1 == 1:
                                count_l_Lift += 0.5
                                dir1 = 0
                        
                        #########################################################
                        
                        #left squat#
                        angle = detector.findAngle(img, 11,23,25,False)
                        per_Squat_1 = np.interp(angle, (90, 160), (100, 0))
                        bar_Squat_1 = np.interp(angle, (90, 160), (165, 450))
                        
                        angle = detector.findAngle(img, 23,25,27, False)
                        per_Squat_2 = np.interp(angle, (90, 160), (100, 0))
                        #print(per_Squat_1,per_Squat_2)
                        bar_Squat_2 = np.interp(angle, (90, 160), (165, 450))
                        #print(angle, per, bar)
                        per_Squat = (per_Squat_1 + per_Squat_2) / 2
                        bar_Squat = (bar_Squat_1 + bar_Squat_2) / 2
                        # Check for the dumbbell curls
                        color_Squat = (200, 200, 200)
                        if per_Squat == 100:
                            color_Squat = (0,255,255)
                            if dir2 == 0:
                                count_Squat += 0.5
                                dir2 = 1
                        if per_Squat == 0:
                            color_Squat = (156, 156, 156)
                            if dir2 == 1:
                                count_Squat += 0.5
                                dir2 = 0
                        
                        ############################################################
                    else:
                        cv2.putText(img, "Right_side", (245, 35), cv2.FONT_HERSHEY_DUPLEX, 1,
                                    (0,0,255), 2)
                        
                        #####################################################
                        #Right lift#
                        angle = detector.findAngle(img, 12, 14, 16,False)
                        per_r_Lift = np.interp(angle, (50, 150), (100, 0))
                        bar_r_Lift = np.interp(angle, (50, 140), (165, 450))
                        
                        color_r_Lift = (200, 200, 200)
                        if per_r_Lift == 100:
                            color_r_Lift = (0,255,255)
                            if dir1 == 0:
                                count_r_Lift += 0.5
                                dir1 = 1
                        if per_r_Lift == 0:
                            color_r_Lift = (156, 156, 156)
                            if dir1 == 1:
                                count_r_Lift += 0.5
                                dir1 = 0
                        
                        #########################################################
                        
                        #Right squat
                        angle = detector.findAngle(img, 12,24,26,False)
                        per_Squat_1 = np.interp(angle, (90, 160), (100, 0))
                        bar_Squat_1 = np.interp(angle, (90, 160), (165, 450))
                        
                        angle = detector.findAngle(img, 24,26,28, False)
                        per_Squat_2 = np.interp(angle, (90, 160), (100, 0))
                        #print(per_Squat_1,per_Squat_2)
                        bar_Squat_2 = np.interp(angle, (90, 160), (165, 450))
                        #print(angle, per, bar)
                        per_Squat = (per_Squat_1 + per_Squat_2) / 2
                        bar_Squat = (bar_Squat_1 + bar_Squat_2) / 2
                        # Check for the dumbbell curls
                        color_Squat = (200, 200, 200)
                        if per_Squat == 100:
                            color_Squat = (0,255,255)
                            if dir2 == 0:
                                count_Squat += 0.5
                                dir2 = 1
                        if per_Squat == 0:
                            color_Squat = (156, 156, 156)
                            if dir2 == 1:
                                count_Squat += 0.5
                                dir2 = 0
                        
                else:
                    if lmList[7][1:2] > lmList[8][1:2]:
                        cv2.putText(img, "Front_side", (245, 35), cv2.FONT_HERSHEY_DUPLEX, 1,
                                    (0,0,255), 2)
                        angle = detector.findAngle(img, 11,23,25, False)
                        per_Squat_1 = np.interp(angle, (100, 160), (100, 0))
                        bar_Squat_1 = np.interp(angle, (100, 160), (165, 450))
                        
                        angle = detector.findAngle(img, 23,25,27, False)
                        per_Squat_2 = np.interp(angle, (100, 160), (100, 0))
                        bar_Squat_2 = np.interp(angle, (100, 160), (165, 450))
                        angle = detector.findAngle(img, 12,24,26, False)
                        per_Squat_3 = np.interp(angle, (100, 160), (100, 0))
                        bar_Squat_3 = np.interp(angle, (100, 160), (165, 450))
                        
                        angle = detector.findAngle(img, 24,26,28, False)
                        per_Squat_4 = np.interp(angle, (100, 160), (100, 0))
                        bar_Squat_4 = np.interp(angle, (100, 160), (165, 450))
                        per_Squat = (per_Squat_1 + per_Squat_2 + per_Squat_3 + per_Squat_4) / 4
                        bar_Squat = (bar_Squat_1 + bar_Squat_2 + bar_Squat_3 + bar_Squat_4) / 4

                        color_Squat = (200, 200, 200)
                        if per_Squat == 100:
                            color_Squat = (0,255,255)
                            if dir2 == 0:
                                count_Squat += 0.5
                                dir2 = 1
                        if per_Squat == 0:
                            color_Squat = (156, 156, 156)
                            if dir2 == 1:
                                count_Squat += 0.5
                                dir2 = 0
                    else:
                        per_l_Lift,per_r_Lift,per_Squat = 0,0,0
                        cv2.putText(img, "Back_side", (245, 35), cv2.FONT_HERSHEY_DUPLEX, 1,
                                      (0,0,255), 2)
                        cv2.rectangle(img,(220,190),(420,290),(0 ,0 ,255),10)
                        cv2.rectangle(img,(220,190),(420,290),(79 ,79 ,60), cv2.FILLED)
                        cv2.putText(img, "Don't turn", (237, 227), cv2.FONT_HERSHEY_DUPLEX, 1, (255,255,255), 2)
                        cv2.putText(img, "your back!", (237, 267), cv2.FONT_HERSHEY_DUPLEX, 1, (255,255,255), 2)
                        #cv2.imshow("Image", img)
                        
                
                cv2.rectangle(img, (0,0), (120, 50),(79 ,79 ,60), cv2.FILLED)
                cv2.putText(img, "fps:"+str(int(fps)), (10, 35), cv2.FONT_HERSHEY_DUPLEX, 1,
                      (200, 200, 200), 2)
                
                canvas = draw.drawPlot(count_l_Lift,per_l_Lift,bar_l_Lift,color_l_Lift,"Left Lift")
                canvas = draw.drawPlot(count_r_Lift,per_r_Lift,bar_r_Lift,color_r_Lift,"Right Lift")
                canvas = draw.drawPlot(count_Squat,per_Squat,bar_Squat,color_Squat,"Squat")

                drawList = draw.drawList(lmList)
                
                #img = np.hstack([img,canvas,drawList])
                #out.write(img)
        else:
            cv2.rectangle(img, (0,0), (120, 50),(79 ,79 ,60), cv2.FILLED)
            cv2.putText(img, "fps:"+str(int(fps)), (10, 35), cv2.FONT_HERSHEY_DUPLEX, 1,
                      (200, 200, 200), 2)
        if using == True:
            img = np.hstack([img,canvas,drawList])
        
        # if cTime - checktime > 5:
        #     checktime = cTime
        #     status_of_use = user_status(User)
        #     print(status_of_use)
        

        #按Q或停止運動結束迴圈
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # cap = cv2.VideoCapture('./input/13.mp4')
    # while True: 
    #     success, img = cap.read()
    #     if success!=True:
    #         img = cv2.imread("./input/1.png")

        imgs = cv2.resize(img,(0,0),fx=0.7,fy=0.7)
        frame = cv2.imencode('.jpg', imgs)[1].tobytes()
        yield (b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 
        #img = cv2.imread("./input/1.png")
    count_Squat = math.floor(count_Squat)
    count_l_Lift = math.floor(count_l_Lift)
    count_r_Lift = math.floor(count_r_Lift)
    print(count_Squat)
    print(count_l_Lift)
    print(count_r_Lift)
        

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
    server.start()


def stop_server():
    global server
    server.shutdown()
    

if __name__ == '__main__':
    
    start_server()
    time.sleep(10)
    stop_server()
    

    # time.sleep(10)
    # stop_server()
    
    
