from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import requests

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

# Login page
from Main import myUI
obj = myUI()
obj.show()



