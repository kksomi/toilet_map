
import pymysql
from database import connection

def getlocation():
    conn=connection.get_connection()
    sql='''select toilet_idx,TNAME,LATI,LONGTI,ADDR_DONG
           from toilet_info
        '''

    cursor=conn.cursor()
    cursor.execute(sql)
    row=cursor.fetchall()
    data_list=[]

    for obj in row:
        data_dic={
            'toilet_idx':obj[0],
            'TNAME':obj[1],
            'LATI':obj[2],
            'LONGTI':obj[3],
            'ADDR_DONG':obj[4]
        }
        data_list.append(data_dic)


    conn.close()
    return data_list

def gettoiletidx(toilet_idx):
    conn = connection.get_connection()
    sql = '''select toilet_idx,TNAME,LATI,LONGTI,ADDR_DONG
               from toilet_info
               where toilet_idx=%s
        '''

    cursor = conn.cursor()
    cursor.execute(sql,toilet_idx)
    row = cursor.fetchall()
    data_list = []

    for obj in row:
        data_dic = {
            'toilet_idx': obj[0],
            'TNAME': obj[1],
            'LATI': obj[2],
            'LONGTI': obj[3],
            'ADDR_DONG': obj[4]
        }
        data_list.append(data_dic)

    conn.close()
    return data_list