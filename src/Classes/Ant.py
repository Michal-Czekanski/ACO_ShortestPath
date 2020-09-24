from src.Classes.Vertex import Vertex
from src.Classes.Edge import Edge
from src.Classes.Path import Path

class Ant:

    def __init__(self, pheromoneInfluence: float, desirabilityInfluence: float):
        self.pheromoneInfluence = pheromoneInfluence
        self.desirabilityInfluence = desirabilityInfluence
