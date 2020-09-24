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

    def test_delete(self):
        vertex1 = Vertex(1)
        vertex2 = Vertex(2)
        edge1 = Edge(vertex1, vertex2, 3)
        edge2 = Edge(vertex1, vertex2, 4)

        vertex1.delete()

        self.assertEqual(vertex1.ind, None)
        self.assertNotIn(edge1, vertex2.edges)
        self.assertNotIn(edge2, vertex2.edges)

if __name__ == '__main__':
    unittest.main()
