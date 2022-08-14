# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1188, 716)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.AllObj = QtWidgets.QWidget()
        self.AllObj.setObjectName("AllObj")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.AllObj)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.addObj = QtWidgets.QPushButton(self.AllObj)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addObj.setFont(font)
        self.addObj.setObjectName("addObj")
        self.gridLayout_3.addWidget(self.addObj, 0, 0, 1, 1)
        self.editObj = QtWidgets.QPushButton(self.AllObj)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.editObj.setFont(font)
        self.editObj.setObjectName("editObj")
        self.gridLayout_3.addWidget(self.editObj, 0, 1, 1, 1)
        self.deleteObj = QtWidgets.QPushButton(self.AllObj)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.deleteObj.setFont(font)
        self.deleteObj.setObjectName("deleteObj")
        self.gridLayout_3.addWidget(self.deleteObj, 0, 2, 1, 1)
        self.loss_or_broke = QtWidgets.QPushButton(self.AllObj)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loss_or_broke.sizePolicy().hasHeightForWidth())
        self.loss_or_broke.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.loss_or_broke.setFont(font)
        self.loss_or_broke.setObjectName("loss_or_broke")
        self.gridLayout_3.addWidget(self.loss_or_broke, 0, 3, 1, 1)
        self.borrow_or_return = QtWidgets.QPushButton(self.AllObj)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.borrow_or_return.sizePolicy().hasHeightForWidth())
        self.borrow_or_return.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.borrow_or_return.setFont(font)
        self.borrow_or_return.setObjectName("borrow_or_return")
        self.gridLayout_3.addWidget(self.borrow_or_return, 0, 4, 1, 1)
        self.ObjSearch = QtWidgets.QLineEdit(self.AllObj)
        self.ObjSearch.setObjectName("ObjSearch")
        self.gridLayout_3.addWidget(self.ObjSearch, 0, 5, 1, 1)
        self.SearchObjList = QtWidgets.QPushButton(self.AllObj)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchObjList.sizePolicy().hasHeightForWidth())
        self.SearchObjList.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SearchObjList.setFont(font)
        self.SearchObjList.setObjectName("SearchObjList")
        self.gridLayout_3.addWidget(self.SearchObjList, 0, 6, 1, 1)
        self.refreshObj = QtWidgets.QPushButton(self.AllObj)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refreshObj.sizePolicy().hasHeightForWidth())
        self.refreshObj.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.refreshObj.setFont(font)
        self.refreshObj.setObjectName("refreshObj")
        self.gridLayout_3.addWidget(self.refreshObj, 0, 7, 1, 1)
        self.tableListObject = QtWidgets.QTableWidget(self.AllObj)
        self.tableListObject.setAutoScroll(True)
        self.tableListObject.setAutoScrollMargin(16)
        self.tableListObject.setObjectName("tableListObject")
        self.tableListObject.setColumnCount(4)
        self.tableListObject.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableListObject.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListObject.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListObject.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListObject.setHorizontalHeaderItem(3, item)
        self.tableListObject.horizontalHeader().setCascadingSectionResizes(False)
        self.tableListObject.horizontalHeader().setMinimumSectionSize(36)
        self.gridLayout_3.addWidget(self.tableListObject, 1, 0, 1, 8)
        self.tabWidget.addTab(self.AllObj, "")
        self.Obj_br = QtWidgets.QWidget()
        self.Obj_br.setObjectName("Obj_br")
        self.tableListBorrow = QtWidgets.QTableWidget(self.Obj_br)
        self.tableListBorrow.setGeometry(QtCore.QRect(10, 20, 1138, 564))
        self.tableListBorrow.setAutoScroll(True)
        self.tableListBorrow.setAutoScrollMargin(16)
        self.tableListBorrow.setObjectName("tableListBorrow")
        self.tableListBorrow.setColumnCount(4)
        self.tableListBorrow.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableListBorrow.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListBorrow.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListBorrow.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListBorrow.setHorizontalHeaderItem(3, item)
        self.tableListBorrow.horizontalHeader().setCascadingSectionResizes(False)
        self.tableListBorrow.horizontalHeader().setMinimumSectionSize(36)
        self.tabWidget.addTab(self.Obj_br, "")
        self.UserTab = QtWidgets.QWidget()
        self.UserTab.setObjectName("UserTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.UserTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.deleteUser = QtWidgets.QPushButton(self.UserTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.deleteUser.setFont(font)
        self.deleteUser.setObjectName("deleteUser")
        self.gridLayout_2.addWidget(self.deleteUser, 0, 2, 1, 1)
        self.StudentIDSearch = QtWidgets.QLineEdit(self.UserTab)
        self.StudentIDSearch.setObjectName("StudentIDSearch")
        self.gridLayout_2.addWidget(self.StudentIDSearch, 0, 3, 1, 1)
        self.editUser = QtWidgets.QPushButton(self.UserTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.editUser.setFont(font)
        self.editUser.setObjectName("editUser")
        self.gridLayout_2.addWidget(self.editUser, 0, 1, 1, 1)
        self.SearchUserList = QtWidgets.QPushButton(self.UserTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchUserList.sizePolicy().hasHeightForWidth())
        self.SearchUserList.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SearchUserList.setFont(font)
        self.SearchUserList.setObjectName("SearchUserList")
        self.gridLayout_2.addWidget(self.SearchUserList, 0, 4, 1, 1)
        self.addUser = QtWidgets.QPushButton(self.UserTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addUser.setFont(font)
        self.addUser.setObjectName("addUser")
        self.gridLayout_2.addWidget(self.addUser, 0, 0, 1, 1)
        self.refresh = QtWidgets.QPushButton(self.UserTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refresh.sizePolicy().hasHeightForWidth())
        self.refresh.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.refresh.setFont(font)
        self.refresh.setObjectName("refresh")
        self.gridLayout_2.addWidget(self.refresh, 0, 5, 1, 1)
        self.tableListuser = QtWidgets.QTableWidget(self.UserTab)
        self.tableListuser.setAutoScroll(True)
        self.tableListuser.setAutoScrollMargin(16)
        self.tableListuser.setObjectName("tableListuser")
        self.tableListuser.setColumnCount(4)
        self.tableListuser.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableListuser.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListuser.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListuser.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListuser.setHorizontalHeaderItem(3, item)
        self.tableListuser.horizontalHeader().setCascadingSectionResizes(False)
        self.tableListuser.horizontalHeader().setMinimumSectionSize(36)
        self.gridLayout_2.addWidget(self.tableListuser, 1, 0, 1, 6)
        self.tabWidget.addTab(self.UserTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1188, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuStore_manage_User = QtWidgets.QMenu(self.menuMenu)
        self.menuStore_manage_User.setObjectName("menuStore_manage_User")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRegister_Object = QtWidgets.QAction(MainWindow)
        self.actionRegister_Object.setObjectName("actionRegister_Object")
        self.actionClose_Program = QtWidgets.QAction(MainWindow)
        self.actionClose_Program.setObjectName("actionClose_Program")
        self.actionRegister_User_2 = QtWidgets.QAction(MainWindow)
        self.actionRegister_User_2.setObjectName("actionRegister_User_2")
        self.actionEdit_User = QtWidgets.QAction(MainWindow)
        self.actionEdit_User.setObjectName("actionEdit_User")
        self.actionRemove_User = QtWidgets.QAction(MainWindow)
        self.actionRemove_User.setObjectName("actionRemove_User")
        self.actionCreate_User = QtWidgets.QAction(MainWindow)
        self.actionCreate_User.setObjectName("actionCreate_User")
        self.actionEdit_User_2 = QtWidgets.QAction(MainWindow)
        self.actionEdit_User_2.setObjectName("actionEdit_User_2")
        self.menuStore_manage_User.addAction(self.actionCreate_User)
        self.menuStore_manage_User.addAction(self.actionEdit_User_2)
        self.menuMenu.addAction(self.actionRegister_Object)
        self.menuMenu.addAction(self.menuStore_manage_User.menuAction())
        self.menuMenu.addAction(self.actionClose_Program)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addObj.setText(_translate("MainWindow", "เพิ่มรายการ"))
        self.editObj.setText(_translate("MainWindow", "แก้ไขรายการ"))
        self.deleteObj.setText(_translate("MainWindow", "ลบรายการ"))
        self.loss_or_broke.setText(_translate("MainWindow", "แจ้งเสีย / สูญหาย"))
        self.borrow_or_return.setText(_translate("MainWindow", "แจ้งยืม / คืน"))
        self.SearchObjList.setText(_translate("MainWindow", "Search"))
        self.refreshObj.setText(_translate("MainWindow", "Refresh"))
        self.tableListObject.setSortingEnabled(False)
        item = self.tableListObject.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "รายการ"))
        item = self.tableListObject.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "เลขครุภัณฑ์"))
        item = self.tableListObject.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "คงเหลือ"))
        item = self.tableListObject.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ทั้งหมด"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AllObj), _translate("MainWindow", "รายการวัสดุทั้งหมด"))
        self.tableListBorrow.setSortingEnabled(False)
        item = self.tableListBorrow.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "รหัสผู้ใช้งาน"))
        item = self.tableListBorrow.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "รายการ"))
        item = self.tableListBorrow.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "เลขครุภัณฑ์"))
        item = self.tableListBorrow.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "จำนวน"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Obj_br), _translate("MainWindow", "รายการวัสดุที่ถูกยืม"))
        self.deleteUser.setText(_translate("MainWindow", "ลบผู้ใช้งาน"))
        self.editUser.setText(_translate("MainWindow", "แก้ไขผู้ใช้งาน"))
        self.SearchUserList.setText(_translate("MainWindow", "Search"))
        self.addUser.setText(_translate("MainWindow", "เพิ่มผู้ใช้งาน"))
        self.refresh.setText(_translate("MainWindow", "Refresh"))
        self.tableListuser.setSortingEnabled(False)
        item = self.tableListuser.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "รหัสผู้ใช้งาน"))
        item = self.tableListuser.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ชื่อ - นามสกุล"))
        item = self.tableListuser.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "เบอร์โทรศัพท์"))
        item = self.tableListuser.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "หมายเหตุ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.UserTab), _translate("MainWindow", "รายชื่อผู้ใช้งานในระบบ"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuStore_manage_User.setTitle(_translate("MainWindow", "Store manage User"))
        self.actionRegister_Object.setText(_translate("MainWindow", "Register Object"))
        self.actionClose_Program.setText(_translate("MainWindow", "Close Program"))
        self.actionRegister_User_2.setText(_translate("MainWindow", "Register User"))
        self.actionEdit_User.setText(_translate("MainWindow", "Edit User"))
        self.actionRemove_User.setText(_translate("MainWindow", "Remove User"))
        self.actionCreate_User.setText(_translate("MainWindow", "Create User "))
        self.actionEdit_User_2.setText(_translate("MainWindow", "Edit User"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
