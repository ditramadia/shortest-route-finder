import Parser as par
import Graph as gr
import AStar as ast
import UCS as ucs

class Controller:
    # === CONSTRUCTOR ===========================================================
    def __init__(self):
        self.__isRunning = False
        self.__algorithm = None
        self.__mapPath = None
        self.__graph = None

    # === STATES ================================================================
    def isRunning(self):
        return self.__isRunning
    
    # === CONTROLS ==============================================================
    def start(self):
        self.__isRunning = True

    def solve(self):
        parser = par.Parser()
        print("Pilih Starting Node:")
        parser.readCommand()
        startingNode = parser.getData()
        print("Pilih Destination Node:")
        parser.readCommand()
        destinationNode = parser.getData()

        if self.__algorithm == "1":
            uCs = ucs.UCS()
            uCs.search(self.__graph, 1, 6)

            print("Solusi:")
            print("Path: " + str(uCs.getSolution()["path"]))
            print("Distance: " + str(uCs.getSolution()["cost"]))

        elif self.__algorithm == "2":
            aStar = ast.AStar()
            aStar.findShortestPath(self.__graph, int(startingNode), int(destinationNode))

            print("Solusi:")
            print("Path: " + str(aStar.getSolution()["path"]))
            print("Distance: " + str(aStar.getSolution()["distance"]))

    def stop(self):
        self.__isRunning = False

    # === IO ====================================================================
    def readMap(self):
        parser = par.Parser()
        print("Masukan file map")
        parser.readCommand()
        self.__mapPath = parser.getData()

        self.__graph = gr.Graph()
        self.__graph.build(self.__mapPath)
    
    def readAlgorithm(self):
        parser = par.Parser()
        print("Pilih algoritma")
        print("1. Uniform Cost Search (UCS)")
        print("2. A*")
        parser.readCommand()
        self.__algorithm = parser.getData()
    

