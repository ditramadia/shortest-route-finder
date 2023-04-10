import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
import Window

app = QApplication(sys.argv)
window = Window.MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(window)
widget.setWindowTitle("Shortest Route Finder")
widget.setFixedHeight(720)
widget.setFixedWidth(1280)
widget.show()
sys.exit(app.exec_())
