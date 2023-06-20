import cv2
import pyzbar.pyzbar as pyzbar

 
def decodeDisplay(imagex1):
    #轉為灰度影象
    #imagex1 = cv2.resize(imagex1,(640,480))
    barcodeData = ""
    gray = cv2.cvtColor(imagex1, cv2.COLOR_BGR2GRAY)
    barcodes = pyzbar.decode(gray)
    
    for barcode in barcodes:
    
    # 提取條形碼的邊界框的位置
    # 畫出影象中條形碼的邊界框
        (x, y, w, h) = barcode.rect
        cv2.rectangle(imagex1, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
        # 條形碼資料為位元組物件，所以如果我們想在輸出影象上
        # 畫出來，就需要先將它轉換成字串
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        
        # 繪出影象上條形碼的資料和條形碼型別
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(imagex1, text, (x, y - 10), cv2.FONT_HERSHEY_PLAIN,2, (0, 0, 255), 2)
        
        #向終端列印條形碼資料和條形碼型別
        #print("掃描結果==》 類別： {0} 內容： {1}".format(barcodeType, barcodeData))
    cv2.imshow("camera", imagex1)
    return barcodeData
    
def detect(account_list,account_game_list,use_socket,q):
    
    #name = ""
    index = None
    getuser =""
    mode = ""
    if use_socket == False:
        camera = cv2.VideoCapture(1)
    #cv2.namedWindow("camera")
    #camera = cv2.VideoCapture(0)
    #print(int(camera.get(3)),int(camera.get(4)))
    while True:
        # if q.qsize() > 0:
        if use_socket == True:
            frame = q.get()
        else:
            ret, frame = camera.read()

        
        getuser = decodeDisplay(frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        if getuser in account_list: 
            index = account_list.index(getuser)
            mode = "fit"
            break
        if getuser in account_game_list:
            index = account_game_list.index(getuser)
            mode = "game"
            #name = getuser
            break
        
    #camera.release()
    cv2.destroyAllWindows() 
    
    return index,mode

if __name__ == '__main__':
    q = ()
    use_socket = False
    account_list = ["A107221025"]
    detect(account_list,use_socket,q)