import Parser as par

class Controller:
    def __init__(self):
        self.__isRunning = False
        self.__algorithm = None
    
    def start(self):
        self.__isRunning = True

    def stop(self):
        self.__isRunning = False

    def isRunning(self):
        return self.__isRunning
    
    def readAlgorithm(self):
        parser = par.Parser()
        print("Pilih algoritma")
        print("1. Uniform Cost Search (UCS)")
        print("2. A*")
        parser.read()
        self.__algorithm = parser.getCommand()
        print(self.__algorithm)
