from src.Classes.Path import Path
from datetime import datetime
from datetime import timedelta


class ACOShortestPathOutputData:
    timeFormatString = "%H:%M:%S %d/%m/%Y"

    pathToAllPathsFile: str
    printAllPaths: bool
    path: Path
    elapsedTime: timedelta
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
                 elapsedTime: timedelta, path: Path,
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

    def getDataAsString(self) -> str:
        """
        :return: Data in neat format which can be written to file.
        """
        dataAsString = """
------------------------------------
Run:          {}
Input:        {}
Parameters:
    - vertex_start =            {}
    - vertex_end =              {}
    - pheromone_influence =     {}
    - desirability_influence =  {}
    - evaporation_coefficent =  {}
    - iters_num  =              {}
Start:        {}
End:          {}
Time running: {}

Shortest path:
weight =      {}
{}
""".format(str(self.runNumber), self.inputFilename, str(self.vertexStartInd), str(self.vertexEndInd),
           str(self.pheromoneInfluence), str(self.desirabilityInfluence), str(self.evaporationCoefficent),
           str(self.itersNum),
           self.algorithmStartTime.strftime(ACOShortestPathOutputData.timeFormatString),
           self.algorithmEndTime.strftime(ACOShortestPathOutputData.timeFormatString),
           str(self.elapsedTime.total_seconds()) + " sec",
           str(self.path.cost),
           self.path.pathAsString())

        if self.printAllPaths:
            # TODO:
            pass

        dataAsString += "------------------------------------"

        return dataAsString
