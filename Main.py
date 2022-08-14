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
# Add Object to POS System
import UI.AddObjectPOS
# Edit object POS
import UI.EditObjectPOS
# Borrow or Return Object in POS System
import UI.Borrow_Return

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
        # MainWindow.setFixedHeight(270)
        # MainWindow.setFixedWidth(350)
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
        # self.widget_mainUI.setFixedWidth(1188)
        # self.widget_mainUI.setFixedHeight(700)
        self.widget_mainUI.show()
        # Set up button signal
        self.SetUpButtonMain()
        # set up table
        self.SetTableWidth()
        # initial load tab index
        self.LoadTabIndex()

    def SetTableWidth(self, table = None, width = []):
        if table == None:
            pass
        elif table == 'tableListuser':
            col = 0
            for col in range(self.ui_mainUI.tableListuser.columnCount()):
                getattr(self.ui_mainUI, table).setColumnWidth(col, width[col])
        elif table == 'tableListObject':
            for col in range(self.ui_mainUI.tableListObject.columnCount()):
                getattr(self.ui_mainUI, table).setColumnWidth(col, width[col])
        elif table == 'tableListBorrow':
            for col in range(self.ui_mainUI.tableListBorrow.columnCount()):
                getattr(self.ui_mainUI, table).setColumnWidth(col, width[col])
        
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
        self.ui_mainUI.refresh.clicked.connect(self.ClearTable_User)
        # -----> Object <-----
        self.ui_mainUI.tableListObject.clicked.connect(self.LoadTextInSelectedObject)
        # Add object in POS System
        self.ui_mainUI.addObj.clicked.connect(self.AddObjectToPOS)
        # Edit object in POS System
        self.ui_mainUI.editObj.clicked.connect(self.EditObjectInPOS)
        # Delete object in POS System
        self.ui_mainUI.deleteObj.clicked.connect(self.DeleteObjectInPOS)
        # Search object in POS System
        self.ui_mainUI.SearchObjList.clicked.connect(self.FilterObjectSearch)
        # Refresh button for load table
        self.ui_mainUI.refreshObj.clicked.connect(self.RefreshTableListObject)
        # When Borrow and Return button clicked
        self.ui_mainUI.borrow_or_return.clicked.connect(self.Borrow_Return_ObjectInPOS)
        
    def LoadTabIndex(self):
        self.TabIndex = self.ui_mainUI.tabWidget.currentIndex()
        # Tab index 2 it's mean User in POS system
        if self.TabIndex == 2:
            # disable edit user
            self.ui_mainUI.editUser.setEnabled(False)
            self.ui_mainUI.deleteUser.setEnabled(False)
            # GET User list in database
            # Load data to table
            self.LoadDataToTableUser()
        # Tab index 1 it's mean Borrow list in POS system
        elif self.TabIndex == 1:
            # Load data borrow list
            self.LoadDataToBorrowListTable()
        # Tab index 0 it's mean All object in POS system
        elif self.TabIndex == 0:
            # Disable edit Obj, Delete Obj
            obj_name = ['editObj', 'deleteObj']
            for i in obj_name:
                getattr(self.ui_mainUI, i).setEnabled(False)
            # Call load object list in Database
            self.LoadObjectListAll()
            
    # Load data to table of borrow list
    def LoadDataToBorrowListTable(self):
        self.SetTableWidth(table = 'tableListBorrow', width = [170, 250, 358, 50, 240])
        try:
            with open('setAPI.json', 'r') as f:
                data = json.load(f)
            url = str(data['borrowList'])
            # requet data from url
            rt = requests.get(url, timeout = 1)
            if rt.status_code == 200:
                data_rt = rt.json()
                self.ui_mainUI.tableListBorrow.setRowCount(len(data_rt))
                row = 0
                for dataBR in data_rt:
                    self.ui_mainUI.tableListBorrow.setItem(row, 0, QtWidgets.QTableWidgetItem(str(dataBR['UserID'])))
                    self.ui_mainUI.tableListBorrow.setItem(row, 1, QtWidgets.QTableWidgetItem(str(dataBR['ObjectID'])))
                    self.ui_mainUI.tableListBorrow.setItem(row, 2, QtWidgets.QTableWidgetItem(str(dataBR['ArticlesID'])))
                    self.ui_mainUI.tableListBorrow.setItem(row, 3, QtWidgets.QTableWidgetItem(str(dataBR['quality_borrow'])))
                    self.ui_mainUI.tableListBorrow.setItem(row, 4, QtWidgets.QTableWidgetItem(str(dataBR['update'])))
                    row += 1
                # Sorting item in table
                self.ui_mainUI.tableListBorrow.sortItems(0)
            elif rt.status_code == 404:
                self.AleartBoxError(description = 'Not found data in database')
        except:
            self.AleartBoxError(description = 'Error in load data to table')
    
    # Load data to table user
    def LoadDataToTableUser(self):
        # set table width
        self.SetTableWidth(table = 'tableListuser', width = [200, 408, 300, 160])
        try:
            with open('setAPI.json', 'r') as f:
                data = json.load(f)
            url = str(data['userList'])
            rt = requests.get(f'{url}', timeout = 1)
            data = rt.json()
            self.ui_mainUI.tableListuser.setRowCount(len(data))
            row = 0
            for person in data:
                self.ui_mainUI.tableListuser.setItem(row, 0, QtWidgets.QTableWidgetItem(person['barcode_user']))
                self.ui_mainUI.tableListuser.setItem(row, 1, QtWidgets.QTableWidgetItem(person['name_user']))
                self.ui_mainUI.tableListuser.setItem(row, 2, QtWidgets.QTableWidgetItem(person['mobile']))
                self.ui_mainUI.tableListuser.setItem(row, 3, QtWidgets.QTableWidgetItem(person['description']))
                row += 1
            self.ui_mainUI.tableListuser.sortItems(0)
        except:
            self.AleartBoxError(description = 'Can\'t connect to Server !')
                
    def LoadTextInSelected(self):
        row = self.ui_mainUI.tableListuser.currentRow()
        column = self.ui_mainUI.tableListuser.currentColumn()
        if column == 0:
            self.item_user = self.ui_mainUI.tableListuser.item(row, column)
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
        # self.widget_register_user.setFixedHeight(370)
        # self.widget_register_user.setFixedWidth(400)
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
                self.LoadDataToTableUser()
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
            rt = requests.get('{}{}' .format(str(url), str(self.item_user.text())), timeout = 1)
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
            rt = requests.put('{}{}' .format(url ,str(self.item_user.text())), data = {'barcode_user': self.ui_Edit_user.barcodeUser.text(), 'name_user': self.ui_Edit_user.fullname.text(), 'mobile': self.ui_Edit_user.mobilenumber.text(), 'description': self.ui_Edit_user.description.text()}, timeout = 1)
            if rt.status_code == 202:
                self.AleartBoxSuccess(description = 'Update user success !')
                # update table
                if self.ui_mainUI.StudentIDSearch.text() == '':
                    self.LoadDataToTableUser()
                elif self.ui_mainUI.StudentIDSearch.text() != '':
                    self.SearchUserInPOSSystem()
                self.widget_Edit_user.close()
            elif rt.status_code == 404:
                self.AleartBoxError(description = 'User not found !')
            elif rt.status_code == 400:
                self.AleartBoxError(description = 'Can\'t update user !')
        except:
            self.AleartBoxError(description = 'Can\'t connect to Server !')

# ----------> Delete User in POS <----------
    def DeleteUserInPOSSystem(self):
        # Confirm 
        ret =  self.AleartBoxConfirm(description = 'Do you want to delete {} ?' .format(self.item_user.text()))
        if ret:
            try:
                with open('setAPI.json', 'r') as f:
                    data = json.load(f)
                url = str(data['deleteUserPOS'])
                student_id = self.item_user.text()
                try:
                    # Delete user in database
                    rt = requests.delete('{}{}' .format(url, str(student_id)), timeout = 1)
                    if rt.status_code == 204:
                        self.AleartBoxSuccess(description = 'Delete user success !')
                        # update table
                        if self.ui_mainUI.StudentIDSearch.text() == '':
                            self.LoadDataToTableUser()
                        elif self.ui_mainUI.StudentIDSearch.text() != '':
                            self.SearchUserInPOSSystem()
                    elif rt.status_code == 404:
                        self.AleartBoxError(description = 'User not found !')
                except:
                    self.AleartBoxError(description = 'Can\'t connect to Server !')
            except:
                self.AleartBoxError(description = 'Can\'t open SetAPI.json !')
        elif not(ret):
            pass

# ----------> Search user in database <----------
    def SearchUserInPOSSystem(self):
        # set table width
        self.SetTableWidth(table = 'tableListuser', width = [200, 408, 300, 160])
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
                    self.ui_mainUI.tableListuser.setItem(row, 0, QtWidgets.QTableWidgetItem(person['barcode_user']))
                    self.ui_mainUI.tableListuser.setItem(row, 1, QtWidgets.QTableWidgetItem(person['name_user']))
                    self.ui_mainUI.tableListuser.setItem(row, 2, QtWidgets.QTableWidgetItem(person['mobile']))
                    self.ui_mainUI.tableListuser.setItem(row, 3, QtWidgets.QTableWidgetItem(person['description']))
                    row += 1
                self.ui_mainUI.tableListuser.sortItems(0)
            elif rt.status_code == 404:
                pass
        except:
            self.AleartBoxError(description = 'Can\'t connect to Server !')

    # Clear Table
    def ClearTable_User(self):
        try:
            # Clear line edit search
            self.ui_mainUI.StudentIDSearch.clear()
            # Load data to table again
            self.LoadDataToTableUser()
        except:
            self.AleartBoxError(description = 'Can\'t connect to Server !')

# ----------> Object list <----------

    def LoadObjectListAll(self):
        # Set size of table
        try:
            self.SetTableWidth(table = 'tableListObject', width = [200, 408, 300, 160])
        except:
            pass
        try:
            with open('setAPI.json', 'r') as f:
                alldata = json.load(f)
            url = str(alldata['listObj'])
            rt = requests.get('{}' .format(url), timeout = 1)
            if rt.status_code == 200:
                alldata = rt.json()
                self.ui_mainUI.tableListObject.setRowCount(len(alldata))
                row = 0
                for data in alldata:
                    obj_name = str(data['barcode_obj'])
                    durable_articles = str(data['durable_articles'])
                    stock = str(data['stock'])
                    allstock = str(data['all_stock'])
                    # stock it's equal None when stock it's haven't borrow by user
                    if stock == 'None':
                        stock = allstock
                    self.ui_mainUI.tableListObject.setItem(row, 0, QtWidgets.QTableWidgetItem(obj_name))
                    self.ui_mainUI.tableListObject.setItem(row, 1, QtWidgets.QTableWidgetItem(durable_articles))
                    self.ui_mainUI.tableListObject.setItem(row, 2, QtWidgets.QTableWidgetItem(stock))
                    self.ui_mainUI.tableListObject.setItem(row, 3, QtWidgets.QTableWidgetItem(allstock))
                    row += 1
                self.ui_mainUI.tableListObject.sortItems(0)
            elif rt.status_code == 404:
                self.AleartBoxError(description = 'Object not found !')
        except:
            self.AleartBoxError(description = 'Can\'t connect to Server !')

    # Load col and row in list object table
    def LoadTextInSelectedObject(self):
        row = self.ui_mainUI.tableListObject.currentRow()
        column = self.ui_mainUI.tableListObject.currentColumn()
        # obj list
        obj_list = ['editObj', 'deleteObj']
        if column == 0:
            self.item_obj = self.ui_mainUI.tableListObject.item(row, column)
            # if column == 1 it's mean that user click on student ID
            for i in obj_list:
                self.ui_mainUI.__dict__[i].setEnabled(True)
        else:
            for i in obj_list:
                self.ui_mainUI.__dict__[i].setEnabled(False)

# ----------> Add Object <----------
    def AddObjectToPOS(self):
        self.widget_addObject_POS = QtWidgets.QMainWindow()
        self.ui_addObject_POS = UI.AddObjectPOS.Ui_MainWindow()
        self.ui_addObject_POS.setupUi(self.widget_addObject_POS)
        self.widget_addObject_POS.setWindowTitle('Add Object')
        self.widget_addObject_POS.setWindowIcon(QtGui.QIcon(r'elec.png'))
        self.ui_addObject_POS.label_6.setPixmap(QtGui.QPixmap(r'elec.png'))
        # set up button signal
        self.widget_addObject_POS_setupButton()
        self.widget_addObject_POS.show()

    # Set up button signal
    def widget_addObject_POS_setupButton(self):
        # Button for add object to database
        self.ui_addObject_POS.addObject.clicked.connect(self.AddObjectToDatabase)
        
    def AddObjectToDatabase(self):
        barcode_obj = str(self.ui_addObject_POS.barcodeObj.text())
        articles = str(self.ui_addObject_POS.articles.text())
        allstock = str(self.ui_addObject_POS.fullstock.text())
        if allstock.isnumeric():
            allstock = int(allstock)
        else:
            self.AleartBoxError(description = 'All stock must be number !')
        # check student id is empty or not
        if barcode_obj != '' and allstock != '':
            with open('setAPI.json', 'r') as f:
                data = json.load(f)
            url = str(data['addObj'])
            st = requests.post(f'{url}', data = {'barcode_obj': barcode_obj, 'durable_articles': articles, 'stock': allstock, 'all_stock': allstock}, timeout = 1)
            if st.status_code == 201:
                self.AleartBoxSuccess(description = 'Register object success !')
                # Clear data in form
                self.ui_addObject_POS.barcodeObj.clear()
                self.ui_addObject_POS.articles.clear()
                self.ui_addObject_POS.fullstock.clear()
                # update table after add user 
                self.LoadObjectListAll()
            elif st.status_code == 302:
                self.AleartBoxError(description = 'Object already exist !')
            elif st.status_code == 400:
                self.AleartBoxError(description = 'Can\'t create object !')
        elif barcode_obj == '' or allstock == '':
            self.AleartBoxError(description = 'Please fill in all fields have RED Color !')

# -----------> Edit Object <----------
    def EditObjectInPOS(self):
        self.widget_EditObect_POS = QtWidgets.QMainWindow()
        self.ui_EditObject_POS = UI.EditObjectPOS.Ui_MainWindow()
        self.ui_EditObject_POS.setupUi(self.widget_EditObect_POS)
        self.widget_EditObect_POS.setWindowTitle('Edit Object')
        self.widget_EditObect_POS.setWindowIcon(QtGui.QIcon(r'elec.png'))
        self.ui_EditObject_POS.label_6.setPixmap(QtGui.QPixmap(r'elec.png'))
        # set up button signal
        self.widget_EditObect_POS_setupButton()
        # Load old data from database
        self.widget_EditObect_POS_loadOldData()
        self.widget_EditObect_POS.show()

    def widget_EditObect_POS_setupButton(self):
        self.ui_EditObject_POS.editconfirm.clicked.connect(self.EditObjectInDatabase)

    # load old data from database
    def widget_EditObect_POS_loadOldData(self):
        try:
            with open('setAPI.json', 'r') as f:
                data = json.load(f)
            url = str(data['loadDataOldBeforePUT_UpdateData'])
            # Load old data
            rt = requests.get(f'{url}{self.item_obj.text()}', timeout = 1)
            OldData = rt.json()
            # Old data load
            self.old_barcode = OldData['barcode_obj']
            old_articles = OldData['durable_articles']
            old_all_stock = OldData['all_stock']
            # Set Text in line edit, it's old data
            self.ui_EditObject_POS.barcodeObject.setText(str(self.old_barcode))
            self.ui_EditObject_POS.articles.setText(str(old_articles))
            self.ui_EditObject_POS.fullstock.setText(str(old_all_stock))
        except:
            self.AleartBoxError(description = 'Can\'t connect to Server !')

    def EditObjectInDatabase(self):
        # Get data from form
        try:
            new_barcode = str(self.ui_EditObject_POS.barcodeObject.text())
            new_articles = str(self.ui_EditObject_POS.articles.text())
            new_all_stock = str(self.ui_EditObject_POS.fullstock.text())
            if new_all_stock.isnumeric():
                new_all_stock = int(new_all_stock)
            else:
                self.AleartBoxError(description = 'All stock must be number !')
            if new_barcode != '' and new_all_stock != '':
                # update data in database with put method
                with open('setAPI.json', 'r') as f:
                    data = json.load(f)
                url = str(data['loadDataOldBeforePUT_UpdateData'])
                try:
                    rt = requests.put(f'{url}{self.old_barcode}', data = {'barcode_obj': new_barcode, 'durable_articles': new_articles, 'all_stock': new_all_stock}, timeout = 1)
                    if rt.status_code == 200:
                        self.AleartBoxSuccess(description = 'Edit object success !')
                        # update table after edit user
                        if self.ui_mainUI.ObjSearch.text() != '':
                            self.FilterObjectSearch()
                        elif self.ui_mainUI.ObjSearch.text() == '':
                            self.LoadObjectListAll()
                        # Close form
                        self.widget_EditObect_POS.close()
                    elif rt.status_code == 400:
                        self.AleartBoxError(description = 'Can\'t edit object !')
                except:
                    self.AleartBoxError(description = 'Can\'t connect to Server !')
        except:
            self.AleartBoxError(description = 'Something wrong !')

# ----------> Delete object in Database <----------
    def DeleteObjectInPOS(self):
        try:
            ret = self.AleartBoxConfirm(description = 'Are you sure to delete {} ?' .format(self.item_obj.text()))
            if ret:
                try:
                    with open('setAPI.json', 'r') as f:
                        data = json.load(f)
                    url = str(data['loadDataOldBeforePUT_UpdateData'])
                    rt = requests.delete(f'{url}{self.item_obj.text()}', timeout = 1)
                    if rt.status_code == 204:
                        self.AleartBoxSuccess(description = 'Delete object success !')
                        # update table after delete user
                        if self.ui_mainUI.ObjSearch.text() != '':
                            self.FilterObjectSearch()
                        elif self.ui_mainUI.ObjSearch.text() == '':
                            self.LoadObjectListAll()
                    elif rt.status_code == 404:
                        self.AleartBoxError(description = 'Object not found !')
                except:
                    self.AleartBoxError(description = 'Something wrong !')
        except:
            self.AleartBoxError(description = 'Can\'t connect to Server !')

# ----------> Filter Object <----------
    def FilterObjectSearch(self):
        try:
            text_search = self.ui_mainUI.ObjSearch.text()
            with open('setAPI.json', 'r') as f:
                data = json.load(f)
            url = str(data['filterObject'])
            rt = requests.get(f'{url}{text_search}', timeout = 1)
            if rt.status_code == 200:
                self.GetTableObject(alldata = rt.json())
            elif rt.status_code == 404:
                self.AleartBoxError(description = 'Object not found !')
        except:
            pass

    def GetTableObject(self, alldata):
        try:
            self.SetTableWidth(table = 'tableListObject', width = [200, 408, 300, 160])
        except:
            pass
        self.ui_mainUI.tableListObject.setRowCount(len(alldata))
        try:
            row = 0
            for data in alldata:
                obj_name = str(data['barcode_obj'])
                durable_articles = str(data['durable_articles'])
                stock = str(data['stock'])
                allstock = str(data['all_stock'])
                # stock it's equal None when stock it's haven't borrow by user
                if stock == 'None':
                    stock = allstock
                self.ui_mainUI.tableListObject.setItem(row, 0, QtWidgets.QTableWidgetItem(obj_name))
                self.ui_mainUI.tableListObject.setItem(row, 1, QtWidgets.QTableWidgetItem(durable_articles))
                self.ui_mainUI.tableListObject.setItem(row, 2, QtWidgets.QTableWidgetItem(stock))
                self.ui_mainUI.tableListObject.setItem(row, 3, QtWidgets.QTableWidgetItem(allstock))
                row += 1
            self.ui_mainUI.tableListObject.sortItems(0)
        except:
            self.AleartBoxError(description = 'Can\'t update table !')

# ----------> refresh list of table <----------
    def RefreshTableListObject(self):
        try:
            self.LoadObjectListAll()
            # clear text line edit of object search
            self.ui_mainUI.ObjSearch.clear()
        except:
            self.AleartBoxError(description = 'Can\'t refresh table !')
            
# ----------> Borrow object in POS System <----------
    def Borrow_Return_ObjectInPOS(self):
        self.widget_BorrowOrReturn_POS = QtWidgets.QMainWindow()
        self.ui_BorrowOrReturn_POS = UI.Borrow_Return.Ui_MainWindow()
        self.ui_BorrowOrReturn_POS.setupUi(self.widget_BorrowOrReturn_POS)
        self.widget_BorrowOrReturn_POS.setWindowTitle('Borrow or Return')
        self.widget_BorrowOrReturn_POS.setWindowIcon(QtGui.QIcon(r'elec.png'))
        self.ui_BorrowOrReturn_POS.label_8.setPixmap(QtGui.QPixmap(r'elec.png'))
        self.widget_BorrowOrReturn_POS.show()
        
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