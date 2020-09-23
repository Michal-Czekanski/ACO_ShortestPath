class Vertex():
    def __init__(self, ind: int):
        self.ind= ind
        self.edges = []
    
    def getTraversibleEdges(self):
        traversibleEdges = []
        for edge in self.edges:
            if edge.traversible:
                traversibleEdges.append(edge)

        return traversibleEdges
