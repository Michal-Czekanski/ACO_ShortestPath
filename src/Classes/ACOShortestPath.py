from src.Classes.Vertex import Vertex
from src.Classes.Edge import Edge
from src.Classes.Path import Path
from src.Classes.Ant import Ant
from src.Classes.Graph import Graph


class ACOShortestPath:

    INITIAL_PHEROMONE_LEVEL = 1

    def __init__(self, pheromoneInfluence: float, desirabilityInfluence: float,
                 evaporationCoefficent: float):
        self.pheromoneInfluence = pheromoneInfluence
        self.desirabilityInfluence = desirabilityInfluence
        self.evaporationCoefficent = evaporationCoefficent

    def findShortestPath(self, graph: Graph, start: Vertex, end: Vertex,
                         iterNum: int, printEachPath: bool):

        self.__initialization__(graph)

        shortestPath = Path(start, [], float("inf"))
        for i in range(iterNum):
            ant = Ant(self.pheromoneInfluence, self.desirabilityInfluence)
            path, antReachedEnd = ant.createPath(start, end)
            while not antReachedEnd:
                path, antReachedEnd = ant.createPath(start, end)
                self.__resetTraversibility__(path)

            self.__resetTraversibility__(path)
            ant.depositPheromone(path)
            self.__pheromoneEvaporation__(graph)

            if printEachPath:
                stringToPrint = "{}. {}".format(str(i + 1), path.pathAsString())
                print(stringToPrint)

            if path.cost < shortestPath.cost:
                shortestPath = path


        return shortestPath

    def __initialization__(self, graph: Graph):
        """
        Make all edges traversible and their pheromoneLevel = 1
        :param graph:
        :return:
        """
        edge: Edge
        for edge in graph.edges:
            edge.depositedPheromone = ACOShortestPath.INITIAL_PHEROMONE_LEVEL
            edge.traversible = True

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
