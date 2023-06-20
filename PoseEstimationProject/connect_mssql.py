import pymssql
import time


userid={}
conn = pymssql.connect(
    server='172.22.248.10'
    , user='fitness'
    , password='abc12345'
    , database='graduation_project'
    , port='9999')
cursor = conn.cursor()

def get_list():
    
    sql="SELECT * FROM users "
    
    cursor.execute(sql)
    row = cursor.fetchone()
    while row:
        userid[row[0]]=row[1]
        #userid.append(row[1])
        #print(str(row[0])+" "+str(row[1])+" "+str(row[2]))
        row = cursor.fetchone() 
    #conn.close()
    return userid

def get_ID(Account):
    
    sql="SELECT * FROM users WHERE account = '%s'"%(Account)
    
    cursor.execute(sql)
    row = cursor.fetchone()
    ID = row[0]
    
    
    return ID

def change_user(Account,use):
    #sql="SELECT * FROM user_status"
    sql = "UPDATE user_status SET account = '%s',status = '%s' WHERE camera = 0"%(Account,use)
    cursor.execute(sql)
    
    conn.commit()
    #conn.close()

def user_status(camera):
    
    sql="SELECT * FROM user_status WHERE camera = '%s'"%(camera)
    cursor.execute(sql)

    row = cursor.fetchone()
    Account = row[2]
    if row[1] == "False":
        return "Finish",Account
    else:
        return "Using",Account
    #conn.close()

def insert_sport_count(ID,Sport1,Sport2,Sport3,Sport4,date):
    sql="SELECT * FROM Fitness_his WHERE userID = '%s' and userDate='%s'"%(ID,date)
    
    cursor.execute(sql)
    row = cursor.fetchone()
    if row != None:
        Sport1 = Sport1 +row[2]
        Sport2 = Sport2 +row[3]
        Sport3 = Sport3 +row[4]
        Sport4 = Sport4 +row[5]
        sql = "UPDATE Fitness_his SET userSport1 = '%s',userSport2 = '%s',userSport3 = '%s',userSport4 = '%s' \
            WHERE userID = '%s' and userDate='%s'"%(Sport1,Sport2,Sport3,Sport4,ID,date)
        cursor.execute(sql)
        conn.commit()
    else:
        sql="INSERT INTO Fitness_his(userID,userDate,userSport1,userSport2,userSport3,userSport4) \
            values(%s,'%s',%d,%d,%d,%d)"%(ID,date,Sport1,Sport2,Sport3,Sport4)
        cursor.execute(sql)
        conn.commit()
    change_user("None","False")
    #conn.close()

def get_game_score(ID):
    sql="SELECT * FROM user_game WHERE gameID = '%s'"%(ID)
    
    cursor.execute(sql)
    row = cursor.fetchone()
    
    if row == None:
           game_1 = 0
           game_2 = 0
           game_3 = 0
    else:
        game_1 = row[1]
        game_2 = row[2]
        game_3 = row[3]
    
    
    return game_1,game_2,game_3

def insert_game_score(ID,score1,score2,score3):
    sql="SELECT * FROM user_game WHERE gameID = '%s'"%(ID)
    
    cursor.execute(sql)
    row = cursor.fetchone()
    if row != None:
        sql = "UPDATE user_game SET Game1 = '%s',Game2 = '%s',Game3 = '%s' \
            WHERE gameID = '%s' "%(score1,score2,score3,ID)
        cursor.execute(sql)
        conn.commit()
    else:
        sql="INSERT INTO user_game(gameID,Game1,Game2,Game3) \
            values(%s,%d,%d,%d)"%(ID,score1,score2,score3)
        #print(sql)
        cursor.execute(sql)
        conn.commit()
    change_user("None","False")
    #conn.close()
    
    
if __name__ == '__main__':  
    #userid = get_id()
    Account = "A107221055"
    while True:
        userid = get_ID(Account)
        print(userid)
        #print(status)
        time.sleep(5)
    conn.close() 
    