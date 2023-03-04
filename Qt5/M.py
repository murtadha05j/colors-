import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction
a=QApplication(sys.argv)
root=QMainWindow()
root.setWindowTitle("hello")
root.setGeometry(500,200,400,400)


menubar=root.menuBar()
f1=menubar.addMenu("file")
f2=menubar.addMenu("edit")
f3=menubar.addMenu("help")
f4=menubar.addMenu("code")
e1=QAction("new",root)
e1.setShortcut("ctrl+a")
e2=QAction("second",root)
e2.setShortcut("ctrl+b")
def f():
    print("hello new")
e1.triggered.connect(f)
f1.addAction(e1)
f1.addAction(e2)
f2.addAction(e2)


root.show()
sys.exit(a.exec_())