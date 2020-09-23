from src.Classes.Vertex import Vertex
from src.Classes.Edge import Edge

class Path:
    def __init__(self, beginning: Vertex, edges, cost: int):
        self.beginning = beginning
        self.edges = edges
        self.cost = cost
