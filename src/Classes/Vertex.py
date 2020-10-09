from copy import copy


class Vertex():
    def __init__(self, ind: int):
        self.ind = ind
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

    def doVertexTraversible(self):
        """
        Makes all edges traversible.
        """
        for edge in self.edges:
            edge.traversible = True

    def doVertexNotTraversible(self):
        """
        Makes all edges not traversible and therefore self not accessible.
        """
        for edge in self.edges:
            edge.traversible = False
