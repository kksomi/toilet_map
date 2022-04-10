import pymysql


DBHOST = 'remotemysql.com'
DBUSER = '7fX80xggfM'
DBPASS = 'Py9RiJ8d77'
DBNAME = '7fX80xggfM'

# 데이터베이스에 접속해서 객체를 번환하는 함수
def get_connection() :
    conn = pymysql.connect(host=DBHOST, user=DBUSER,
                password=DBPASS, db=DBNAME,
                charset='utf8')
    return conn


