class Parser:
    def __init__(self):
        self.__command = None

    def read(self):
        self.__command = str(input("> "))
        
    def getCommand(self):
        return self.__command