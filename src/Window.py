import os
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import * 
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore
from PyQt5.QtCore import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.figure as Figure
import networkx as nx
import gmplot
import Controller

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('src/uibuilder/Main.ui', self)
        self.pushButton.clicked.connect(self.toggleMenu)
        self.search_btn.clicked.connect(self.searchRoute)
        self.import_btn.clicked.connect(self.openFileDialog)

        self.web_view = QWebEngineView(self.plot)
        self.web_view.setFixedWidth(1280)
        self.web_view.setFixedHeight(720)
        self.plot.hide()

        widget_size = self.plot.size()
        self.figure = Figure.Figure(figsize=(widget_size.width(), widget_size.height()))
        self.figure.set_size_inches(widget_size.width()/100, widget_size.height()/120)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setParent(self.plot)
        self.graph = self.figure.add_subplot(111)
        self.graph.set_axis_off()
        self.canvas.hide()

        self.solution.hide()
        self.popup_container.hide()

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
                self.popup_container.hide()
                self.plot.hide()

            except Exception as err:
                self.popup_value.setText(f"Input file error: {err.args[0]}")
                self.popup_container.show()

    def createGMPlot(self):
        gmap = gmplot.GoogleMapPlotter(-6.901837, 107.601241, 13)

        for node in self.__controller.getGraph().getNodeList():
            for node2 in self.__controller.getGraph().getNodeList():
                if self.__controller.getGraph().getAdjMatrix()[node.getId() - 1][node2.getId() - 1] > 0:
                    lats = [node.getX(), node2.getX()]
                    lngs = [node.getY(), node2.getY()]
                    gmap.scatter(lats, lngs, '#FFA54F', size=10, marker=False)
                    gmap.plot(lats, lngs, '#FFA54F', edge_width=2.5)

        latsSolution = []
        lngsSolution = []
        for node in self.__controller.getSolution()["path"]:
            latsSolution.append(self.__controller.getGraph().getNodeList()[node - 1].getX())
            lngsSolution.append(self.__controller.getGraph().getNodeList()[node - 1].getY())
            
        gmap.scatter(latsSolution, lngsSolution, '#63B8FF', size=10, marker=False)
        gmap.plot(latsSolution, lngsSolution, '#63B8FF', edge_width=3.5)
        gmap.draw(f"./test/temp.html")
    
    def createNetworkX(self):
        g = nx.DiGraph()
        nodeList = self.__controller.getGraph().getNodeList()
        node1Idx = 0
        for nodeRow in self.__controller.getGraph().getAdjMatrix():
            node2Idx = 0
            for weight in nodeRow:
                if weight > 0:
                    g.add_edge(nodeList[node1Idx].getId(), nodeList[node2Idx].getId(), weight=weight)
                node2Idx += 1
            node1Idx += 1
        return g
    
    def pairRouteEdge(self):
        pair = []
        nodeIdx = 0
        for node in self.__controller.getSolutionRouteList():
            if nodeIdx == len(self.__controller.getSolutionRouteList()) - 1:
                break
            pair.append((int(node), int(self.__controller.getSolutionRouteList()[nodeIdx + 1])))
            nodeIdx += 1
        return pair

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

            if self.__controller.getGraph().getIsWCoordinate():
                self.canvas.hide()
                self.createGMPlot()
                self.web_view.setUrl(QtCore.QUrl.fromLocalFile(os.path.abspath("test/temp.html")))
                self.plot.show()
            else:
                self.plot.show()
                network = self.createNetworkX()
                pos = nx.kamada_kawai_layout(network)
                pair = self.pairRouteEdge()
                print(pair)
                nx.draw(network, pos, node_size=500, node_color='#FFA54F', ax=self.graph, font_size=10, font_color="black", font_weight="bold", with_labels=True)
                nx.draw_networkx_edges(network, pos, edgelist=pair, edge_color='#63B8FF', width=3, ax=self.graph)
                self.canvas.show()
                
            self.distance_value.setText(str(self.__controller.getSolutionDistance()))
            self.route_value.setText(self.__controller.getSolutionRoute())
            self.solution.show()
            self.toggleMenu()
            
        except Exception as err:
            self.popup_value.setText(f"Input file error: {err.args[0]}")
            self.popup_container.show()
