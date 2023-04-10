import gmplot

class Plotter:
    def createGMPlot(self, graph, solution):
        gmap = gmplot.GoogleMapPlotter(-6.901837, 107.601241, 13, apikey="", map_type="satellite")

        for node in graph.getNodeList():
            for node2 in graph.getNodeList():
                if graph.getAdjMatrix()[node.getId() - 1][node2.getId() - 1] > 0:
                    lats = [node.getX(), node2.getX()]
                    lngs = [node.getY(), node2.getY()]
                    gmap.scatter(lats, lngs, '#FFA54F', size=10, marker=False)
                    gmap.plot(lats, lngs, '#FFA54F', edge_width=2.5)

        latsSolution = []
        lngsSolution = []
        for node in solution["path"]:
            latsSolution.append(graph.getNodeList()[node - 1].getX())
            lngsSolution.append(graph.getNodeList()[node - 1].getY())
            
        gmap.scatter(latsSolution, lngsSolution, '#63B8FF', size=10, marker=False)
        gmap.plot(latsSolution, lngsSolution, '#63B8FF', edge_width=3.5)
        gmap.draw(f"./test/temp.html")
    
    def plot(self, graph, solution):
        if graph.getIsWCoordinate():
            self.createGMPlot(graph, solution)
            print("Display gmplot")
        else:
            print("Display noetworkx")