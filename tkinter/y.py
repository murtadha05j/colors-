import sys
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QLineEdit,QLabel,QMessageBox,QMainWindow
a=QApplication(sys.argv)
t=QWidget()
t2=QMainWindow()
t.setWindowTitle("hello")
t.setGeometry(500,200,400,400)
m=QMessageBox.question(t,"question","did you like python?")
def f():
    tt=int(t1.text())
    l.setText(str(tt))
    t1.setText(" ")


b=QPushButton("click me",t) # event
b.move(20,20)
b.setToolTip("click here")
b.clicked.connect(f)

t1=QLineEdit(t)   # input
t1.setGeometry(20,2,90,20)

l=QLabel("label",t)  # output
l.move(40,50)




t.show()
sys.exit(a.exec_())

