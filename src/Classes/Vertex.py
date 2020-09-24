from copy import copy

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

    def delete(self):
        self.ind = None
        tmpEdgesList = copy(self.edges)
        for edge in tmpEdgesList:
            edge.delete()
