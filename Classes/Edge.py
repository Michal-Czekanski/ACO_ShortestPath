from Vertex import Vertex

class Edge:
    def __init__(self, v1: Vertex, v2: Vertex, weight: int):
        self.vertexes = {v1, v2}
        self.weight = weight
        self.desirability = 1 / weight
        self.depositedPheromone = 0
        self.traversible = True

    def getVertexes(self):
        return list(self.vertexes)

    def getOtherEnd(self, firstEnd: Vertex):
        if firstEnd in self.vertexes:
            for vertex in self.getVertexes():
                if not vertex is firstEnd:
                    return vertex

        return None
