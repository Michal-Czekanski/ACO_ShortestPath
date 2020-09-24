import unittest

from src.Classes.Ant import Ant
from src.Classes.Vertex import Vertex
from src.Classes.Edge import Edge
from src.Classes.Path import Path

class TestAnt(unittest.TestCase):

    def test_createPath1(self):
        """Case 1: Path between vertexes does not exist
        """
        vertex1 = Vertex(1)
        vertex2 = Vertex(2)

        ant = Ant(1, 1)

        self.assertIsNone(ant.createPath(vertex1, vertex2))

    def test_createPath2(self):
        """Case 2: Path between vertexes exists.
        """
        vertex1 = Vertex(1)
        vertex2 = Vertex(2)
        edge = Edge(vertex1, vertex2, 3)
        edge.depositedPheromone = 1

        ant = Ant(1, 1)

        self.assertIsNotNone(ant.createPath(vertex1, vertex2))



if __name__ == "__main__":
    unittest.main()
