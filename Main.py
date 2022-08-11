from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import requests
import json
import os
from pathlib import Path

# Login UI
from UI.Login import *
# Mainprogram
import UI.MainProgram
# Register user
import UI.AddUserInPOS
# Edit User POS
import UI.EditUserPOS

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]

class myUI(Ui_MainWindow):
    def __init__(self):
        super().setupUi(MainWindow)
        # Set image program
        try:
            self.label_4.setPixmap(QtGui.QPixmap(r'elec.png'))
        except:
            MainWindow.close()
        MainWindow.setWindowIcon(QtGui.QIcon(r'elec.png'))
        MainWindow.setWindowTitle('POS System By: {}' .format('Anurak'))
        MainWindow.setFixedHeight(240)
        MainWindow.setFixedWidth(350)
        # Setup button signal
        self.setUpButton()
        
    def setUpButton(self):
        self.loginBT.clicked.connect(self.LoginProcess)
        
    # Login to database
    def LoginProcess(self):
        username = str(self.Username.text())
        password = str(self.Password.text())
        if username == '' or password == '':
            self.AleartBoxError(description = 'Please fill in all fields !') 
        else:
            with open('setAPI.json', 'r') as f:
                data = json.load(f)
            url = str(data['login'])
            st = requests.post(f'{url}', data = {'username': username, 'password': password}, timeout = 1)    
            # Token
            self.Token = st.text
            if st.status_code == 200:
                self.AleartBoxSuccess(description = 'Login success !')
                # Close Login page
                MainWindow.close()
                # Open main program
                self.MainProgramStarted()
            elif st.status_code == 400:
                self.AleartBoxError(description = 'Username or password is incorrect !')
            else:
                self.AleartBoxError(description = 'Can\'t connect to Server !')
                MainWindow.close()
    
    # Aleartbox error
    def AleartBoxError(self, description):
        msg = QMessageBox()
        msg.setWindowTitle('Error !')
        msg.setWindowIcon(QtGui.QIcon(os.path.join(ROOT, r'imageIcon\error.png')))
        msg.setText(description)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        
    # Aleartbox Success 
    def AleartBoxSuccess(self, description):
        msg = QMessageBox()
        msg.setWindowTitle('Success !')
        msg.setWindowIcon(QtGui.QIcon(os.path.join(ROOT, r'imageIcon\success.png')))
        msg.setText(description)
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def AleartBoxConfirm(self, description):
        msg = QMessageBox()
        msg.setWindowTitle('Confirm ? ')
        msg.setWindowIcon(QtGui.QIcon(os.path.join(ROOT, r'imageIcon\question.png')))
        msg.setText(description)
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # ret is signal from clicked button
        ret = msg.exec_()
        if ret == QMessageBox.Yes:
            return True
        elif ret == QMessageBox.No:
            return False
        
    def show(self):
        MainWindow.show()
        sys.exit(app.exec_())
        
    def close(self):
        MainWindow.close()
        
# ----------> Main Program <----------
    def MainProgramStarted(self):
        self.widget_mainUI = QtWidgets.QMainWindow()
        self.ui_mainUI = UI.MainProgram.Ui_MainWindow()
        self.ui_mainUI.setupUi(self.widget_mainUI)
        self.widget_mainUI.setWindowTitle('POS ELECTRONICS BY : Anurak')
        self.widget_mainUI.setWindowIcon(QtGui.QIcon(r'elec.png'))
        self.widget_mainUI.setFixedWidth(1188)
        self.widget_mainUI.setFixedHeight(700)
        self.widget_mainUI.show()
        # Set up button signal
        self.SetUpButtonMain()
        # set up table
        self.SetTableWidth()

    def SetTableWidth(self):
        self.ui_mainUI.tableListuser.setColumnWidth(0, 50)
        self.ui_mainUI.tableListuser.setColumnWidth(1, 200)
        self.ui_mainUI.tableListuser.setColumnWidth(2, 408)
        self.ui_mainUI.tableListuser.setColumnWidth(3, 300)
        self.ui_mainUI.tableListuser.setColumnWidth(4, 160)
        
    # Setup button main program
    def SetUpButtonMain(self):
        # Close program in main program
        self.ui_mainUI.actionClose_Program.triggered.connect(self.closeProgram)
        # Edit user in POS System
        self.ui_mainUI.editUser.clicked.connect(self.EditUserInPOSSystem)
        # All user POS Tab
        self.ui_mainUI.addUser.clicked.connect(self.StartRegisterUser)
        # Tab signal
        self.ui_mainUI.tabWidget.currentChanged.connect(self.LoadTabIndex)
        # signal in table widget
        self.ui_mainUI.tableListuser.clicked.connect(self.LoadTextInSelected)
        # Delete user in POS System
        self.ui_mainUI.deleteUser.clicked.connect(self.DeleteUserInPOSSystem)
        # Search user in POS Syetem
        self.ui_mainUI.SearchUserList.clicked.connect(self.SearchUserInPOSSystem)
        # Refresh button for load table
        self.ui_mainUI.refresh.clicked.connect(self.ClearTable)
        
    def LoadTabIndex(self):
        self.TabIndex = self.ui_mainUI.tabWidget.currentIndex()
        if self.TabIndex == 2:
            # disable edit user
            self.ui_mainUI.editUser.setEnabled(False)
            self.ui_mainUI.deleteUser.setEnabled(False)
            # GET User list in database
            # Load data to table
            self.LoadDataToTable()
            
    def LoadDataToTable(self):
        # set table width
        self.SetTableWidth()
        try:
            with open('setAPI.json', 'r') as f:
                data = json.load(f)
            url = str(data['userList'])
            rt = requests.get(f'{url}', timeout = 1)
            data = rt.json()
            self.ui_mainUI.tableListuser.setRowCount(len(data))
            row = 0
            for person in data:
                self.ui_mainUI.tableListuser.setItem(row, 0, QtWidgets.QTableWidgetItem(str(row)))
                self.ui_mainUI.tableListuser.setItem(row, 1, QtWidgets.QTableWidgetItem(person['barcode_user']))
                self.ui_mainUI.tableListuser.setItem(row, 2, QtWidgets.QTableWidgetItem(person['name_user']))
                self.ui_mainUI.tableListuser.setItem(row, 3, QtWidgets.QTableWidgetItem(person['mobile']))
                self.ui_mainUI.tableListuser.setItem(row, 4, QtWidgets.QTableWidgetItem(person['description']))
                row += 1
        except:
            self.AleartBoxError(description = 'Can\'t connect to Server !')
                
    def LoadTextInSelected(self):
        row = self.ui_mainUI.tableListuser.currentRow()
        column = self.ui_mainUI.tableListuser.currentColumn()
        if column == 1:
            self.item = self.ui_mainUI.tableListuser.item(row, column)
            # if column == 1 it's mean that user click on student ID
            self.ui_mainUI.editUser.setEnabled(True)
            self.ui_mainUI.deleteUser.setEnabled(True)
        else:
            self.ui_mainUI.editUser.setEnabled(False)
            self.ui_mainUI.deleteUser.setEnabled(False)
        
# ----------> Register User in POS <----------  
    def StartRegisterUser(self):
        self.widget_register_user = QtWidgets.QMainWindow()
        self.ui_register_user = UI.AddUserInPOS.Ui_MainWindow()
        self.ui_register_user.setupUi(self.widget_register_user)
        self.widget_register_user.setWindowTitle('Register User')
        self.widget_register_user.setWindowIcon(QtGui.QIcon(r'elec.png'))
        try:
            self.ui_register_user.label_6.setPixmap(QtGui.QPixmap(r'elec.png'))
        except:
            pass
        self.widget_register_user.setFixedHeight(370)
        self.widget_register_user.setFixedWidth(400)
        # Set up button signal
        self.widget_register_user_setUpButton()
        self.widget_register_user.show()
        
    def widget_register_user_setUpButton(self):
        self.ui_register_user.addUser.clicked.connect(self.AddUserInPOSSystem)
        
    def AddUserInPOSSystem(self):
        student_id = str(self.ui_register_user.barcodeUser.text())
        student_name = str(self.ui_register_user.fullname.text())
        mobile = str(self.ui_register_user.mobilenumber.text())
        des = str(self.ui_register_user.description.text())
        # check student id is empty or not
        if student_id != '' and student_name != '' and mobile != '':
            with open('setAPI.json', 'r') as f:
                data = json.load(f)
            url = str(data['addUserPOS'])
            st = requests.post(f'{url}', data = {'barcode_user': student_id, 'name_user': student_name, 'mobile': mobile, 'description': des}, timeout = 1)
            if st.status_code == 201:
                self.AleartBoxSuccess(description = 'Register user success !')
                # Clear data in form
                self.ui_register_user.barcodeUser.clear()
                self.ui_register_user.fullname.clear()
                self.ui_register_user.mobilenumber.clear()
                self.ui_register_user.description.clear()
                # update table after add user 
                self.LoadDataToTable()
            elif st.status_code == 302:
                self.AleartBoxError(description = 'User already exist !')
            elif st.status_code == 400:
                self.AleartBoxError(description = 'Can\'t connect to Server !')
        elif student_id == '' or student_name == '' or mobile == '':
            self.AleartBoxError(description = 'Please fill in all fields have RED Color !')
            
# ----------> Edit User in POS <----------
    def EditUserInPOSSystem(self):
        self.widget_Edit_user = QtWidgets.QMainWindow()
        self.ui_Edit_user = UI.EditUserPOS.Ui_MainWindow()
        self.ui_Edit_user.setupUi(self.widget_Edit_user)
        self.widget_Edit_user.setWindowTitle('Edit User')
        self.widget_Edit_user.setWindowIcon(QtGui.QIcon(r'elec.png'))
        # Load old data 
        self.LoadOldDataFromDatabase()
        # set up button signal
        self.widget_Edit_user_setupButton()
        self.widget_Edit_user.show()

    def LoadOldDataFromDatabase(self):
        try:
            with open('setAPI.json', 'r') as f:
                data = json.load(f)
            url = str(data['LoadOldData'])
            rt = requests.get('{}{}' .format(str(url), str(self.item.text())), timeout = 1)
            if rt.status_code == 200:
                data = rt.json()
                # Student ID
                self.ui_Edit_user.barcodeUser.setText(data['barcode_user'])
                # Name
                self.ui_Edit_user.fullname.setText(data['name_user'])
                # mobile number
                self.ui_Edit_user.mobilenumber.setText(data['mobile'])
                # description
                self.ui_Edit_user.description.setText(data['description'])
            elif rt.status_code == 404:
                self.AleartBoxError(description = 'User not found !')
        except:
            self.AleartBoxError(description = 'Can\'t connect to Server !')
            
    def widget_Edit_user_setupButton(self):
        self.ui_Edit_user.editconfirm.clicked.connect(self.UpdateDataToDatabase)
        
    def UpdateDataToDatabase(self):
        try:
            with open('setAPI.json', 'r') as f:
                data = json.load(f)
            url = str(data['UpdataData'])
            rt = requests.put('{}{}' .format(url ,str(self.item.text())), data = {'barcode_user': self.ui_Edit_user.barcodeUser.text(), 'name_user': self.ui_Edit_user.fullname.text(), 'mobile': self.ui_Edit_user.mobilenumber.text(), 'description': self.ui_Edit_user.description.text()}, timeout = 1)
            if rt.status_code == 202:
                self.AleartBoxSuccess(description = 'Update user success !')
                # update table
                self.LoadDataToTable()
                self.widget_Edit_user.close()
            elif rt.status_code == 404:
                self.AleartBoxError(description = 'User not found !')
            elif rt.status_code == 400:
                self.AleartBoxError(description = 'Can\'t update user !')
        except:
            self.AleartBoxError(description = 'Can\'t connect to Server !')

# ----------> Delete User in POS <----------
    def DeleteUserInPOSSystem(self):
        try:
            with open('setAPI.json', 'r') as f:
                data = json.load(f)
            url = str(data['deleteUserPOS'])
            student_id = self.item.text()
            try:
                # Delete user in database
                rt = requests.delete('{}{}' .format(url, str(student_id)), timeout = 1)
                if rt.status_code == 204:
                    self.AleartBoxSuccess(description = 'Delete user success !')
                    # update table
                    self.LoadDataToTable()
                elif rt.status_code == 404:
                    self.AleartBoxError(description = 'User not found !')
            except:
                self.AleartBoxError(description = 'Can\'t connect to Server !')
        except:
            self.AleartBoxError(description = 'Can\'t open SetAPI.json !')

# ----------> Search user in database <----------
    def SearchUserInPOSSystem(self):
        # set table width
        self.SetTableWidth()
        # Load text from line edit
        text_filter = str(self.ui_mainUI.StudentIDSearch.text())
        try:
            with open('setAPI.json', 'r') as f:
                data = json.load(f)
            url = str(data['filterUser'])
            rt = requests.get('{}{}' .format(url, str(text_filter)), timeout = 1)
            if rt.status_code == 200:
                data = rt.json()
                self.ui_mainUI.tableListuser.setRowCount(len(data))
                row = 0
                for person in data:
                    self.ui_mainUI.tableListuser.setItem(row, 0, QtWidgets.QTableWidgetItem(str(row)))
                    self.ui_mainUI.tableListuser.setItem(row, 1, QtWidgets.QTableWidgetItem(person['barcode_user']))
                    self.ui_mainUI.tableListuser.setItem(row, 2, QtWidgets.QTableWidgetItem(person['name_user']))
                    self.ui_mainUI.tableListuser.setItem(row, 3, QtWidgets.QTableWidgetItem(person['mobile']))
                    self.ui_mainUI.tableListuser.setItem(row, 4, QtWidgets.QTableWidgetItem(person['description']))
                    row += 1
            elif rt.status_code == 404:
                pass
        except:
            self.AleartBoxError(description = 'Can\'t connect to Server !')

    # Clear Table
    def ClearTable(self):
        try:
            # Clear line edit search
            self.ui_mainUI.StudentIDSearch.clear()
            # Load data to table again
            self.LoadDataToTable()
        except:
            self.AleartBoxError(description = 'Can\'t connect to Server !')
        
# ----------> Close Program <----------
    def closeProgram(self):
        try:
            MainWindow.close()
        except:
            pass
        try:
            self.widget_mainUI.close()
        except:
            pass
        try:
            self.widget_register_user.close()
        except:
            pass
        sys.exit(app.exec_())

obj = myUI()

if __name__ == '__main__':
    MainWindow.show()
    sys.exit(app.exec_())