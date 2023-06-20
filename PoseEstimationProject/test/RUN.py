from QRCODE import detect
from connect_mssql import get_list,change_user,insert_sport_count
from Fitness_detect import Fitness_detect
import time
#from AI_train_on_flask import gen

if __name__ == '__main__':
    camera = 0
    
    while True:
        #獲取所有使用者
        user_list = get_list()
        account_list = user_list.values()
        #讀取使用者qrcode
        Account = detect(account_list)
        #Account ="candykucc"
        #修改使用者狀態
        if Account != "":
            change_user(Account,"True")
            time.sleep(20)
            #開啟姿態辨識
            ID = list(user_list.keys())[list(user_list.values()).index(Account)]
            
            #Sport1,Sport2,Sport3 = gen(Account)
            Sport1,Sport2,Sport3 = Fitness_detect(Account,camera)
            #Sport1,Sport2,Sport3 = 3,4,5
            #結果記錄到資料庫
            insert_sport_count(ID,Sport1,Sport2,Sport3)
        else:
            print("End")
            break