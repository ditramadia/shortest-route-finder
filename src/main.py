# Import Modules
import sys
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import * 
# import Controller as ct
import Window

# controller = ct.Controller()

# controller.start()
# while(controller.isRunning()):
#     controller.displaySplash()
#     controller.mode()
#     controller.readMap()
#     controller.readAlgorithm()
#     controller.solve()
#     if controller.wCoordinate():
#         controller.plotter()
#     controller.menu()

app = QApplication(sys.argv)
window = Window.MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(window)
widget.setWindowTitle("Shortest Route Finder")
widget.setFixedHeight(720)
widget.setFixedWidth(1280)
widget.show()
sys.exit(app.exec_())
