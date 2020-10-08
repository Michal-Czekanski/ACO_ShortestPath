from src.Classes.ACOShortestPathOutputWriter import ACOShortestPathOutputWriter

import unittest
import datetime


class TestACOShortestPathOutputWriter(unittest.TestCase):
    def test_createOutputFilename(self):
        testLaunchingTimeAndDate = datetime.datetime.strptime("2020_01_29_12_59", "%Y_%m_%d_%H_%M")
        testInputFilename = "testInputFilename.txt"
        testVertexStartInd = 1
        testVertexEndInd = 2
        testPheromoneInfluence = 0.1
        testDesirabilityInfluence = 0.1
        testEvaporationCoefficent = 0.1
        testItersNum = 10

        expectedOutputFilename = "testInputFilename_2020_01_29_12_59_1_2_0.1_0.1_0.1_10.txt"
        resultOutputFilename = ACOShortestPathOutputWriter.createOutputFilename(testLaunchingTimeAndDate,
                                                                                testInputFilename,
                                                                                testVertexStartInd,
                                                                                testVertexEndInd,
                                                                                testPheromoneInfluence,
                                                                                testDesirabilityInfluence,
                                                                                testEvaporationCoefficent,
                                                                                testItersNum)

        self.assertEqual(expectedOutputFilename, resultOutputFilename)


if __name__ == "__main__":
    unittest.main()
