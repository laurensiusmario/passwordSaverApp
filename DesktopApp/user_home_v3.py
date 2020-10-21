from PyQt5 import QtCore, QtGui, QtWidgets
import encryptionlib as crypt
import json
import sys
import requests

url_api_get = "https://127.0.0.1:5000/api/get_user_storage/"
url_api_put = "https://127.0.0.1:5000/api/update_user_storage/"
url_api_updateacc = "https://127.0.0.1:5000/api/update_user_account/"
url_api_delacc = "https://127.0.0.1:5000/api/delete_user/"
url_api_logout = "https://127.0.0.1:5000/api/user_logout/"


class Ui_MainWindow_home(object):
    ## Set initialization parameters
    def __init__(self, message, usname):
        global headerr 
        global id_user

        id_user = usname
        headerr = message

    ## Create GUI object (button, text, etc)
    def setupUi_home(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1150, 451)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.activeuser_label = QtWidgets.QLabel(self.centralwidget)
        self.activeuser_label.setObjectName("activeuser_label")
        self.verticalLayout_3.addWidget(self.activeuser_label)
        self.tableData = QtWidgets.QTableWidget(self.centralwidget)
        self.tableData.setEnabled(True)
        self.tableData.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableData.setAlternatingRowColors(True)
        self.tableData.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableData.setRowCount(0)
        self.tableData.setObjectName("tableData")
        self.tableData.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableData.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableData.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableData.setHorizontalHeaderItem(2, item)
        self.tableData.horizontalHeader().setDefaultSectionSize(120)
        self.verticalLayout_3.addWidget(self.tableData)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.AESKey = QtWidgets.QFormLayout()
        self.AESKey.setObjectName("AESKey")
        self.AESKey_label = QtWidgets.QLabel(self.centralwidget)
        self.AESKey_label.setObjectName("AESKey_label")
        self.AESKey.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.AESKey_label)
        self.AESK_input = QtWidgets.QLineEdit(self.centralwidget)
        self.AESK_input.setObjectName("AESK_input")
        self.AESKey.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.AESK_input)
        self.verticalLayout.addLayout(self.AESKey)
        self.UpdateTable_button = QtWidgets.QPushButton(self.centralwidget)
        self.UpdateTable_button.setObjectName("UpdateTable_button")
        self.verticalLayout.addWidget(self.UpdateTable_button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.AddNewPassword_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddNewPassword_label.sizePolicy().hasHeightForWidth())
        self.AddNewPassword_label.setSizePolicy(sizePolicy)
        self.AddNewPassword_label.setObjectName("AddNewPassword_label")
        self.verticalLayout.addWidget(self.AddNewPassword_label)
        self.line_1 = QtWidgets.QFrame(self.centralwidget)
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.verticalLayout.addWidget(self.line_1)
        self.AddNewPassword = QtWidgets.QFormLayout()
        self.AddNewPassword.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.AddNewPassword.setObjectName("AddNewPassword")
        self.Website_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Website_label.sizePolicy().hasHeightForWidth())
        self.Website_label.setSizePolicy(sizePolicy)
        self.Website_label.setObjectName("Website_label")
        self.AddNewPassword.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Website_label)
        self.Website_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Website_input.setObjectName("Website_input")
        self.AddNewPassword.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Website_input)
        self.Username_label = QtWidgets.QLabel(self.centralwidget)
        self.Username_label.setObjectName("Username_label")
        self.AddNewPassword.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Username_label)
        self.Username_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Username_input.setObjectName("Username_input")
        self.AddNewPassword.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Username_input)
        self.Password_label = QtWidgets.QLabel(self.centralwidget)
        self.Password_label.setObjectName("Password_label")
        self.AddNewPassword.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Password_label)
        self.Password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Password_input.setObjectName("Password_input")
        self.AddNewPassword.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Password_input)
        self.verticalLayout.addLayout(self.AddNewPassword)
        self.AddPassword_button = QtWidgets.QPushButton(self.centralwidget)
        self.AddPassword_button.setObjectName("AddPassword_button")
        self.verticalLayout.addWidget(self.AddPassword_button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem1)
        self.DeletePassword_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DeletePassword_label.sizePolicy().hasHeightForWidth())
        self.DeletePassword_label.setSizePolicy(sizePolicy)
        self.DeletePassword_label.setObjectName("DeletePassword_label")
        self.verticalLayout.addWidget(self.DeletePassword_label)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.DeletePassword = QtWidgets.QFormLayout()
        self.DeletePassword.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.DeletePassword.setObjectName("DeletePassword")
        self.RowNumber_label = QtWidgets.QLabel(self.centralwidget)
        self.RowNumber_label.setObjectName("RowNumber_label")
        self.DeletePassword.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.RowNumber_label)
        self.RowN_input = QtWidgets.QSpinBox(self.centralwidget)
        self.RowN_input.setObjectName("RowN_input")
        self.DeletePassword.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.RowN_input)
        self.verticalLayout.addLayout(self.DeletePassword)
        self.DeletePassword_button = QtWidgets.QPushButton(self.centralwidget)
        self.DeletePassword_button.setObjectName("DeletePassword_button")
        self.verticalLayout.addWidget(self.DeletePassword_button)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ChangeUserProfile = QtWidgets.QLabel(self.centralwidget)
        self.ChangeUserProfile.setObjectName("ChangeUserProfile")
        self.verticalLayout_2.addWidget(self.ChangeUserProfile)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.NewUsername_label = QtWidgets.QLabel(self.centralwidget)
        self.NewUsername_label.setObjectName("NewUsername_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.NewUsername_label)
        self.NewPassword_label = QtWidgets.QLabel(self.centralwidget)
        self.NewPassword_label.setObjectName("NewPassword_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.NewPassword_label)
        self.ConfirmPassword_label = QtWidgets.QLabel(self.centralwidget)
        self.ConfirmPassword_label.setObjectName("ConfirmPassword_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.ConfirmPassword_label)
        self.NewUsername_input = QtWidgets.QLineEdit(self.centralwidget)
        self.NewUsername_input.setObjectName("NewUsername_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.NewUsername_input)
        self.NewPassword_input = QtWidgets.QLineEdit(self.centralwidget)
        self.NewPassword_input.setObjectName("NewPassword_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.NewPassword_input)
        self.ConfirmPassword_input = QtWidgets.QLineEdit(self.centralwidget)
        self.ConfirmPassword_input.setObjectName("ConfirmPassword_input")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ConfirmPassword_input)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.CUP_Button = QtWidgets.QPushButton(self.centralwidget)
        self.CUP_Button.setObjectName("CUP_Button")
        self.verticalLayout_2.addWidget(self.CUP_Button)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem2)
        self.ChangeAESKey = QtWidgets.QLabel(self.centralwidget)
        self.ChangeAESKey.setObjectName("ChangeAESKey")
        self.verticalLayout_2.addWidget(self.ChangeAESKey)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.OldKey_label = QtWidgets.QLabel(self.centralwidget)
        self.OldKey_label.setObjectName("OldKey_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.OldKey_label)
        self.NewKey_label = QtWidgets.QLabel(self.centralwidget)
        self.NewKey_label.setObjectName("NewKey_label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.NewKey_label)
        self.ConfirmNewKey_label = QtWidgets.QLabel(self.centralwidget)
        self.ConfirmNewKey_label.setObjectName("ConfirmNewKey_label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.ConfirmNewKey_label)
        self.OldKey_input = QtWidgets.QLineEdit(self.centralwidget)
        self.OldKey_input.setObjectName("OldKey_input")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.OldKey_input)
        self.NewKey_input = QtWidgets.QLineEdit(self.centralwidget)
        self.NewKey_input.setObjectName("NewKey_input")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.NewKey_input)
        self.ConfirmNewKey_input = QtWidgets.QLineEdit(self.centralwidget)
        self.ConfirmNewKey_input.setObjectName("ConfirmNewKey_input")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ConfirmNewKey_input)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.CAK_Button = QtWidgets.QPushButton(self.centralwidget)
        self.CAK_Button.setObjectName("CAK_Button")
        self.verticalLayout_2.addWidget(self.CAK_Button)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem3)
        self.DeleteAccount = QtWidgets.QLabel(self.centralwidget)
        self.DeleteAccount.setObjectName("DeleteAccount")
        self.verticalLayout_2.addWidget(self.DeleteAccount)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.DA_Button = QtWidgets.QPushButton(self.centralwidget)
        self.DA_Button.setObjectName("DA_Button")
        self.verticalLayout_2.addWidget(self.DA_Button)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1150, 26))
        self.menubar.setObjectName("menubar")
        self.menuAccount = QtWidgets.QMenu(self.menubar)
        self.menuAccount.setObjectName("menuAccount")
        MainWindow.setMenuBar(self.menubar)
        self.actionLogOut = QtWidgets.QAction(MainWindow)
        self.actionLogOut.setObjectName("actionLogOut")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuAccount.addAction(self.actionLogOut)
        self.menuAccount.addSeparator()
        self.menuAccount.addAction(self.actionAbout)
        self.menubar.addAction(self.menuAccount.menuAction())

        self.retranslateUi_home(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ## Connect button to function
        self.UpdateTable_button.clicked.connect(self.execUpdateTable)
        self.AddPassword_button.clicked.connect(self.execAddPassword)
        self.DeletePassword_button.clicked.connect(self.execDeletePassword)
        self.actionLogOut.triggered.connect(self.execLogOut)
        self.actionAbout.triggered.connect(self.execAbout)
        self.CUP_Button.clicked.connect(self.update_user_profile)
        self.CAK_Button.clicked.connect(self.execChangeKey)
        self.DA_Button.clicked.connect(self.execDeleteAccount)

    def getUserStorage(self):
        global data
        global encrypted_data
        global aescheck
        global addinit

        data = []
        aescheck = False
        aesnew = False
        passwordnew = False
        addinit = False
        
        if(headerr==""):
            self.showWarningBox('Warning','Please Login')
        else:
            try:
                response = requests.get(url_api_get, verify=False, cookies=headerr)
                encrypted_data = response.text
            except:
                print("Get data error")

            key = self.AESK_input.text()
            
            if(response.ok): # Storage Filled
                try:
                    data = eval((crypt.decrypt(encrypted_data,crypt.processDecryptKey(key))).decode())
                    aescheck = True
                    print("> Got data from server database")
                except:
                    print("Data evaluation failed")
                    aescheck = False
                    print("Failed getting data from database: Please insert the right AES key")
                    self.showWarningBox('Warning',"Failed getting data from database: \nPlease insert the right AES key")
            else: # Storage Empty
                servicename = self.Website_input.text()
                username = self.Username_input.text()
                password = self.Password_input.text()

                if (key):
                    aesnew = True

                if (servicename and username and password):
                    passwordnew = True

                if (aesnew and passwordnew):
                    self.showInformationBox('Success',"AES Key Setup Succesfull: \nAES key : " + key)
                    addinit = True
                else:
                    self.showWarningBox('Warning',"Storage Empty: \nPlease insert new password and new AES key")            

    def postUserStorage(self):
        global data

        if(headerr==""):
            self.showWarningBox('Warning','Please Login')
        else:
            try:
                key = self.AESK_input.text()
                temp = (crypt.encrypt(str(data).encode(),crypt.processDecryptKey(key)))
                encrypted_data = temp.decode()
                obj = {"storage":str(encrypted_data)}
                resp = requests.put(url_api_put, json = obj, verify=False, cookies=headerr)

                print("> Data posted to server database")
            except:
                print("Failed posting data to database")
                self.showWarningBox('Warning',"Failed posting data to database")

    def execUpdateTable(self):
        global data
        global aescheck

        # Reset table data
        self.tableData.setRowCount(0)
        
        if(headerr==""):
            self.showWarningBox('Warning','Please Login')
        else:
            try:
                # Get array of dictionaries on data variable
                aescheck = False
                self.getUserStorage()

                if aescheck:
                    # Parse and show into table
                    headercount = self.tableData.columnCount()
                    for n in data:
                        rowPosition = self.tableData.rowCount()
                        self.tableData.insertRow(rowPosition)
                        for x in range(0,headercount,1):
                            tablehead = self.tableData.horizontalHeaderItem(x).text()
                            for key in n.keys():
                                if tablehead == key:
                                    self.tableData.setItem(rowPosition,x,QtWidgets.QTableWidgetItem(str(n[key])))
                    print("> Table view updated")
            except:
                print("Exception: Error updating tableview")
                pass

    def execAddPassword(self):
        global data
        global aescheck
        global addinit

        if(headerr==""):
            self.showWarningBox('Warning','Please Login')
        else:
            try:
                # Get array of dictionaries on data variable
                aescheck = False
                self.getUserStorage()

                if aescheck or addinit:
                    servicename = self.Website_input.text()
                    username = self.Username_input.text()
                    password = self.Password_input.text()
                    temp = {
                        'servicename': servicename,
                        'username': username,
                        'password': password
                    }
                    data.append(temp)
                    print(data)
                    self.postUserStorage()
                    self.execUpdateTable()
                    print("Success adding row data\n")
            except:
                print("Exception: Error adding row data")
                pass

    def execDeletePassword(self):
        global data
        global aescheck

        if(headerr==""):
            self.showWarningBox('Warning','Please Login')
        else:
            try:
                # Get array of dictionaries on data variable
                aescheck = False
                self.getUserStorage()

                if aescheck:
                    RowN = int(self.RowN_input.text())
                    if (RowN > 0 and (RowN < (self.tableData.rowCount()+1))):
                        del(data[RowN-1])
                        self.postUserStorage()
                        self.execUpdateTable()
                        print("Success removing row data\n")
                    else:
                        print("> Error removing row: False input range")
                        self.showWarningBox('Warning',"Error removing row: \nInput row number out of bounds")
            except:
                print("Exception: Error removing row data")
                pass
         
    def execChangeKey(self):
        global data
        
        oldkey = self.OldKey_input.text()
        newkey = self.NewKey_input.text()
        confirmnewkey = self.ConfirmNewKey_input.text()
        if(headerr==""):
            self.showWarningBox('Warning','Please Login')
        else:
            ## Get data from database
            try:
                response = requests.get(url_api_get, verify=False, cookies=headerr)
                encrypted_data = response.text
            except:
                print("Get data error")

            # Storage value check
            if(response.ok): # Storage Filled
                # Check all Change Encryption Key columns
                if oldkey and newkey and confirmnewkey:
                    # Check old key
                    try:
                        data = eval((crypt.decrypt(encrypted_data,crypt.processDecryptKey(oldkey))).decode())
                        print("> Got data from server database")
                        # Confiming new key
                        if (newkey == confirmnewkey):
                            ## Encrypt and post data with new key
                            try:
                                temp = (crypt.encrypt(str(data).encode(),crypt.processDecryptKey(newkey)))
                                encrypted_data = temp.decode()
                                obj = {"storage":str(encrypted_data)}
                                requests.put(url_api_put, json = obj, verify=False, cookies=headerr)
                                print("> Data posted to server database")
                                self.showInformationBox('Success',"Encryption Key Setup Succesful \nEncryption key : " + newkey)
                            except:
                                print("Failed posting data to database")
                                self.showWarningBox('Warning',"Failed posting data to database")
                        else:
                            self.showWarningBox('Warning',"New key confirmation failed")
                    except:
                        print("Data evaluation failed")
                        print("Failed getting data from database: Incorrect old encryption key")
                        self.showWarningBox('Warning',"Failed getting data from database: \nIncorrect old encryption key")
                else:
                    self.showWarningBox('Warning',"Please fill all required column to change encryption key")
            else: # Storage Empty
                self.showWarningBox('Warning',"Storage Empty: \nPlease insert new password and new encryption key")

    def update_user_profile(self):
        global id_user

        if(headerr==""):
            self.showWarningBox('Warning','Please Login')
        else:
            try:
                ## Input new username and password form user
                print("Update User Account!")
                username = self.NewUsername_input.text()
                password = self.NewPassword_input.text()
                confirm_pass = self.ConfirmPassword_input.text()
                
                ## Create JSON object
                obj = {"name":username,"password":password}

                ## Input verification
                if((len(username))>0):
                    ## Update username or username & password
                    if(password == confirm_pass):
                        x = requests.put(url_api_updateacc, json=obj, verify=False, cookies=headerr)
                        self.showInformationBox('Update Successful',x.text)   
                        id_user = username 
                        self.activeuser_label.setText("Active User : "+id_user)
                        
                    else:
                        self.showWarningBox('Warning','Unmatched Password')
                else:
                    ## Update only password
                    if(password == confirm_pass):
                        x = requests.put(url_api_updateacc, json=obj, verify=False, cookies=headerr)
                        self.showInformationBox('Update Successful',x.text)    
                    else:
                        self.showWarningBox('Warning','Unmatched Password')                     
            except:
                print("Exception: Error updating user profile")
                pass

    def execLogOut(self):
        global headerr
        if(headerr==""):
            self.showWarningBox('Warning','Please Login')
        else:
            ## Log out confirmaion message
            result = self.showConfirmationBox("Log Out","Do you wish to log out?")
            if result:
                print("Logging out")
                try:
                    ## API request to log out
                    x = requests.get(url_api_logout, verify=False, cookies=headerr)
                    self.showInformationBox('Info : ',x.text)
                    ## Close application
                    QtCore.QCoreApplication.instance().quit()
                except:
                    print("Exception: Error log out")
                    pass
            else:
                print("Log out canceled")

    def execDeleteAccount(self):
        global headerr
        
        if(headerr==""):
            self.showWarningBox('Warning','Please Login')
        else:
            result = self.showConfirmationBox("Delete Account","Do you wish to PERMANENTLY remove your account and all data inside this account?")
            if result:
                ## Delete Account and logging out
                print("Deleting account")
                try:
                    x = requests.delete(url_api_delacc, verify=False, cookies=headerr)
                    self.showInformationBox('Delete Account',x.text)
                    QtCore.QCoreApplication.instance().quit()
                except:
                    print("Exception: Error delete account")
                    pass
            else:
                ## No
                print("canceled")

    def execAbout(self):
        self.showInformationBox('About',
        """Tugas Besar Perancangan Perangkat Lunak Jaringan\n 
        Dibuat oleh :\n
        - Laurensius Mario Surya (13216045)\n
        - Immanuel Hardjo (13216090)\n
        - Vincent Oktavian Kaulika (13216115)""")

    def showInformationBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def showWarningBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    
    def showConfirmationBox(self,title,message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        retval = msg.exec_()
        if retval == 16384:
            result = True
        else:
            result = False
        return result

    def retranslateUi_home(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Manager"))
        self.activeuser_label.setText(_translate("MainWindow", "Active User : "+id_user))
        item = self.tableData.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "servicename"))
        item = self.tableData.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "username"))
        item = self.tableData.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "password"))
        self.AESKey_label.setText(_translate("MainWindow", "Encryption Key"))
        self.UpdateTable_button.setText(_translate("MainWindow", "Refresh/Update Table"))
        self.AddNewPassword_label.setText(_translate("MainWindow", "Add Password"))
        self.Website_label.setText(_translate("MainWindow", "Servicename"))
        self.Username_label.setText(_translate("MainWindow", "Username"))
        self.Password_label.setText(_translate("MainWindow", "Password"))
        self.AddPassword_button.setText(_translate("MainWindow", "Add Password"))
        self.DeletePassword_label.setText(_translate("MainWindow", "Remove Password"))
        self.RowNumber_label.setText(_translate("MainWindow", "Row Number"))
        self.DeletePassword_button.setText(_translate("MainWindow", "Delete Password"))
        self.ChangeUserProfile.setText(_translate("MainWindow", "Change User Profile"))
        self.NewUsername_label.setText(_translate("MainWindow", "New Username"))
        self.NewPassword_label.setText(_translate("MainWindow", "New Password"))
        self.ConfirmPassword_label.setText(_translate("MainWindow", "Confirm Password"))
        self.CUP_Button.setText(_translate("MainWindow", "Submit"))
        self.ChangeAESKey.setText(_translate("MainWindow", "Change Encryption Key"))
        self.OldKey_label.setText(_translate("MainWindow", "Old Key"))
        self.NewKey_label.setText(_translate("MainWindow", "New Key"))
        self.ConfirmNewKey_label.setText(_translate("MainWindow", "Confirm New Key"))
        self.CAK_Button.setText(_translate("MainWindow", "Submit"))
        self.DeleteAccount.setText(_translate("MainWindow", "Delete Account"))
        self.DA_Button.setText(_translate("MainWindow", "DELETE ACCOUNT"))
        self.menuAccount.setTitle(_translate("MainWindow", "Account"))
        self.actionLogOut.setText(_translate("MainWindow", "Log Out"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app_home = QtWidgets.QApplication(sys.argv)
    MainWindow_home = QtWidgets.QMainWindow()
    ui_home = Ui_MainWindow_home()
    ui_home.setupUi_home(MainWindow_home)
    MainWindow_home.show()
    sys.exit(app_home.exec_())
