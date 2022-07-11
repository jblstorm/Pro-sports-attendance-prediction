import pymysql
from tkinter import *
from tkinter import messagebox

# 함수 선언
def insertData():
    cur=None
    con= None
    data1, data2, data3, data4,data5 = "", "", "", "",""

    sql = ""
    conn = pymysql.connect(host='127.0.0.1', user='root', password='root', db='local_student', charset='utf8')
    cur = conn.cursor()
    data1= edt1.get(); data2= edt2.get(); data3= edt3.get(); data4=edt4.get(); data5=edt5.get()
    try:
        sql="insert into usertable values('"+data1+"','"+data2+"','"+data3+"','"+data4+"','"+data5+")"
        cur.execute(sql)
    except:
        messagebox.showerror('오류','데이터 입력 오류 발생')
    else:
        messagebox.showinfo('성공','데이터 입력 성공')
    conn.commit()
    conn.close()

# 데이터 선택함수 정의
def selectData():
    strdata1, strdata2, strdata3, strdata4,strdata5 = [], [], [], [], []
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='local_student', charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT * FROM student_list")
    strdata1.append("name");
    strdata2.append("birth")
    strdata3.append("id");
    strdata4.append("hometown")
    strdata5.append("subject")
    strdata1.append("-----------");
    strdata2.append("-----------")
    strdata3.append("-----------");
    strdata4.append("-----------")
    strdata5.append("-----------");
    while(True):
            row=cur.fetchone()
            strdata1.append(row[0]); strdata2.append(row[1])
            strdata3.append(row[2]); strdata4.append(row[3])
            strdata5.append(row[4]);
            listdata1.delete(0,listdata1.size()-1); listdata2.delete(0,listdata2.size()-1)
            listdata3.delete(0,listdata3.size()-1); listdata4.delete(0,listdata4.size()-1)
            listdata5.delete(0,listdata4.size()-1);
            for item1,item2,item3,item4 in zip(strdata1,strdata2,strdata3,strdata4):
                 listdata1.insert(END,item1); listdata2.insert(END,item2)
                 listdata3.insert(END,item3); listdata4.insert(END,item4)
                 listdata5.insert(END, item5);
    conn.close()

    # 메인코드
    window = Tk()
    window.geometry("600*300")
    window.resizable(width=0, height=0)
    window.title("Dorm_student_list")

    edtFrame = Frame(window);
    edtFrame.pack()
    listFrame = Frame(window)
    listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

    edt1 = Entry(edtFrame, width=10);
    edt1.pack(side=LEFT, padx=10, pady=10)
    edt2 = Entry(edtFrame, width=10);
    edt2.pack(side=LEFT, padx=10, pady=10)
    edt3 = Entry(edtFrame, width=10);
    edt3.pack(side=LEFT, padx=10, pady=10)
    edt4 = Entry(edtFrame, width=10);
    edt4.pack(side=LEFT, padx=10, pady=10)
    edt5 = Entry(edtFrame, width=10);
    edt5.pack(side=LEFT, padx=10, pady=10)

    btnInsert = Button(edtFrame, text="입력", command=insertData)
    btnInsert.pack(side=LEFT, padx=10, pady=10)
    btnInsert = Button(edtFrame, text="조회", command=selectData)
    btnInsert.pack(side=LEFT, padx=10, pady=10)

    listdata1 = Listbox(listFrame, bg='yellow')
    listdata1.pack(side=LEFT, fill=BOTH, expand=1)
    listdata2 = Listbox(listFrame, bg='yellow')
    listdata2.pack(side=LEFT, fill=BOTH, expand=1)
    listdata3 = Listbox(listFrame, bg='yellow')
    listdata3.pack(side=LEFT, fill=BOTH, expand=1)
    listdata4 = Listbox(listFrame, bg='yellow')
    listdata4.pack(side=LEFT, fill=BOTH, expand=1)
    listdata5 = Listbox(listFrame, bg='yellow')
    listdata5.pack(side=LEFT, fill=BOTH, expand=1)

    window.mainloop()

