import unittest
from src.Classes.Vertex import Vertex
from src.Classes.Edge import Edge

class TestVertex(unittest.TestCase):

    def test_getTraversibleEdges(self):
        vertex1 = Vertex(1)
        vertex2 = Vertex(2)
        edge1 = Edge(vertex1, vertex2, 3)
        edge2 = Edge(vertex1, vertex2, 4)
        edge2.traversible = False

        self.assertNotIn(edge2, vertex1.getTraversibleEdges())
