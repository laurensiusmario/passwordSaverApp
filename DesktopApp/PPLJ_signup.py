# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PPLJ_signup.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon

from PPLJ_login import Ui_Dialog_Login

from PyQt5.QtWebEngineWidgets import *
import requests
import json
from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication

url ='https://127.0.0.1:5000/api/add_user'

class Ui_Dialog_Signup(object):
    def setupUi_signup(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 375) #675,375
        self.username = QtWidgets.QLabel(Dialog)
        self.username.setGeometry(QtCore.QRect(50, 100, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLabel(Dialog)
        self.password.setGeometry(QtCore.QRect(50, 160, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.create_acc = QtWidgets.QLabel(Dialog)
        self.create_acc.setGeometry(QtCore.QRect(10, 20, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.create_acc.setFont(font)
        self.create_acc.setAlignment(QtCore.Qt.AlignCenter)
        self.create_acc.setObjectName("create_acc")
        self.line_user = QtWidgets.QLineEdit(Dialog)
        self.line_user.setGeometry(QtCore.QRect(160, 100, 241, 22))
        self.line_user.setObjectName("line_user")
        self.line_pass = QtWidgets.QLineEdit(Dialog)
        self.line_pass.setGeometry(QtCore.QRect(160, 160, 241, 22))
        self.line_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_pass.setObjectName("line_pass")
        self.confirm_pass = QtWidgets.QLabel(Dialog)
        self.confirm_pass.setGeometry(QtCore.QRect(50, 230, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.confirm_pass.setFont(font)
        self.confirm_pass.setObjectName("confirm_pass")
        self.line_confirmpass = QtWidgets.QLineEdit(Dialog)
        self.line_confirmpass.setGeometry(QtCore.QRect(160, 240, 241, 22))
        self.line_confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_confirmpass.setObjectName("line_confirmpass")
        self.button_signup = QtWidgets.QPushButton(Dialog)
        self.button_signup.setGeometry(QtCore.QRect(130, 320, 93, 28))
        self.button_signup.setObjectName("button_signup")
        self.button_login = QtWidgets.QPushButton(Dialog)
        self.button_login.setGeometry(QtCore.QRect(230, 320, 93, 28))
        self.button_login.setObjectName("button_login")
        self.warning = QtWidgets.QLabel(Dialog)
        self.warning.setGeometry(QtCore.QRect(170, 190, 231, 31))
        self.warning.setObjectName("warning")
        self.warning2 = QtWidgets.QLabel(Dialog)
        self.warning2.setGeometry(QtCore.QRect(160, 190, 16, 16))
        self.warning2.setObjectName("warning2")

        self.button_signup.clicked.connect(self.signupCheck_signup)
        self.button_login.clicked.connect(self.loginCheck_signup)

        self.retranslateUi_signup(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    

    def signupCheck_signup(self):
        print("Sign Up Button Clicked!")
        username = self.line_user.text()
        password = self.line_pass.text()
        confirm_pass = self.line_confirmpass.text()
        
        obj = {"name":username,"password":password}

        if((len(username))>0):
            if(password == confirm_pass):
                x = requests.post(url, json=obj, verify=False)

                if (x.text =="user existed"):
                    self.showMessageBox('Warning','Username already existed!')     
                else:     
                    self.showInformationBox('Account Created','otp_secret : '+x.text)
                    self.loginCheck_signup()
            else:
                self.showMessageBox('Warning','Unmatched Password')
        else:
            self.showMessageBox('Warning','Invalid username')
        
    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def showInformationBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def loginCheck_signup(self):
        print("Log In Button Clicked!")
        self.Dialog_login = QtWidgets.QDialog()
        self.ui_login = Ui_Dialog_Login()
        self.ui_login.setupUi_login(self.Dialog_login)
        self.Dialog_login.show()
        Dialog_Signup.hide()

    def retranslateUi_signup(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Password Manager : Sign Up"))
        self.username.setText(_translate("Dialog", "Username"))
        self.password.setText(_translate("Dialog", "Password"))
        self.create_acc.setText(_translate("Dialog", "Create Account"))
        self.line_user.setPlaceholderText(_translate("Dialog", "Input Username"))
        self.line_pass.setPlaceholderText(_translate("Dialog", "Input Password"))
        self.confirm_pass.setText(_translate("Dialog", "<html><head/><body><p>Confirm<br/>Password</p></body></html>"))
        self.line_confirmpass.setPlaceholderText(_translate("Dialog", "Confirm Password"))
        self.button_signup.setText(_translate("Dialog", "Sign Up!"))
        self.button_login.setText(_translate("Dialog", "Log In"))
        self.warning.setText(_translate("Dialog", "<html><head/><body><p>Choose password with a mix of<br/> letters, numbers &amp; symbols</p></body></html>"))
        self.warning2.setText(_translate("Dialog", "*"))


if __name__ == "__main__":
    import sys
    app_signup = QtWidgets.QApplication(sys.argv)
    Dialog_Signup = QtWidgets.QDialog()
    ui = Ui_Dialog_Signup()
    ui.setupUi_signup(Dialog_Signup)
    Dialog_Signup.show()
    sys.exit(app_signup.exec_())
