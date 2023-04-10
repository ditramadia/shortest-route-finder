from PyQt5.uic import loadUi
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
import os
import Controller

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('src/uibuilder/Main.ui', self)
        self.pushButton.clicked.connect(self.toggleMenu)
        self.search_btn.clicked.connect(self.searchRoute)
        self.import_btn.clicked.connect(self.openFileDialog)
        self.solution.hide()

        self.__controller = Controller.Controller()

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
        filePath, _ = QFileDialog.getOpenFileName(self, 'Open file', '', 'Text files (*.txt)')
        fileName = os.path.basename(filePath)
        if filePath:
            try:
                self.__controller.importFile(filePath, fileName)
                self.solution.hide()
                self.file_label.setText(fileName)
            except Exception as err:
                print(f"Input file error (Ini belum dihandle): {err.args[0]}")
    
    def searchRoute(self):
        try:
            if self.file_label.text() == "No file":
                raise Exception("No input file")
            if self.start_input.text() == "":
                raise Exception("Start node is missing")
            if self.end_input.text() == "":
                raise Exception("End node is missing")
            if not self.start_input.text().isdigit() or not self.__controller.isNodeValid(int(self.start_input.text())):
                raise Exception("Start node does not exist")
            if not self.end_input.text().isdigit() or not self.__controller.isNodeValid(int(self.end_input.text())):
                raise Exception("End node does not exist")
            if not self.radioButton.isChecked() and not self.radioButton_2.isChecked():
                raise Exception("No algorithm selected")
            
            if self.radioButton.isChecked():
                self.solution_label.setText("Shortest Route (UCS)")
                self.__controller.search(True, int(self.start_input.text()), int(self.end_input.text()))
            else:
                self.solution_label.setText("Shortest Route (A*)")
                self.__controller.search(False, int(self.start_input.text()), int(self.end_input.text()))
            
            self.distance_value.setText(str(self.__controller.getSolutionDistance()))
            self.route_value.setText(self.__controller.getSolutionRoute())
            self.solution.show()
            self.toggleMenu()
        except Exception as err:
            print(f"Search error (Ini belum dihandle): {err.args[0]}")
        
       
        
        