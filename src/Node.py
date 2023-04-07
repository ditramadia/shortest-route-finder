class Node:
    # === CONSTRUCTOR ===========================================================
    def __init__(self, id):
        self.x = None
        self.y = None
        self.id = id
        self.parent = None

    # === GETTER SETTER =========================================================
    def getId(self):
        return self.id
    
    def setParent(self, parent):
        self.parent = parent    

    def getParent(self):
        return self.parent
    
    def getId(self):
        return self.id