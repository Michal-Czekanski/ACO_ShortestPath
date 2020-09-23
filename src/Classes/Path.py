from src.Classes.Vertex import Vertex
from src.Classes.Edge import Edge

class Path:
    def __init__(self, beginning: Vertex, edges, cost: int):
        self.beginning = beginning
        self.edges = edges
        self.cost = cost

    def printPath(self):
        print(self.__pathAsString__())

    def pathAsString(self):
        result = str(beginning.ind)
        currentVertex = beginning
        for edge in edges:
            currentVertex = edge.getOtherEnd(currentVertex)
            result += " - " + str(currentVertex)

        result += " weight : " + str(self.cost)

        return result
