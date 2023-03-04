import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton,QComboBox,QRadioButton
from PyQt5.QtGui import QPixmap
from database_information.database_user import database1
a = QApplication(sys.argv)
t = QWidget()
t.setWindowTitle("second window")
t.setGeometry(100,100,428,322)


background=QLabel(t)
pix=QPixmap('img/n.jpg')
background.setPixmap(pix)

# five label
fullName= QLabel('Full name',t)
passW= QLabel('password',t)
userName= QLabel('User name', t)
depart=QLabel('Department', t)
type= QLabel('Type', t)
fullName.move(100,50)
passW.move(100,80)
userName.move(100,110)
depart.move(100,140)
type.move(100,180)

# two edit line
Fullname=QLineEdit(t)
password=QLineEdit(t)
Username=QLineEdit(t)
Fullname.move(200,50)
password.move(200,75)
Username.move(200,100)
# combox department
department=QComboBox(t)
department.addItem('CS')
department.addItem('IS')
department.addItem('IT')
department.move(200,140)

#type radiobutton
s= QRadioButton('student',t)
rr= QRadioButton('professor',t)
s.move(150,180)
rr.move(220,180)

#button
send=QPushButton('send data',t)
send.move(150,220)

def eve1():
    try:
        f = Fullname.text()
        p = password.text()
        u = Username.text()
        if s.isChecked():
            tt = 'student'
        elif rr.isChecked():
            tt = 'professor'
        else:
            tt = 'null'
        d = department.currentText()
        database1().insert_data(f,p,u,tt,d)
        t.destroy()
    except Exception as ee:
        print(ee)




send.clicked.connect(eve1)



t.show()
