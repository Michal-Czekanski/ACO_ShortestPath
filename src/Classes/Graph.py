from src.Classes.Vertex import Vertex
from src.Classes.Edge import Edge
from typing import List

class Graph:

    def __init__(self, vertexes: List[Vertex], edges: List[Edge]):
        self.vertexes = vertexes
        self.edges = edges

    def addEdge(self, edge: Edge):
        if not edge in self.edges:
            if not edge.getVertexes()[0] in self.vertexes:
                self.vertexes.append(edge.getVertexes()[0])
            if not edge.getVertexes()[1] in self.vertexes:
                self.vertexes.append(edge.getVertexes()[1])
            self.edges.append(edge)
            return True
        else:
            return False

    def addVertex(self, vertex: Vertex) -> bool:
        if vertex in self.vertexes:
            return False

        self.vertexes.append(vertex)
        return True

    def deleteVertex(self, vertex: Vertex):
        self.vertexes.remove(vertex)
        vertex.delete()

    def deleteEdge(self, edge: Edge):
        self.edges.remove(edge)
        edge.delete()
