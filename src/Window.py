from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import * 

class MainWindow(QMainWindow):
    # === CONSTRUCTOR ===========================================================
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('src/uibuilder/Main.ui', self)