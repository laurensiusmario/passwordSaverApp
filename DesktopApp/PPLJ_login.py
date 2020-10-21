# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PPLJ_login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import json

from user_home_v3 import Ui_MainWindow_home

url ='https://127.0.0.1:5000/api/user_login'

class Ui_Dialog_Login(object):
    def setupUi_login(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 380)
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
        self.login = QtWidgets.QLabel(Dialog)
        self.login.setGeometry(QtCore.QRect(10, 20, 431, 31))

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.login.setFont(font)
        self.login.setAlignment(QtCore.Qt.AlignCenter)
        self.login.setObjectName("login")

        self.line_user = QtWidgets.QLineEdit(Dialog)
        self.line_user.setGeometry(QtCore.QRect(160, 100, 241, 22))
        self.line_user.setObjectName("line_user")

        self.line_pass = QtWidgets.QLineEdit(Dialog)
        self.line_pass.setGeometry(QtCore.QRect(160, 160, 241, 22))
        self.line_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_pass.setObjectName("line_pass")

        self.token = QtWidgets.QLabel(Dialog)
        self.token.setGeometry(QtCore.QRect(50, 210, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.token.setFont(font)
        self.token.setObjectName("token")

        self.line_token = QtWidgets.QLineEdit(Dialog)
        self.line_token.setGeometry(QtCore.QRect(160, 220, 241, 22))
        self.line_token.setObjectName("line_token")
        
        self.button_login = QtWidgets.QPushButton(Dialog)
        self.button_login.setGeometry(QtCore.QRect(175, 320, 100, 28))
        self.button_login.setObjectName("button_login")
        
        self.button_login.clicked.connect(self.loginCheck_login)

        self.retranslateUi_login(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    def loginCheck_login(self):
        print("Log In Button Clicked!")
        username = self.line_user.text()
        password = self.line_pass.text()
        token = self.line_token.text()

        obj = {"name":username,"password":password,"token":token}

        if (username=="") or (password=="") or (token==""):
            self.showMessageBox('Warning', 'Please fill everything!')
        else:
            if(((len(username))>0) and ((len(password))>0) and ((len(token))>0)):
                x = requests.post(url, json=obj, verify=False)
                #print(x.cookies.get_dict())
                #print(x.headers)             
                #print(x.request.headers)
                if(x.text == "Valid"):
                    self.showInformationBox('Log In Successful','Welcome, '+username+'!')
                    self.cookiesss = x.cookies.get_dict()
                    self.home(self.cookiesss, username)                 
                else:
                    self.showMessageBox('Warning','Incorrect Username/Password/Token')
            else:
                self.showMessageBox('Warning','Invalid input')

    def home(self, cookiesss, usname):
        print("Log In Button Clicked, Redirect to Home!")
        self.message = cookiesss
        self.id = usname
        self.MainWindow_home = QtWidgets.QMainWindow()
        self.ui_home = Ui_MainWindow_home(self.message, self.id)
        self.ui_home.setupUi_home(self.MainWindow_home)
        self.MainWindow_home.show()
        try:
            Dialog_login.hide()
        except:
            pass

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

    def retranslateUi_login(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Password Manager : Log In"))
        self.username.setText(_translate("Dialog", "Username"))
        self.password.setText(_translate("Dialog", "Password"))
        self.login.setText(_translate("Dialog", "Log In"))
        self.line_user.setPlaceholderText(_translate("Dialog", "Input Username"))
        self.line_pass.setPlaceholderText(_translate("Dialog", "Input Password"))
        self.token.setText(_translate("Dialog", "Token"))
        self.line_token.setPlaceholderText(_translate("Dialog", "Input TOTP Token"))
        self.button_login.setText(_translate("Dialog", "Log In"))


if __name__ == "__main__":
    import sys
    app_login = QtWidgets.QApplication(sys.argv)
    Dialog_login = QtWidgets.QDialog()
    ui = Ui_Dialog_Login()
    ui.setupUi_login(Dialog_login)
    Dialog_login.show()
    sys.exit(app_login.exec_())
