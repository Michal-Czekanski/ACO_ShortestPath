import unittest
from src.Classes.Edge import Edge
from src.Classes.Vertex import Vertex

class TestEdge(unittest.TestCase):
    def test_constructor(self):
        vertex1 = Vertex(1)
        vertex2 = Vertex(2)
        edge = Edge(vertex1, vertex2, 3)

        self.assertIn(edge, vertex1.edges)
        self.assertIn(edge, vertex2.edges)

if __name__ == "__main__":
    unittest.main()
