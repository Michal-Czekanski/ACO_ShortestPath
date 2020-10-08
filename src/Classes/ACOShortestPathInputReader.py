from src.Classes.Vertex import Vertex
from src.Classes.Edge import Edge
from src.Classes.Graph import Graph

class ACOShortestPathInputReader:
    @staticmethod
    def readGraphFromInputFile(inputFilePath: str) -> Graph:
        file = open(inputFilePath)

        try:

            vertexesNum = int(file.readline().strip().split()[2])
            edgesNum = int(file.readline().strip().split()[2])

            vertexes = [Vertex(i + 1) for i in range(vertexesNum)]

            edges = []

            line = file.readline().strip()
            while line:
                content = line.split()

                # Vertex start
                vertexStartInd = int(content[1])
                vertexStart = None
                vertex: Vertex
                for vertex in vertexes:
                    if vertex.ind == vertexStartInd:
                        vertexStart = vertex

                # Vertex end
                vertexEndInd = int(content[2])
                vertexEnd = None
                vertex: Vertex
                for vertex in vertexes:
                    if vertex.ind == vertexEndInd:
                        vertexEnd = vertex

                # Weight
                weight = int(content[3])

                edges.append(Edge(vertexStart, vertexEnd, weight))
                line = file.readline().strip()
        except Exception as e:
            file.close()
            raise e

        file.close()
        return Graph(vertexes, edges)
