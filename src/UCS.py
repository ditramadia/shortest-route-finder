import Graph as gp
class UCS:

    def __init__(self):
        self.path = []
        self.cost = 0
        self.visited = []
        self.queue = []


    def search(self, graph, start, goal):
        listnode  = graph.getNodeList()
        matrix = graph.getAdjMatrix()

        self.queue.append([start, 0])
        
        while len(self.queue) > 0:
            current = self.queue.pop(0)
            self.visited.append(current[0])

            if current[0] == goal:
                        node = listnode[goal - 1]
                        while node != None:
                            print(node.getId())
                            self.path.append(node.getId())
                            
                            if (node.getId() == start):
                                break
                            node = listnode[node.getParent() - 1]
                        self.cost = current[1]
                        self.path.reverse()
                        break
                
            for i in range(len(matrix[current[0] - 1])):
                    if matrix[current[0] - 1][i] != 0 and (i + 1) not in self.visited:
                        listnode[i].setParent(current[0])
                        self.queue.append([i + 1, current[1] + matrix[current[0] - 1][i]])
                        
            self.queue.sort(key=lambda x: x[1])

        return self.path, self.cost

