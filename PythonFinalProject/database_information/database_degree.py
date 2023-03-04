import mysql.connector
class database2():
    def conn(self):
        con=mysql.connector.connect(user='root',password='',host='localhost',database='python_project')
        return con
        print("done")
    def insert_data(self,id,m1,m2,m3):
        c=self.conn()
        cur=c.cursor()
        s=m1+m2+m3
        sql=' insert into degree value ("%d","%d","%d","%d","%d")'%(id,m1,m2,m3,s)
        try:
            cur.execute(sql)
            c.commit()
            print("insert row")
        except Exception as ee:
            c.rollback()
            print(ee)
        c.close()
    def get_degree(self,id):
        c = self.conn()
        cur = c.cursor()
        sql="select * from degree where id='%d'" % (id)
        try:
            cur.execute(sql)
            list_data=cur.fetchall()
            return list_data

        except Exception as ee:
            print(ee)
            return None
        c.close()
    def update_data(self,id,m1,m2,m3):
        c = self.conn()
        cur = c.cursor()
        sum=m1+m2+m3
        sql="update degree set m1='%d', m2='%d', m3='%d', sum='%d' where id ='%d'" % (m1,m2,m3,sum,id)
        try:
            cur.execute(sql)
            c.commit()
            print(" updata rwo")
        except Exception as ee:
            c.rollback()
            print("error")
            print(ee)
        c.close()
    def get_degrees(self):
        c = self.conn()
        cur = c.cursor()
        sql=" select user_informations.id, fullname, deparment, m1,m2,m3,sum from user_informations, degree where user_informations.id= degree.id" # equal to joint command
        try:
            cur.execute(sql)
            list_data=cur.fetchall()
            return list_data

        except Exception as ee:
            print(ee)
            return None
        c.close()

