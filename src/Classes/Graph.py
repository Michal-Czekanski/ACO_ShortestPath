from src.Classes.Vertex import Vertex
from src.Classes.Edge import Edge
from typing import List

class Graph:

    def __init__(self, vertexes: List[Vertex], edges: List[Edge]):
        self.vertexes = vertexes
        self.edges = edges
