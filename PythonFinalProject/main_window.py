
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap
from database_information.database_user import database1
a = QApplication(sys.argv)
root = QWidget()
root.setWindowTitle("hello")
root.setGeometry(500, 200, 400, 400)

# picture
lab = QLabel(root)
p = QPixmap('img/pic.jpg')
lab.setPixmap(p)
root.resize(p.width(), p.height())
# tow label
user = QLabel('user name', root)
password = QLabel('password', root)
user.move(100, 50)
password.move(100, 80)

# two edit line
username = QLineEdit(root)
Epassword = QLineEdit(root)
username.move(200, 50)
Epassword.move(200, 75)

# two button
signin = QPushButton('sign in', root)
signup = QPushButton('sign up', root)
signin.move(150, 110)
signup.move(250, 110)


def ev1():
    try:
        import database_information.database_user
        var=database_information.database_user.database1().check_user(username.text(),Epassword.text())
        if var == 1:
            print("hello")
            ty = database1().get_stutus(username.text())
            if ty == 'student':
                import student.main_stu
            else:
                import professor.main_pro
    except Exception as ee:
        print(ee)
def ev2():
    try:

        import second_window
        print("welcome second ")
    except Exception as ee:
        print(ee)

signin.clicked.connect(ev1)
signup.clicked.connect(ev2)

root.show()
sys.exit(a.exec_())
