from Vertex import Vertex

class Edge:
    def __init__(self, v1: Vertex, v2: Vertex, weight: int):
        self.vertexes = {v1, v2}
        self.weight = weight
        self.desirability = 1 / weight
        self.depositedPheromone = 0
        self.traversible = True
