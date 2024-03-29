from src.Classes.Vertex import Vertex
from src.Classes.Edge import Edge

class Path:
    def __init__(self, beginning: Vertex, edges, cost: int):
        self.beginning = beginning
        self.edges = edges
        self.cost = cost

    def printPath(self):
        print(self.pathAsString())

    def pathAsString(self):
        result = str(self.beginning.ind)
        currentVertex = self.beginning
        for edge in self.edges:
            currentVertex = edge.getOtherEnd(currentVertex)
            result += " - " + str(currentVertex.ind)

        result += " --- weight = " + str(self.cost)

        return result
