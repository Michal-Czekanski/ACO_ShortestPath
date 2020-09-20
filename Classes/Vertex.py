class Vertex():
    def __init__(ind: int):
        self.ind= ind
        self.edges = []
    
    def getTraversibleEdges():
        traversibleEdges = []
        for edge in self.edges:
            if edge.traversible:
                traversibleEdges.append(edge)

        return traversibleEdges
