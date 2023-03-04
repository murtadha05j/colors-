class database():
    def conn(self):
        import sqlite3
        con=sqlite3.connect('domain.db')
        print("connected")
        return con
    def create_table(self):
        try:
            connect = self.conn()
            c = connect.cursor()
            c.execute('create table ola(user_name Text, password Text)')
            print("create table")
        except  Exception as e:
            print(e)
        connect.close()

    def insert_data(self,v1,v2):
        try:
            connect = self.conn()
            c = connect.cursor()
            c.execute("insert into user values ('%s', '%s')" %(v1,v2))
            connect.commit()
            print("inset now")
        except Exception as e:
            print(e)
        connect.close()
    def check_user(self,v1,v2):
        try:
            connect=self.conn()
            c=connect.cursor()
            c.execute('select * from user')
            data=c.fetchall()
            i=0
            b=0
            while i < len(data):
                if data[i][0]==v1:
                    if data[i][1]==v2:
                        b=1
                        break
                    else:
                        b=2
                        break
                else:
                    b=3

                i+=1
        except Exception as e:
            print(e)
        connect.close()
        return b
x=database().check_user("ax","a")
if x==1:
    print("welcome")
elif x==2:
    print("password wrong")
else:
    print("user is not exist")




