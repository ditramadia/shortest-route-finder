import Graph
import UCS
import AStar

class Controller:
    # === CONSTRUCTOR ===========================================================
    def __init__(self):
        self.__graph = None
        self.__solution = None

    # === GETTER SETTER =========================================================
    def getSolution(self):
        return self.__solution
    
    def getSolutionDistance(self):
        return self.__solution["distance"]
    
    def getSolutionRoute(self):
        route = ""
        i = 0
        for node in self.__solution["path"]:
            if i == len(self.__solution["path"]) - 1:
                route += str(node)
                break
            route += str(node) + " - "
            i += 1
        return route
    
    def getSolutionRouteList(self):
        return self.__solution["path"]
    
    def getGraph(self):
        return self.__graph

    # === VALIDATOR =============================================================
    def isNodeValid(self, nodeId):
        valid = False
        for node in self.__graph.getNodeList():
            if nodeId == node.getId():
                valid = True
        return valid

    # === IO ====================================================================
    def importFile(self, filePath, fileName):
        self.__graph = Graph.Graph(filePath, fileName)
        self.__graph.build()
    
    def search(self, isUCS, startNodeId, endNodeId):
        if isUCS:
            ucsAlgorithm = UCS.UCS()
            ucsAlgorithm.search(self.__graph, startNodeId, endNodeId)
            self.__solution = ucsAlgorithm.getSolution()
        else:
            aStarAlgorithm = AStar.AStar()
            aStarAlgorithm.findShortestPath(self.__graph, startNodeId, endNodeId)
            self.__solution = aStarAlgorithm.getSolution()