class Parser:
    # === CONSTRUCTOR ===========================================================
    def __init__(self):
        self.__data = None

    # === GETTER SETTER =========================================================
    def getData(self):
        return self.__data

    # === IO ====================================================================
    def readCommand(self):
        self.__data = str(input("> "))
        