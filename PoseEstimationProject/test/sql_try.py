import pymssql
import time
import datetime

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

def change_user(Account,use):
    #sql="SELECT * FROM user_status"
    sql = "UPDATE user_status SET account = '%s',status = '%s' WHERE camera = 0"%(Account,use)
    cursor.execute(sql)
    
    conn.commit()
    #conn.close()

def user_status(Account):
    
    sql="SELECT * FROM user_status WHERE account = '%s'"%(Account)
    cursor.execute(sql)

    row = cursor.fetchone()
    if row[1] == "False":
        return "Finish"
    else:
        return "Still using"
    #conn.close()

def insert_sport_count(ID,Sport1,Sport2,Sport3):
    date = datetime.date.today()
    sql="SELECT * FROM Fitness_his WHERE userID = '%s' and userDate='%s'"%(ID,date)
    
    cursor.execute(sql)
    row = cursor.fetchone()
    if row != None:
        Sport1 = Sport1 +row[2]
        Sport2 = Sport2 +row[3]
        Sport3 = Sport3 +row[4]
        sql = "UPDATE Fitness_his SET userSport1 = '%s',userSport2 = '%s',userSport3 = '%s' \
            WHERE userID = '%s' and userDate='%s'"%(Sport1,Sport2,Sport3,ID,date)
        cursor.execute(sql)
        conn.commit()
    else:

        sql="INSERT INTO Fitness_his(userID,userDate,userSport1,userSport2,userSport3) \
            values(%s,'%s',%d,%d,%d)"%(ID,date,Sport1,Sport2,Sport3)
        cursor.execute(sql)
        conn.commit()
    change_user("None","False")
    
    #conn.close()

    
if __name__ == '__main__':  
    #userid = get_id()
    ID = "17"
    Sport1,Sport2,Sport3 = 1,2,3
    # while True:
    #     status = user_status(Account)
    #     #print(status)
    #     time.sleep(5)
    insert_sport_count(ID,Sport1,Sport2,Sport3)
    conn.close() 
    