import Node as nd
import math

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
    def buildAdjMatrix(self, path, wCoordinate):
        self.__adjMatrix = []

        file = open(f"./test/{path}.txt", "r")
        i = 0
        for line in file:
            charList = line.replace("\n", "").split()
            weightList = []
            
            if wCoordinate:
                for j in range(0, len(charList) - 2):
                    weightList.append(math.sqrt(((self.__nodeList[i].getX() - self.__nodeList[j].getX()) ** 2) + ((self.__nodeList[i].getY() - self.__nodeList[j].getY()) ** 2)) * float(charList[j]))
            else:
                for element in charList:
                    weightList.append(float(element))
            
            self.__adjMatrix.append(weightList)
            i += 1

        for row in self.__adjMatrix:
            if len(row) != len(self.__adjMatrix):
                raise Exception

        file.close()

    def buildNodeList(self, path, wCoordinate):
        self.__nodeList = []

        file = open(f"./test/{path}.txt", "r")
        i = 1
        for line in file:
            charList = line.replace("\n", "").split()
            if wCoordinate:
                newNode = nd.Node(i, float(charList[len(charList) - 2]), float(charList[len(charList) - 1]))
            else:
                newNode = nd.Node(i)

            self.__nodeList.append(newNode)

            i += 1 
        file.close()
        # for node in self.__nodeList:
        #     print(node.getX(), end=" ")
        # print()
        # for node in self.__nodeList:
        #     print(node.getY(), end=" ")

    def build(self, path, wCoordinate):
        self.buildNodeList(path, wCoordinate)
        self.buildAdjMatrix(path, wCoordinate)

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