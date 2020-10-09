import sys
import os

from datetime import datetime
from datetime import timedelta
from typing import IO

from src.Classes.ACOShortestPath import ACOShortestPath
from src.Classes.Graph import Graph
from src.Classes.ACOShortestPathInputReader import ACOShortestPathInputReader
from src.Classes.ACOShortestPathOutputData import ACOShortestPathOutputData
from src.Classes.ACOShortestPathOutputWriter import ACOShortestPathOutputWriter
from src.Classes.Path import Path
from src.Classes.Vertex import Vertex


def createInputFilePath(filename: str):
    """
    Creates absolute path to input file.
    All input files should be stored in Data/InputGraphFiles directory.
    :param filename:
    :return: Absolute path to given input file's name
    """
    filePath = os.path.abspath(os.path.join(__file__, os.pardir, "Data", "InputGraphFiles", filename))
    return filePath


projectRootDir = os.path.abspath(os.path.join(__file__, os.pardir))
outputDataDirPath = os.path.join(projectRootDir, "Data", "OutputResultFiles")
allPathsTempFilePath = os.path.join(projectRootDir, "Data", "allPathsTemp.txt")

if len(sys.argv) != 10:
    print("Invalid number of arguments.")
    print("Correct command:")
    print("python Run.py input_filename vertex_start vertex_end pheromone_influence "
          "desirability_influence evaporation_coefficent iters_num runs_num print_all_paths[y/n]")
    exit()

launchingTimeAndDate: datetime = datetime.now()

try:
    inputFilename: str = sys.argv[1]
    vertexStartInd: int = int(sys.argv[2])
    vertexEndInd: int = int(sys.argv[3])
    pheromoneInfluence: float = float(sys.argv[4])
    desirabilityInfluence: float = float(sys.argv[5])
    evaporationCoefficent: float = float(sys.argv[6])
    itersNum: int = int(sys.argv[7])
    runsNum: int = int(sys.argv[8])
    printAllPaths: bool = (lambda p: p.lower() == "y")(sys.argv[9])
except Exception as e:
    print("Arguments in wrong order.")
    print("Correct order:")
    print("python Run.py input_filename vertex_start vertex_end pheromone_influence "
          "desirability_influence evaporation_coefficent iters_num runs_num print_all_paths[y/n]")
    exit()

if printAllPaths:
    outputDataDirPath = os.path.join(outputDataDirPath, "ResultsWithAllPathsPrinted")

inputFilePath = os.path.join(projectRootDir, "Data", "InputGraphFiles", inputFilename)
inputGraph: Graph = ACOShortestPathInputReader.readGraphFromInputFile(inputFilePath)

vertexStart: Vertex = None
vertex: Vertex
for vertex in inputGraph.vertexes:
    if vertex.ind == vertexStartInd:
        vertexStart = vertex
        break

vertexEnd: Vertex = None
vertex: Vertex
for vertex in inputGraph.vertexes:
    if vertex.ind == vertexEndInd:
        vertexEnd = vertex
        break

outputFilePath = ACOShortestPathOutputWriter.createOutputFile(outputDataDirPath, launchingTimeAndDate, inputFilename,
                                                              vertexStartInd, vertexEndInd, pheromoneInfluence,
                                                              desirabilityInfluence, evaporationCoefficent, itersNum)

for runNum in range(1, runsNum + 1):

    if printAllPaths:
        # Redirect all prints to Data/allPathsTemp
        allPathsTempFile: IO = open(allPathsTempFilePath, "w")
        sys.stdout = allPathsTempFile

    startTime: datetime = datetime.now()

    algorithm = ACOShortestPath(pheromoneInfluence, desirabilityInfluence, evaporationCoefficent)
    shortestPath: Path = algorithm.findShortestPath(inputGraph, vertexStart, vertexEnd, itersNum, printAllPaths)

    endTime: datetime = datetime.now()
    elapsedTime: timedelta = endTime - startTime

    if printAllPaths:
        # Stop redirecting all prints to Data/allPathsTemp
        allPathsTempFile.close()
        sys.stdout = sys.__stdout__

    data: ACOShortestPathOutputData = ACOShortestPathOutputData(runNum, inputFilename, vertexStartInd, vertexEndInd,
                                                                pheromoneInfluence, desirabilityInfluence,
                                                                evaporationCoefficent, itersNum, startTime, endTime,
                                                                elapsedTime, shortestPath,
                                                                printAllPaths, allPathsTempFilePath)

    ACOShortestPathOutputWriter.writeOutputToFile(outputFilePath, data)
