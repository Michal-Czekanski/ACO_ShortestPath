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

    def test_getOtherEnd(self):
        vertex1 = Vertex(1)
        vertex2 = Vertex(2)
        vertex3 = Vertex(3)

        edge = Edge(vertex1, vertex2, 3)

        self.assertEqual(edge.getOtherEnd(vertex1), vertex2)
        self.assertEqual(edge.getOtherEnd(vertex2), vertex1)
        self.assertEqual(edge.getOtherEnd(vertex3), None)

    def test_delete(self):
        vertex1 = Vertex(1)
        vertex2 = Vertex(2)

        edge = Edge(vertex1, vertex2, 3)
        edge.delete()

        self.assertNotIn(edge, vertex1.edges)
        self.assertNotIn(edge, vertex2.edges)


if __name__ == "__main__":
    unittest.main()
