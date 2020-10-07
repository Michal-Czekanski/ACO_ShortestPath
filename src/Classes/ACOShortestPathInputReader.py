from src.Classes.Vertex import Vertex
from src.Classes.Edge import Edge
from src.Classes.Graph import Graph

class ACOShortestPathInputReader:
    @staticmethod
    def readGraphFromInputFile(inputFilename: str) -> Graph:
        file = open(inputFilename)

        vertexesNum = int(file.readline().strip())
        edgesNum = int(file.readline().strip())

        vertexes = [Vertex(i + 1) for i in range(vertexesNum)]

        edges = []

        line = file.readline().strip()
        while line:
            content = line.split()

            vertexStart = int(content[1])
            vertexEnd = int(content[2])
            weight = int(content[3])

            edges.append(Edge(vertexStart, vertexEnd, weight))
            line = file.readline().strip()

        return Graph(vertexes, edges)
