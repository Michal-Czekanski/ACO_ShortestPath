from src.Classes.Path import Path
from datetime import datetime


class ACOShortestPathOutputData:
    timeFormatString = "%H:%M:%S %d/%m/%Y"

    printAllPaths: bool
    path: Path
    elapsedTime: datetime
    algorithmEndTime: datetime
    algorithmStartTime: datetime
    itersNum: int
    evaporationCoefficent: float
    desirabilityInfluence: float
    pheromoneInfluence: float
    vertexEndInd: int
    vertexStartInd: int
    runNumber: int
    inputFilename: str

    def __init__(self, runNumber: int, inputFilename: str, vertexStartInd: int, vertexEndInd: int,
                 pheromoneInfluence: float,
                 desirabilityInfluence: float,
                 evaporationCoefficent: float, itersNum: int, algorithmStartTime: datetime, algorithmEndTime: datetime,
                 elapsedTime: datetime, path: Path,
                 printAllPaths: bool, pathToAllPathsFile: str):
        self.runNumber = runNumber
        self.inputFilename = inputFilename
        self.vertexStartInd = vertexStartInd
        self.vertexEndInd = vertexEndInd
        self.pheromoneInfluence = pheromoneInfluence
        self.desirabilityInfluence = desirabilityInfluence
        self.evaporationCoefficent = evaporationCoefficent
        self.itersNum = itersNum
        self.algorithmStartTime = algorithmStartTime
        self.algorithmEndTime = algorithmEndTime
        self.elapsedTime = elapsedTime
        self.path = path
        self.printAllPaths = printAllPaths
        self.pathToAllPathsFile = pathToAllPathsFile
