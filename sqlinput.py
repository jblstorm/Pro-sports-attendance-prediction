#pymysql 실행
import pymysql

#전역변수 선언부
conn: None
cur = None
data1, data2, data3, data4 = "", "", "", ""
create_book_table = ""


conn=pymysql.connect(host='127.0.0.1',port=3306,user='root' ,password='root',db='madang',charset='utf8')
cur=conn.cursor()





# TABLE 없을 시 CREATE
create_book_table = '''
            CREATE TABLE IF NOT EXISTS customer (
                 bookid INT NOT NULL,
                   name VARCHAR(40) DEFAULT NULL,
                   publisher varchar(50) DEFAULT NULL,
                   price varchar(20) DEFAULT NULL,
                   PRIMARY KEY (bookid)
            );
        '''
cur.execute(create_book_table)
# customer TABLE 에 Enter 입력시까지 한 행씩 데이터 입력
while True :
    data1=input('book.bookid ==>')
    break;
data2 = input('book.name ==>')
data3 = input('book.publisher==>')
data4 = input("book.price ==>")




sql = "INSERT INTO book VALUES('" + data1 + "','" + data2 + "','" + data3 + "','" + data4 + "')"
cur.execute(sql)




#mysql 서버 반영
conn.commit()
# DB 연결 닫기
conn.close()




