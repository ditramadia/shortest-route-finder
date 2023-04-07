class AStar:
    # === CONSTRUCTOR ===========================================================
    def __init__(self):
        self.openList = set([])
        self.closedList = set([])
        self.solution = {
            "path" : [],
            "distance" : None
            }
        self.fScore = {}
        self.gScore = {}
        self.hScore = {}
        self.last = {}

    # === GETTER SETTER ==========================================================
    def getSolution(self):
        return self.solution
    
    # === UTILITY ================================================================
    
    # Initialize score and last with default value
    def initialState(self, graph):
        for node in graph.getNodeList():
            self.hScore[int(node.getId())] = float(9999)
            self.gScore[int(node.getId())] = float("inf")
            self.fScore[int(node.getId())] = float("inf")
            self.last[int(node.getId())] = None    
    
    # Update starting node score
    def updateStartingNode(self, startingNode):
        self.openList.add(startingNode)
        self.gScore[startingNode] = 0
        self.fScore[startingNode] = self.gScore[startingNode] + self.hScore[startingNode]
        self.last[startingNode] = startingNode
    
    # Determine node to expand based on lowest fScore
    def determineExpandNode(self):
        expandNode = None
        for comparingNode in self.openList:
            if expandNode == None or self.gScore[comparingNode] + self.hScore[comparingNode] < self.gScore[expandNode] + self.hScore[expandNode]:
                expandNode = comparingNode
        return expandNode
    
    # Update neighbouring node of expand node and update its score
    def updateNeighbourNode(self, graph, expandNode):
        comparingNode = 1
        for weight in graph.getAdjMatrix()[expandNode - 1]:
            if weight > 0 and weight != float("inf"):
                if comparingNode not in self.openList and comparingNode not in self.closedList:
                    self.openList.add(comparingNode)
                    self.last[comparingNode] = expandNode
                    self.gScore[comparingNode] = self.gScore[expandNode] + weight
                    self.fScore[comparingNode] = self.gScore[comparingNode] + self.hScore[comparingNode]
                else:
                    if self.gScore[comparingNode] > self.gScore[expandNode] + weight:
                        self.gScore[comparingNode] = self.gScore[expandNode] + weight
                        self.last[comparingNode] = expandNode
                        if comparingNode in self.closedList:
                            self.closedList.remove(comparingNode)
                            self.openList.add(comparingNode)
            comparingNode += 1
    
    # Reconstruct solution path
    def reconstructPath(self, startingNode, destinationNode):
        self.solution["path"] = [destinationNode]
        
        while self.solution["path"][0] != startingNode:
            self.solution["path"].insert(0, self.last[self.solution["path"][0]])
        
        self.solution["distance"] = self.gScore[destinationNode]    

    # === METHODS ===============================================================
    def findShortestPath(self, graph, startingNode, destinationNode):
        self.initialState(graph)
        self.updateStartingNode(startingNode)
        while True:
            expandNode = self.determineExpandNode()
            if expandNode == destinationNode:
                self.reconstructPath(startingNode, destinationNode)
                return
            self.updateNeighbourNode(graph, expandNode)
            self.openList.remove(expandNode)
            self.closedList.add(expandNode)