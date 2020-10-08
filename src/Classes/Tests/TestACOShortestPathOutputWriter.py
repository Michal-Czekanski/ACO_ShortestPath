from src.Classes.ACOShortestPathOutputWriter import ACOShortestPathOutputWriter
from src.Classes.ACOShortestPathOutputData import ACOShortestPathOutputData
from src.Classes.Vertex import Vertex
from src.Classes.Edge import Edge
from src.Classes.Path import Path

import unittest
import datetime
import os


class TestACOShortestPathOutputWriter(unittest.TestCase):
    def test_writeOutputToFile_withoutAllPaths(self):

        # Initialize data
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
        testPrintAllPaths = False
        testPathToAllPathsFile = ""

        testData = ACOShortestPathOutputData(testRunNumber, testInputFilename, testVertexStartInd, testVertexEndInd,
                                             testPheromoneInfluence, testDesirabilityInfluence,
                                             testEvaporationCoefficent, testItersNum,
                                             testAlgorithmStartTime, testAlgorithmEndTime, testElapsedTime,
                                             testPath, testPrintAllPaths, testPathToAllPathsFile)

        testOutputFilename = "test_writeOutputToFile_withoutAllPaths"
        outputDataDirPath = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, os.pardir, os.pardir, "Data",
                                                         "OutputResultFiles"))
        testOutputFilePath = os.path.join(outputDataDirPath, testOutputFilename)

        # Testing
        ACOShortestPathOutputWriter.writeOutputToFile(testOutputFilePath, testData)

        expectedFileContent = """
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

        actualFileContent = ""

        actualFile = open(testOutputFilePath, "r")
        line = actualFile.readline()
        while line:
            actualFileContent += line
            line = actualFile.readline()
        actualFile.close()
        os.remove(testOutputFilePath)

        self.assertEqual(expectedFileContent, actualFileContent)





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

    def test_createOutputFile(self):
        testLaunchingTimeAndDate = datetime.datetime.strptime("2020_01_29_12_59", "%Y_%m_%d_%H_%M")
        testInputFilename = "testInputFilename.txt"
        testVertexStartInd = 1
        testVertexEndInd = 2
        testPheromoneInfluence = 0.1
        testDesirabilityInfluence = 0.1
        testEvaporationCoefficent = 0.1
        testItersNum = 10

        outputDataDirPath = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, os.pardir, os.pardir, "Data",
                                                         "OutputResultFiles"))

        expectedOutputFilePath = os.path.join(outputDataDirPath,
                                              "testInputFilename_2020_01_29_12_59_1_2_0.1_0.1_0.1_10.txt")

        resultOutputFilePath = ACOShortestPathOutputWriter.createOutputFile(outputDataDirPath, testLaunchingTimeAndDate,
                                                                            testInputFilename,
                                                                            testVertexStartInd,
                                                                            testVertexEndInd,
                                                                            testPheromoneInfluence,
                                                                            testDesirabilityInfluence,
                                                                            testEvaporationCoefficent,
                                                                            testItersNum)

        self.assertEqual(expectedOutputFilePath, resultOutputFilePath)
        self.assertTrue(os.path.isfile(resultOutputFilePath))
        os.remove(resultOutputFilePath)


if __name__ == "__main__":
    unittest.main()
