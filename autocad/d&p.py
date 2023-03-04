import sqlite3
#connect
con=sqlite3.connect("oow.db")
cursor=con.cursor()
#cursor.execute('create table dimensions (width int , height int )')

#w=int(input("enter the w "))
#h=int(input("enter the h "))

cursor.execute("INSERT INTO dimensions (width,height) VALUES(%d,%d)" %(w,h))

cursor.execute("SELECT width FROM dimensions ORDER BY rowid DESC LIMIT 1;")
#list=cursor.fetchall()
print(list[0][0])


con.commit()

cursor.close()