import unittest
from src.Classes.Vertex import Vertex
from src.Classes.Edge import Edge
from src.Classes.Path import Path

class TestPath(unittest.TestCase):

    def test_constructor(self):
        vertex1 = Vertex(1)
        vertex2 = Vertex(2)
        vertex3 = Vertex(3)

        edge1 = Edge(vertex1, vertex2, 1)
        edge2 = Edge(vertex2, vertex3, 2)

        path = Path(vertex1, [edge1, edge2], 1 + 2)

        self.assertEqual(vertex1, path.beginning)
        self.assertEqual(path.cost, 3)
        self.assertIn(edge1, path.edges)
        self.assertIn(edge2, path.edges)

if __name__ == "__main__":
    unittest.main()
