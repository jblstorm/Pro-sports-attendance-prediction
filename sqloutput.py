######## book table 출럭######
import pymysql
import pprint

#전역변수 선언
con,cur=None,None
data1,data2,data3,data4="","","",""
row=None

#main code
conn=pymysql.connect(port=3306,host='127.0.0.1',user='root' ,password='root',db='madang',charset='utf8')
cur=conn.cursor()

cur.execute("SELECT * FROM madang.book;")

print("bookid    bookname    publisher     price")
print('------------------------------------------------')

while True:
    row = cur.fetchone()
    if row == None:
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("%5s  %5s   %5s    %7s" % (data1, data2, data3, data4))

conn.close()