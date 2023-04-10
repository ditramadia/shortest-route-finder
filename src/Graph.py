import math
import Node

class Graph:
    # === CONSTRUCTOR ===========================================================
    def __init__(self, filePath, fileName):
        self.__filePath = filePath
        self.__fileName = fileName
        self.__isWCoordinate = False
        self.__adjMatrix = []
        self.__nodeList = []

    # === GETTER SETTER =========================================================
    def getAdjMatrix(self):
        return self.__adjMatrix

    def getNodeList(self):
        return self.__nodeList  

    # === INITIALIZER ===========================================================
    def validateFileFormat(self):

        file = open(self.__filePath)
        charMatrix = []
        for line in file:
            charMatrix.append(line.replace("\n", "").split())
        file.close()

        if len(charMatrix) == len(charMatrix[0]):
            for charList in charMatrix:
                if len(charList) != len(charMatrix):
                    raise Exception("The number of rows and columns does not match")
                for char in charList:
                    try:
                        float(char)
                    except:
                        raise Exception("All characters must be a numerical value")
            self.__isWCoordinate = False
        elif len(charMatrix) + 2 == len(charMatrix[0]):
            for charList in charMatrix:
                if len(charList) != 2 + len(charMatrix):
                    raise Exception("The number of rows and columns does not match")
                for char in charList:
                    try:
                        float(char)
                    except:
                        raise Exception("All characters must be a numerical value")
            self.__isWCoordinate = True
        else:
            raise Exception("The number of rows and columns does not match")
    
    def buildNodes(self):
        self.__nodeList = []

        file = open(self.__filePath, "r")
        nodeId = 1
        for line in file:
            charList = line.replace("\n", "").split()
            if self.__isWCoordinate:
                newNode = Node.Node(nodeId, float(charList[len(charList) - 2]), float(charList[len(charList) - 1]))
            else:
                newNode = Node.Node(nodeId)
            self.__nodeList.append(newNode)
            nodeId += 1
        file.close()

        # print(self.__isWCoordinate)
        # print()
        # for node in self.__nodeList:
        #     print(node.getId(), end=" ")
        # print()
        # for node in self.__nodeList:
        #     print(node.getX(), end=" ")
        # print()
        # for node in self.__nodeList:
        #     print(node.getY(), end=" ")
        # print()
    
    def buildAdjMatrix(self):
        self.__adjMatrix = []

        file = open(self.__filePath, "r")
        i = 0
        for line in file:
            charList = line.replace("\n", "").split()
            weightList = []

            if self.__isWCoordinate:
                for j in range(0, len(charList) - 2):
                    weightList.append(math.sqrt(((self.__nodeList[i].getX() - self.__nodeList[j].getX()) ** 2) + ((self.__nodeList[i].getY() - self.__nodeList[j].getY()) ** 2)) * float(charList[j]))
            else:
                for element in charList:
                    weightList.append(float(element))
            
            self.__adjMatrix.append(weightList)
            i += 1
        file.close()

    def build(self):
        self.validateFileFormat()
        self.buildNodes()
        self.buildAdjMatrix()
