import Node as nd

class Graph:
    # === CONSTRUCTOR ===========================================================
    def __init__(self):
        self.__adjMatrix = []
        self.__nodeList = []

    # === GETTER SETTER =========================================================
    def getAdjMatrix(self):
        return self.__adjMatrix

    def getNodeList(self):
        return self.__nodeList    

    # === INITIALIZER ===========================================================
    def buildAdjMatrix(self, path):
        self.__adjMatrix = []

        file = open(f"./test/{path}.txt", "r")
        for line in file:
            charList = line.replace("\n", "").split()
            weightList = []
            
            for element in charList:
                weightList.append(float(element))
            
            self.__adjMatrix.append(weightList)
        
        file.close()

    def buildNodeList(self, path):
        self.__nodeList = []

        file = open(f"./test/{path}.txt", "r")
        i = 1
        for line in file:
            newNode = nd.Node(i)
            self.__nodeList.append(newNode)

            i += 1 
        file.close()

    def build(self, path):
        self.buildAdjMatrix(path)
        self.buildNodeList(path)

    def getAdjMatrix(self):
        return self.__adjMatrix

    def getNodeList(self):
        return self.__nodeList
        
    # === DISPLAY  ==============================================================
    def printAdjMatrix(self):
        print("[")
        for row in self.__adjMatrix:
            print("[", end="")
            for element in row:
                print(str(element) + " ", end="")
            print("]")
        print("]")

    def printNodeList(self):
        print("[", end="")
        for node in self.__nodeList:
            print(str(node.getId()) + ",", end="")
        print("]")