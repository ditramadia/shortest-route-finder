class Node:
    # === CONSTRUCTOR ===========================================================
    def __init__(self, id, x=None, y=None):
        self.x = x
        self.y = y
        self.id = id
        self.parent = None

    # === GETTER SETTER =========================================================
    def getId(self):
        return self.id
        
    def getId(self):
        return self.id
    
    def setParent(self, parent):
        self.parent = parent    

    def getParent(self):
        return self.parent

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y