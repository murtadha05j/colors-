import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QTabWidget, QTableWidget, \
    QTableWidgetItem, QPushButton
from PyQt5.QtGui import QPixmap
from database_information.database_user import database1
a = QApplication(sys.argv)
root = QMainWindow()
root.setWindowTitle("hello")
root.setGeometry(500, 200, 400, 400)
tab=QTabWidget(root)

##########################
# one tab                #
##########################

t1=QWidget(root)

##########################
# table for student      #
##########################
table=QTableWidget(t1)
c=database1().get_student()
id=[]
fullname=[]
type=[]
username=[]
password=[]
department=[]
for data in c:
    id.append(data[0])
    fullname.append(data[1])
    password.append(data[2])
    username.append(data[3])
    type.append(data[4])
    department.append(data[5])
table.setColumnCount(6)
table.setRowCount(len(username))

i=0
while i<len(username):
    table.setItem(i,0,QTableWidgetItem(str(id[i])))
    table.setItem(i,1,QTableWidgetItem(fullname[i]))
    table.setItem(i,2,QTableWidgetItem(username[i]))
    table.setItem(i,3,QTableWidgetItem(type[i]))
    table.setItem(i,4,QTableWidgetItem(department[i]))
    table.setItem(i,5,QTableWidgetItem(password[i]))
    i+=1
table.setGeometry(10,10,350,250)
table.setHorizontalHeaderLabels(str("Id:FullName:UserName:Type:Department:Password").split(":"))

##########################
# two tab                #
##########################

t2=QWidget(root)
#four label

id=QLabel('id' ,t2)
m1=QLabel('m1',t2)
m2=QLabel('m2',t2)
m3=QLabel('m3',t2)
id.move(100,50)
m1.move(100,80)
m2.move(100,110)
m3.move(100,140)

# four edit line
Id=QLineEdit(t2)
M1=QLineEdit(t2)
M2=QLineEdit(t2)
M3=QLineEdit(t2)
Id.move(200,50)
M1.move(200,75)
M2.move(200,100)
M3.move(200,125)

# one button
add=QPushButton('add degree',t2)
add.move(180,170)

def eve4():
    import database_information.database_degree
    database_information.database_degree.database2().insert_data(int(Id.text()),int(M1.text()),int(M2.text()),int(M3.text()))
    print('done')
    Id.setText(' ')
    M1.setText(' ')
    M2.setText(' ')
    M3.setText(' ')
add.clicked.connect(eve4)

##########################
# three tab               #
##########################
t3=QWidget(root)
# 7 label
id=QLabel('enter id student',t3)
m1=QLabel('M1 Degree',t3)
m2=QLabel('M2 Degree',t3)
m3=QLabel('M3 Degree',t3)
d1=QLabel('null',t3)
d2=QLabel('null',t3)
d3=QLabel('null',t3)
id.move(100,40)
m1.move(100,80)
m2.move(100,110)
m3.move(100,140)
d1.move(200,80)
d2.move(200,110)
d3.move(200,140)

# two edit line
Id1=QLineEdit(t3)
M11=QLineEdit(t3)
M21=QLineEdit(t3)
M31=QLineEdit(t3)
Id1.move(180,38)
M11.move(250,75)
M21.move(250,110)
M31.move(250,135)
Id1.resize(50,15)
M11.resize(50,15)
M21.resize(50,15)
M31.resize(50,15)

# one button
updata=QPushButton('updata degree',t3)
search=QPushButton('search',t3)
updata.move(180,170)
search.move(250,35)

def ev5():
    import database_information.database_degree
    data=database_information.database_degree.database2().get_degree(int(Id1.text()))

    if data!=None:
        d1.setText(str(data[0][1]))
        d2.setText(str(data[0][2]))
        d3.setText(str(data[0][3]))
    else:
        print("error")
search.clicked.connect(ev5)


def ev6():
    import database_information.database_degree
    database_information.database_degree.database2().update_data(int(Id1.text()),int(M11.text()),int(M21.text()),int(M31.text()))
    print("dddddd")
    d1.setText(M11.text())
    d2.setText(M21.text())
    d3.setText(M31.text())
    M11.setText(' ')
    M21.setText(' ')
    M31.setText(' ')
updata.clicked.connect(ev6)


##########################
# four tab               #
##########################

t4=QWidget(root)
# table to show all students
table=QTableWidget(t4)
ID=[]
Fullname=[]
Department=[]
D1=[]
D2=[]
D3=[]
sum=[]
import database_information.database_degree
v=database_information.database_degree.database2().get_degrees()
for data in v:
    ID.append(data[0])
    Fullname.append(data[1])
    Department.append(data[2])
    D1.append(data[3])
    D2.append(data[4])
    D3.append(data[5])
    sum.append(data[6])
table.setColumnCount(7)
table.setRowCount(len(ID))

i=0
while i<len(ID):
    table.setItem(i,0,QTableWidgetItem(str(ID[i])))
    table.setItem(i,1,QTableWidgetItem(Fullname[i]))
    table.setItem(i,2,QTableWidgetItem(Department[i]))
    table.setItem(i,3,QTableWidgetItem(str(D1[i])))
    table.setItem(i,4,QTableWidgetItem(str(D2[i])))
    table.setItem(i,5,QTableWidgetItem(str(D3[i])))
    table.setItem(i,6,QTableWidgetItem(str(sum[i])))
    i+=1
table.setGeometry(10,10,350,250)
table.setHorizontalHeaderLabels(str("Id:FullName:Department:M1:M2:M3:Sum").split(":"))


tab.resize(428,322)
tab.addTab(t1,'Show')
tab.addTab(t2,'Add degree')
tab.addTab(t3,'Updata degree')
tab.addTab(t4,"Degree")


root.show()


