import sqlite3
import tkinter as tk
from tkinter import messagebox

mainwindow=tk.Tk()
mainwindow.title("STUDENT MANAGEMENT SYSTEM")
heading_label=tk.Label(mainwindow,text="Name")
heading_label.pack()
name=tk.Entry(mainwindow)
name.pack()
heading_label=tk.Label(mainwindow,text="College")
heading_label.pack()
college=tk.Entry(mainwindow)
college.pack()
heading_label=tk.Label(mainwindow,text="Address")
heading_label.pack()
address=tk.Entry(mainwindow)
address.pack()
heading_label=tk.Label(mainwindow,text="Phone")
heading_label.pack()
phone=tk.Entry(mainwindow)
phone.pack()

connection=sqlite3.connect("student.db")
TABLE_NAME="student_table"
STUDENT_ID="student_id"
STUDENT_NAME="student_name"
STUDENT_COLLEGE="student_college"
STUDENT_ADDRESS="student_address"
STUDENT_PHONE="student_phone"
connection.execute(' CREATE TABLE IF NOT EXISTS '+TABLE_NAME+'('+STUDENT_ID+' INTEGER PRIMARY KEY AUTOINCREMENT, '+STUDENT_NAME+' TEXT, '+STUDENT_COLLEGE+' TEXT, '+STUDENT_ADDRESS+' TEXT, '+STUDENT_PHONE+' INTEGER);')
def insert():
    uname=name.get()
    ucollege=college.get()
    uaddress=address.get()
    uphone=phone.get()
    if(len(uname)>0 and len(ucollege)>0 and len(uaddress)>0 and len(uphone)>0):
        connection.execute(" INSERT INTO "+TABLE_NAME+" ( "+STUDENT_NAME+", "+STUDENT_COLLEGE+", "+STUDENT_ADDRESS+", "+STUDENT_PHONE+" ) VALUES ( '"+uname+"', '"+ucollege+"', '"+uaddress+"', "+uphone+" ); ")
        connection.commit()
        messagebox.showerror("error","INSERTED")
    else:
        messagebox.showerror("error","insert some value")
def collect():
    cursor = connection.execute("select * from " + TABLE_NAME + ";")
    for row in cursor:
            result_label_name = tk.Label(mainwindow,text=row[1]+"       "+row[2]+"      "+row[3]+"      "+str(row[4]))
            result_label_name.pack()
save=tk.Button(mainwindow,text="SAVE",command=lambda:insert())
save.pack()
retrieve=tk.Button(mainwindow,text="RETRIEVE",command=lambda:collect())
retrieve.pack()
result_label_name = tk.Label(mainwindow, text="Name     College     Address     Phone_Number")
result_label_name.pack()
mainwindow.mainloop()