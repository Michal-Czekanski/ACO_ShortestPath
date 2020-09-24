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
            chosenEdge: Edge = self.chooseEdge(traversibleEdges)
            chosenEdge.traversible = False
            pathEdges.append(chosenEdge)
            cost += chosenEdge.weight

            currentVertex = chosenEdge.getOtherEnd(currentVertex)
            traversibleEdges = currentVertex.getTraversibleEdges()

        if currentVertex is end:
            return Path(start, pathEdges, cost)
        return None

    def chooseEdge(self, possibleEdges: List[Edge]) -> Edge:
        chosenEdge = None

        sumOfAll = sum([edge.desirability * edge.depositedPheromone for edge in possibleEdges]) \
            * self.desirabilityInfluence * self.pheromoneInfluence

        while chosenEdge is None:
            for edge in possibleEdges:
                probabilityOfChoosing = round(((edge.desirability * self.desirabilityInfluence * edge.depositedPheromone * self.pheromoneInfluence) \
                    / sumOfAll), 2)

                print(probabilityOfChoosing)
                if random() < probabilityOfChoosing:
                    chosenEdge = edge
                    break

        return chosenEdge
