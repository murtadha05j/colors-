import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QMessageBox, QMainWindow, \
    QTableWidget, QTableWidgetItem,QInputDialog,QLineEdit
from PyQt5.QtGui import QPixmap
a=QApplication(sys.argv)
root=QWidget()
root.setWindowTitle("hello")
root.setGeometry(500,200,400,400)
m=QMessageBox.question(root,"question","did you like python?")
def f():
    tt=int(t1.text())
    l.setText(str(tt))
    t1.setText(" ")


b=QPushButton("click me",root) # event
b.move(20,20)
b.setToolTip("click here")
b.clicked.connect(f)

t1=QLineEdit(root)   # input
t1.setGeometry(20,2,90,20)

l=QLabel("label",root)  # output
l.move(40,50)


table=QTableWidget(root) # table
table.setRowCount(2)
table.setColumnCount(3)
table.setGeometry(60,70,300,300)
def c():
    for b1 in table.selectedItems():
        print(b1.row(),b1.column(),b1.text())
table.clicked.connect(c)
table.setItem(0,0,QTableWidgetItem('1'))
table.setItem(0,1,QTableWidgetItem('2'))
table.setItem(0,2,QTableWidgetItem('3'))
table.setItem(1,0,QTableWidgetItem('4'))
table.setItem(1,1,QTableWidgetItem('5'))
table.setItem(1,2,QTableWidgetItem('6'))
table.setHorizontalHeaderLabels(str("num1:num2:num3:").split(":"))
table.setVerticalHeaderLabels(str("a*b").split("*"))



i=QInputDialog.getInt(root,'cal','enter number',12,0,100,2) # bahave as a list
x=QInputDialog.getText(root,'2021','enter name',QLineEdit.Normal)
v=('yellow','black','white','blue')
c=QInputDialog.getItem(root,'background','enter your color',v)




lab=QLabel(root) # picture
p=QPixmap('a.jpg')
lab.setPixmap(p)
root.resize(p.width(),p.height())


root.show()
sys.exit(a.exec_())

