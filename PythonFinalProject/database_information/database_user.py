import mysql.connector
class database1():
    def conn(self):
        con=mysql.connector.connect(user='root',password='',host='localhost',database='python_project')
        return con
        print("done")
    def get_user(self):
        c=self.conn()
        cur=c.cursor()
        sql="select * from user_informations"
        try:
            cur.execute(sql)
            list_data=cur.fetchall()
            return list_data

        except Exception as ee:
            print(ee)
            return None
    def check_user(self,user,passWord):
        data=self.get_user()
        username=[]
        password=[]
        for i in data:
            username.append(i[3])
            password.append(i[2])
        j=0
        while j<len(username):
            if  username[j]==user:
                if password[j]==passWord:
                    return 1
                else:
                    return 2
            else:
                j+=1
                continue
                return 3
    def get_stutus(self,s1):
        c=self.conn()
        cur=c.cursor()
        sql="select type form user_informations where username= '%s'" %s1
        try:
            cur.execute(sql)
            data=cur.fetchall()
            return data[0][0]
        except Exception as ee:
            print(ee)
            return None
    def insert_data(self,f,p,u,t,d):
        c=self.conn()
        cur=c.cursor()
        sql=' insert into user_informations (fullname, password, username, type, deparment) value ("%s","%s","%s","%s","%s")'%(f,p,u,t,d)
        try:
            cur.execute(sql)
            c.commit()
            print("insert row")
        except Exception as ee:
            c.rollback()
            print(ee)
        c.close()
    def get_student(self):
        c=self.conn()
        cur=c.cursor()
        sql="select * from user_informations where type='student'"
        try:
            cur.execute(sql)
            list_data=cur.fetchall()
            return list_data

        except Exception as ee:
            print(ee)
            return None
