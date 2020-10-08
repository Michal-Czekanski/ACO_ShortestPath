from src.Classes.ACOShortestPathOutputData import ACOShortestPathOutputData
from src.Classes.Vertex import Vertex
from src.Classes.Edge import Edge
from src.Classes.Path import Path

import datetime
import unittest


class TestACOShortestPathOutputData(unittest.TestCase):
    def test_getDataAsString(self):
        testRunNumber = 1
        testInputFilename = "testInputFilename.txt"
        testVertexStartInd = 1
        testVertexEndInd = 2
        testPheromoneInfluence = 0.1
        testDesirabilityInfluence = 0.1
        testEvaporationCoefficent = 0.1
        testItersNum = 10
        testAlgorithmStartTime = datetime.datetime.strptime("2020_01_29_12_59", "%Y_%m_%d_%H_%M")
        testAlgorithmEndTime = datetime.datetime.strptime("2020_01_29_13_59", "%Y_%m_%d_%H_%M")
        testElapsedTime = testAlgorithmEndTime - testAlgorithmStartTime

        v1 = Vertex(1)
        v2 = Vertex(2)
        e = Edge(v1, v2, 9)
        testPath = Path(v1, [e], e.weight)

        testData = ACOShortestPathOutputData(testRunNumber, testInputFilename, testVertexStartInd, testVertexEndInd,
                                         testPheromoneInfluence, testDesirabilityInfluence,
                                         testEvaporationCoefficent, testItersNum,
                                         testAlgorithmStartTime, testAlgorithmEndTime, testElapsedTime,
                                         testPath, False, "")
        expectedDataAsString = """
------------------------------------
Run:          1
Input:        testInputFilename.txt
Parameters:
    - vertex_start =            1
    - vertex_end =              2
    - pheromone_influence =     0.1
    - desirability_influence =  0.1
    - evaporation_coefficent =  0.1
    - iters_num  =              10
Start:        12:59:00 29/01/2020
End:          13:59:00 29/01/2020
Time running: 3600.0 sec

Shortest path:
weight =      9
1 - 2 --- weight = 9
------------------------------------"""

        actualDataAsString = testData.getDataAsString()

        self.assertEqual(expectedDataAsString, actualDataAsString)


if __name__ == "__main__":
    unittest.main()
