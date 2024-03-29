from src.Classes.Vertex import Vertex
from src.Classes.Edge import Edge
from src.Classes.Path import Path

from random import random

from typing import List
from typing import Tuple


class Ant:

    def __init__(self, pheromoneInfluence: float, desirabilityInfluence: float):
        self.pheromoneInfluence = pheromoneInfluence
        self.desirabilityInfluence = desirabilityInfluence

    def createPath(self, start: Vertex, end: Vertex) -> Tuple[Path, bool]:
        """
        Tries to create path from start to end. \n
        :return: Tuple[createdPath: Path, antReachedEnd: bool]
        """
        cost = 0
        pathEdges = []

        currentVertex: Vertex = start
        traversibleEdges = currentVertex.getTraversibleEdges()

        while (not currentVertex is end) and traversibleEdges:
            chosenEdge: Edge = self.chooseEdgeToTraverse(traversibleEdges)
            currentVertex.doVertexNotTraversible()
            pathEdges.append(chosenEdge)
            cost += chosenEdge.weight

            currentVertex = chosenEdge.getOtherEnd(currentVertex)
            traversibleEdges = currentVertex.getTraversibleEdges()

        createdPath = Path(start, pathEdges, cost)
        antReachedEnd = False
        if currentVertex is end:
            antReachedEnd = True
        return createdPath, antReachedEnd

    def chooseEdgeToTraverse(self, possibleEdges: List[Edge]) -> Edge:
        chosenEdge = None

        sumOfAll = sum(
            [edge.desirability ** self.desirabilityInfluence * edge.depositedPheromone ** self.pheromoneInfluence
             for edge in possibleEdges])

        while chosenEdge is None:
            for edge in possibleEdges:
                probabilityOfChoosing = round(((edge.desirability ** (
                    self.desirabilityInfluence) * edge.depositedPheromone ** self.pheromoneInfluence)
                                               / sumOfAll), 2)

                if random() < probabilityOfChoosing:
                    chosenEdge = edge
                    break

        return chosenEdge

    def depositPheromone(self, path: Path):
        edge: Edge
        for edge in path.edges:
            edge.depositedPheromone += (1 / path.cost)
