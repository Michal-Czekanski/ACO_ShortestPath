from src.Classes.Vertex import Vertex
from src.Classes.Edge import Edge
from src.Classes.Path import Path
from src.Classes.Ant import Ant
from src.Classes.Graph import Graph

class ACOShortestPath:

    def __init__(self, pheromoneInfluence: float, desirabilityInfluence: float,\
                        evaporationCoefficent: float):
        self.pheromoneInfluence = pheromoneInfluence
        self.desirabilityInfluence = desirabilityInfluence
        self.evaporationCoefficent = evaporationCoefficent

    def __initialization__(graph: Graph):
        edge: Edge
        for edge in graph.edges:
            edge.depositedPheromone = 1
