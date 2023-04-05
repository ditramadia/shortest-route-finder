class Graph:
    def __init__(self):
        self.__adjMatrix = []

    def readFile(self, path):
        self.__adjMatrix = []

        file = open(f"./test/{path}.txt", "r")
        for line in file:
            charList = line.replace("\n", "").split()
            weightList = []
            
            for element in charList:
                weightList.append(float(element))
            
            self.__adjMatrix.append(weightList)

    def printAdjMatrix(self):
        print("[")
        for row in self.__adjMatrix:
            print("[", end="")
            for element in row:
                print(str(element) + ",", end="")
            print("]")
        print("]")