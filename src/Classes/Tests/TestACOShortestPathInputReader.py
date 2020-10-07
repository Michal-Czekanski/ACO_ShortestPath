import unittest

from src.Classes.ACOShortestPathInputReader import ACOShortestPathInputReader
from src.Classes.Vertex import Vertex
from src.Classes.Edge import Edge
from src.Classes.Graph import Graph

import os

class TestACOShortestPathInputReader(unittest.TestCase):
    def test_readGraphFromInputFile(self):
        testGraphContent = """vertexesNum = 2
edgesNum = 1
1. 1 2 9
"""
        testFilename = "test_readGraphFromInputFile"

        testFile = open(testFilename, mode="x")
        testFile.write(testGraphContent)
        testFile.close()

        resultGraph: Graph
        try:
            resultGraph = ACOShortestPathInputReader.readGraphFromInputFile(testFilename)
        except Exception as e:
            os.remove(testFilename)
            raise e

        os.remove(testFilename)

        self.assertEqual(len(resultGraph.vertexes), 2)
        self.assertEqual(resultGraph.vertexes[0].ind, 1)
        self.assertEqual(resultGraph.vertexes[1].ind, 2)
        self.assertEqual(len(resultGraph.edges), 1)
        self.assertEqual(resultGraph.edges[0].weight, 9)



if __name__ == "__main__":
    unittest.main()
