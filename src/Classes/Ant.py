from src.Classes.Vertex import Vertex
from src.Classes.Edge import Edge
from src.Classes.Path import Path

from random import random

from typing import List

class Ant:

    def __init__(self, pheromoneInfluence: float, desirabilityInfluence: float):
        self.pheromoneInfluence = pheromoneInfluence
        self.desirabilityInfluence = desirabilityInfluence

    def createPath(self, start: Vertex, end: Vertex):
        cost = 0
        pathEdges = []

        currentVertex: Vertex = start
        traversibleEdges = currentVertex.getTraversibleEdges()

        while (not currentVertex is end) and currentVertex.getTraversibleEdges():
            chosenEdge: Edge = self.chooseEdgeToTraverse(traversibleEdges)
            self.makeVertexNotAccesible(currentVertex)
            pathEdges.append(chosenEdge)
            cost += chosenEdge.weight

            currentVertex = chosenEdge.getOtherEnd(currentVertex)
            traversibleEdges = currentVertex.getTraversibleEdges()

        if currentVertex is end:
            return Path(start, pathEdges, cost)
        return None

    def chooseEdgeToTraverse(self, possibleEdges: List[Edge]) -> Edge:
        chosenEdge = None

        sumOfAll = sum([edge.desirability**(self.desirabilityInfluence) * edge.depositedPheromone**(self.pheromoneInfluence) for edge in possibleEdges])

        while chosenEdge is None:
            for edge in possibleEdges:
                probabilityOfChoosing = round(((edge.desirability**(self.desirabilityInfluence) * edge.depositedPheromone**(self.pheromoneInfluence)) \
                    / sumOfAll), 2)

                if random() < probabilityOfChoosing:
                    chosenEdge = edge
                    break

        return chosenEdge


    def depositPheromone(self, path: Path):
        edge: Edge
        for edge in path.edges:
            edge.depositedPheromone += (1 / path.cost)

    def makeVertexNotAccesible(self, vertex: Vertex):
        edge:Edge
        for edge in vertex.edges:
            edge.traversible = False
