from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
import os

class MainWindow(QMainWindow):
    # === CONSTRUCTOR ===========================================================
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('src/uibuilder/Main.ui', self)
        self.pushButton.clicked.connect(self.toggleMenu)
        self.search_btn.clicked.connect(self.toggleMenu)
        self.import_btn.clicked.connect(self.openFileDialog)
        self.start_node = self.start_input.text()
        self.end_node = self.end_input.text()
        if self.radioButton.isChecked():
            self.algorithm = 1
        elif self.radioButton_2.isChecked():
            self.algorithm = 2
        
    def toggleMenu(self):
        if self.sidebar_container.pos().x() == 0:
            self.closeMenu()
        else:
            self.openMenu()

    def closeMenu(self):
        self.animation = QPropertyAnimation(self.sidebar_container, b"pos") 
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setStartValue(QPoint(0, 0))
        self.animation.setEndValue(QPoint(-321,0))
        self.animation.setDuration(200)
        self.animation.start()

    def openMenu(self):
        self.animation = QPropertyAnimation(self.sidebar_container, b"pos") 
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setStartValue(QPoint(-321, 0))
        self.animation.setEndValue(QPoint(0,0))
        self.animation.setDuration(200)
        self.animation.start()

    def openFileDialog(self):
        # Open the file dialog and get the selected file path
        self.filePath, _ = QFileDialog.getOpenFileName(self, 'Open file', '', 'Text files (*.txt)')
        self.fileName = os.path.basename(self.filePath)
        if self.filePath:
            self.file_label.setText(self.fileName)
        
        