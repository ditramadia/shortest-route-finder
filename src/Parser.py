class Parser:
    def __init__(self):
        self.__data = None

    def readCommand(self):
        self.__data = str(input("> "))
        
    def getData(self):
        return self.__data