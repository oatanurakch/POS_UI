from cgitb import text
from ctypes import alignment
from this import d
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

# google sheet api
from connection import LoadNameUserInSheet, updatedata

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
        # Load initial User
        self.data_User = LoadNameUserInSheet()
        
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
        # Tab signal
        self.ui_mainUI.tabWidget.currentChanged.connect(self.LoadTabIndex)
        # Search user in POS Syetem
        self.ui_mainUI.SearchUserList.clicked.connect(self.SearchUserInPOSSystem)
        # Signal when click in line edit
        self.ui_mainUI.StudentIDSearch.editingFinished.connect(self.SearchUserInPOSSystem)
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
                    # Set Alignment center for quality of borrow list
                    item_Alignment = QtWidgets.QTableWidgetItem(str(dataBR['quality_borrow']))
                    item_Alignment.setTextAlignment(4)
                    self.ui_mainUI.tableListBorrow.setItem(row, 3, item_Alignment)
                    self.ui_mainUI.tableListBorrow.setItem(row, 4, QtWidgets.QTableWidgetItem((str(dataBR['update'])).split('.')[0]))
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
            self.data_User = LoadNameUserInSheet()
            self.ui_mainUI.tableListuser.setRowCount(len(self.data_User))
            row = 0
            for person in self.data_User:
                self.ui_mainUI.tableListuser.setItem(row, 0, QtWidgets.QTableWidgetItem(person[0]))
                self.ui_mainUI.tableListuser.setItem(row, 1, QtWidgets.QTableWidgetItem(person[1]))
                self.ui_mainUI.tableListuser.setItem(row, 2, QtWidgets.QTableWidgetItem(person[2]))
                self.ui_mainUI.tableListuser.setItem(row, 3, QtWidgets.QTableWidgetItem(person[3]))
                row += 1 
            self.ui_mainUI.tableListuser.sortItems(0)
        except:
            self.AleartBoxError(description = 'Can\'t connect to Server !')

# ----------> Search user in database <----------
    def SearchUserInPOSSystem(self):
        # set table width
        self.SetTableWidth(table = 'tableListuser', width = [200, 408, 300, 160])
        # Load text from line edit
        text_filter = str(self.ui_mainUI.StudentIDSearch.text())
        try:
            
            # Searching in table
            self.find_data = []
            for i in self.data_User:
                if i[0].startswith(text_filter) or i[1].startswith(text_filter) or text_filter in i[0] or text_filter in i[1]:
                    self.find_data.append(i)
            
            # Append in table
            self.ui_mainUI.tableListuser.setRowCount(len(self.find_data))
            row = 0
            for person in self.find_data:
                self.ui_mainUI.tableListuser.setItem(row, 0, QtWidgets.QTableWidgetItem(person[0]))
                self.ui_mainUI.tableListuser.setItem(row, 1, QtWidgets.QTableWidgetItem(person[1]))
                self.ui_mainUI.tableListuser.setItem(row, 2, QtWidgets.QTableWidgetItem(person[2]))
                self.ui_mainUI.tableListuser.setItem(row, 3, QtWidgets.QTableWidgetItem(person[3]))
                row += 1
            self.ui_mainUI.tableListuser.sortItems(0)
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
                    # Set alignment data in table
                    list_alignCenter = [QtWidgets.QTableWidgetItem(str(i)) for i in [stock, allstock]]
                    for item in list_alignCenter:
                        # setTextAlignment(4) # 4 it's center of cell
                        item.setTextAlignment(4)
                    self.ui_mainUI.tableListObject.setItem(row, 0, QtWidgets.QTableWidgetItem(obj_name))
                    self.ui_mainUI.tableListObject.setItem(row, 1, QtWidgets.QTableWidgetItem(durable_articles))
                    self.ui_mainUI.tableListObject.setItem(row, 2, list_alignCenter[0])
                    self.ui_mainUI.tableListObject.setItem(row, 3, list_alignCenter[1])
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
                # Set alignment data in table
                list_alignCenter = [QtWidgets.QTableWidgetItem(str(i)) for i in [stock, allstock]]
                for item in list_alignCenter:
                    # setTextAlignment(4) # 4 it's center of cell
                    item.setTextAlignment(4)
                self.ui_mainUI.tableListObject.setItem(row, 0, QtWidgets.QTableWidgetItem(obj_name))
                self.ui_mainUI.tableListObject.setItem(row, 1, QtWidgets.QTableWidgetItem(durable_articles))
                self.ui_mainUI.tableListObject.setItem(row, 2, list_alignCenter[0])
                self.ui_mainUI.tableListObject.setItem(row, 3, list_alignCenter[1])
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
        # set up button signal
        self.SetUp_Ui_BorrowOrReturn_POS()

    def SetUp_Ui_BorrowOrReturn_POS(self):
        # Barcode of user
        self.ui_BorrowOrReturn_POS.barcodeUser.returnPressed.connect(self.GetNameByBarcode)
        # Borrow button
        self.ui_BorrowOrReturn_POS.borrowObject.clicked.connect(self.BorrowObject)
        # Retrun button
        self.ui_BorrowOrReturn_POS.returnObject.clicked.connect(self.ReturnObject)

    # Load name of user by barcode
    def GetNameByBarcode(self):
        try:
            # Load name and other data from self.user_data
            try:
                state = False
                # Searching user with Student ID
                for i in self.data_User:
                    if i[0] == self.ui_BorrowOrReturn_POS.barcodeUser.text():
                        # Set text name of user
                        self.ui_BorrowOrReturn_POS.fullname_2.setText(i[1])
                        state = True
                if not state:
                    # Aleart box for notify user that user not found
                    self.AleartBoxError(description = 'User not found !')
                    try:
                        # Clear user text in line edit
                        self.ui_BorrowOrReturn_POS.barcodeUser.clear()
                    except:
                        pass
                    try:
                        # Clear Full name
                        self.ui_BorrowOrReturn_POS.fullname_2.clear()
                    except:
                        pass
                
            except:
                self.AleartBoxError(description = 'Can\'t connect to Server !')
        except:
            self.AleartBoxError(description = 'Can\'t load json !')
            
    def BorrowObject(self):
        # Load list of object in database with API
        try:
            with open('setAPI.json', 'r') as f:
                data = json.load(f)
            url = str(data['addBorrow'])
            # Check if user or some line edit not found
            if self.ui_BorrowOrReturn_POS.barcodeUser.text() == '' or self.ui_BorrowOrReturn_POS.barcodeObj_2.text() == '' or self.ui_BorrowOrReturn_POS.fullname_2.text() == '':
                self.AleartBoxError(description = 'Please fill all edit line !')
            else:
                # Add object to database with API
                rt = requests.post(url, data = {'ID': self.ui_BorrowOrReturn_POS.barcodeUser.text(), 'OBJID': self.ui_BorrowOrReturn_POS.barcodeObj_2.text(), 'QUALITY' : int(self.ui_BorrowOrReturn_POS.fullstock_2.text())}, timeout = 1)
                if rt.status_code == 201:
                    self.AleartBoxSuccess(description = 'Borrow object success !')
                    self.ui_BorrowOrReturn_POS.barcodeObj_2.clear()
                elif rt.status_code == 404:
                    self.AleartBoxError(description = 'Object not found !')
                elif rt.status_code == 400:
                    self.AleartBoxError(description = 'Object already borrow !')
                elif rt.status_code == 410:
                    self.AleartBoxError(description = 'Stock not update !')
                elif rt.status_code == 304:
                    self.AleartBoxError(description = 'Stock not enough !')
        except: pass
        
    def ReturnObject(self):
        try:
            with open('setAPI.json', 'r') as f:
                data = json.load(f)
            url = str(data['returnObject'])
            if self.ui_BorrowOrReturn_POS.barcodeUser.text() == '' or self.ui_BorrowOrReturn_POS.barcodeObj_2.text() == '' or self.ui_BorrowOrReturn_POS.fullname_2.text() == '':
                self.AleartBoxError(description = 'Please fill all edit line !')
            else:
                # Add object to database with API
                rt = requests.post(url, data = {'ID': self.ui_BorrowOrReturn_POS.barcodeUser.text(), 'OBJID': self.ui_BorrowOrReturn_POS.barcodeObj_2.text(), 'QUALITY' : int(self.ui_BorrowOrReturn_POS.fullstock_2.text())}, timeout = 1)
                if rt.status_code == 202:
                    self.AleartBoxSuccess(description = 'Return object success !')
                    self.ui_BorrowOrReturn_POS.barcodeObj_2.clear()
                elif rt.status_code == 404:
                    self.AleartBoxError(description = 'Object not found !')
                elif rt.status_code == 400:
                    self.AleartBoxError(description = 'Object already borrow !')
                elif rt.status_code == 410:
                    self.AleartBoxError(description = 'Stock not update !')
                elif rt.status_code == 304:
                    self.AleartBoxError(description = 'Return over quality !')
        except: pass 

        
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