# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'autocad.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from pyautocad import Autocad, APoint, aDouble
import array  # for polyline
import math

acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from Python\n")
print(acad.doc.Name)

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        font = QtGui.QFont()
        font.setPointSize(5)
        Form.setFont(font)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(150, 90, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 130, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(280, 90, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(280, 130, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 170, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(280, 170, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 220, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        ###########################################
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(150, 50, 101, 31))
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(260, 40, 81, 41))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label")
        ##################################

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "العرض"))

        self.label_2.setText(_translate("Form", "الطول"))
        self.label_3.setText(_translate("Form", "عدد النسخ "))
        self.pushButton.setText(_translate("Form", "ارسم"))
        self.pushButton.clicked.connect(self.c)
        #######################################

        self.comboBox.setItemText(0, _translate("Form", "rectangle"))
        self.comboBox.setItemText(1, _translate("Form", "circle"))
        self.comboBox.setItemText(2, _translate("Form", "triangle"))
        self.comboBox.setItemText(3, _translate("Form", "shape"))
        self.label_4.setText(_translate("Form", "اختار الشكل"))

        #####################################################

    def c(self):
        n = self.comboBox.currentText()
        w = int(self.lineEdit.text())
        h = int(self.lineEdit_2.text())
        repeat = int(self.lineEdit_3.text())
        x=0
        y=0
        if n == "shape":

            for i in range(repeat):
                import box
                box.shapes().draw1(x, y, w, h)
                y+=h*1.4+40
        elif n == "rectangle":
            for i in range(repeat):
                import box
                box.shapes().draw0(x, y, w, h)
                y+=h/3+70



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

