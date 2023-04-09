import Graph

class Controller:
    # === CONSTRUCTOR ===========================================================
    def __init__(self):
        self.__selectedAlgorithm = 0
        self.__graph = None

    # === IO ====================================================================
    def importFile(self, filePath, fileName):
        self.__graph = Graph.Graph(filePath, fileName)
        self.__graph.build()
