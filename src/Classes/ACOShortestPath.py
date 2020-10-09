from src.Classes.Vertex import Vertex
from src.Classes.Edge import Edge
from src.Classes.Path import Path
from src.Classes.Ant import Ant
from src.Classes.Graph import Graph


class ACOShortestPath:

    def __init__(self, pheromoneInfluence: float, desirabilityInfluence: float, \
                 evaporationCoefficent: float):
        self.pheromoneInfluence = pheromoneInfluence
        self.desirabilityInfluence = desirabilityInfluence
        self.evaporationCoefficent = evaporationCoefficent

    def findShortestPath(self, graph: Graph, start: Vertex, end: Vertex,
                         iterNum: int, printEachPath: bool):

        self.__initialization__(graph)

        shortestPath = Path(start, end, float("inf"))
        for i in range(iterNum):
            ant = Ant(self.pheromoneInfluence, self.desirabilityInfluence)
            path = ant.createPath(start, end)
            if not path is None:
                self.__resetTraversibility__(path)
                ant.depositPheromone(path)
                self.__pheromoneEvaporation__(graph)

                if printEachPath:
                    stringToPrint = "{}. {}".format(str(i + 1), path.pathAsString())
                    print(stringToPrint)

                if path.cost < shortestPath.cost:
                    shortestPath = path
            else:
                if printEachPath:
                    stringToPrint = "{}. Path not found".format(str(i + 1))
                    print(stringToPrint)

        return shortestPath

    def __initialization__(self, graph: Graph):
        edge: Edge
        for edge in graph.edges:
            edge.depositedPheromone = 1

    def __resetTraversibility__(self, path: Path):
        """
        Makes all vertexes from given path accesbile \n
        by making all edges of each vertex traversible.
        """
        currentVertex: Vertex = path.beginning
        currentVertex.doVertexTraversible()
        edge: Edge
        for edge in path.edges:
            currentVertex = edge.getOtherEnd(currentVertex)
            currentVertex.doVertexTraversible()

    def __pheromoneEvaporation__(self, graph: Graph):
        edge: Edge
        for edge in graph.edges:
            edge.depositedPheromone *= (1 - self.evaporationCoefficent)
