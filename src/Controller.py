import Parser as par
import Graph as gr

class Controller:
    def __init__(self):
        self.__isRunning = False
        self.__algorithm = None
        self.__mapPath = None
        self.__graph = None
    
    def start(self):
        self.__isRunning = True

    def stop(self):
        self.__isRunning = False

    def isRunning(self):
        return self.__isRunning

    def readAlgorithm(self):
        parser = par.Parser()
        print("Pilih algoritma")
        print("1. Uniform Cost Search (UCS)")
        print("2. A*")
        parser.readCommand()
        self.__algorithm = parser.getData()
    
    def readMap(self):
        parser = par.Parser()
        print("Masukan file map")
        parser.readCommand()
        self.__mapPath = parser.getData()

        self.__graph = gr.Graph()
        self.__graph.readFile(self.__mapPath)
        self.__graph.printAdjMatrix()
