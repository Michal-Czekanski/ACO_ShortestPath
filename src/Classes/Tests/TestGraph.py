import unittest
from src.Classes.Edge import Edge
from src.Classes.Vertex import Vertex
from src.Classes.Graph import Graph

class TestGraph(unittest.TestCase):

    def test_addEdge(self):
        vertex1 = Vertex(1)
        vertex2 = Vertex(2)
        graph = Graph([vertex1, vertex2], [])

        # Case 1: Both of edge's vertexes are in graph
        edge1 = Edge(vertex1, vertex2, 3)

        graph.addEdge(edge1)
        self.assertIn(edge1, graph.edges)

        # Case 2: One edge's vertex is not in graph
        vertex3 = Vertex(3)
        edge2 = Edge(vertex2, vertex3, 4)

        graph.addEdge(edge2)
        self.assertIn(edge2, graph.edges)
        self.assertIn(vertex3, graph.vertexes)

        # Case 3: Both of edge's vertexes are not in graph
        vertex4 = Vertex(4)
        vertex5 = Vertex(5)
        edge3 = Edge(vertex4, vertex5, 3)

        graph.addEdge(edge3)
        self.assertIn(edge3, graph.edges)
        self.assertIn(vertex4, graph.vertexes)
        self.assertIn(vertex5, graph.vertexes)



if __name__ == "__main__":
    unittest.main()
