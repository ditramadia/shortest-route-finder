class Graph:
    # === CONSTRUCTOR ===========================================================
    def __init__(self, filePath, fileName):
        self.__filePath = filePath
        self.__fileName = fileName
        self.__isWCoordinate = False
        self.__adjMatrix = []
        self.__nodeList = []

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

    def build(self):
        self.validateFileFormat()
