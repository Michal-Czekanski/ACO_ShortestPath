from src.Classes.ACOShortestPathOutputData import ACOShortestPathOutputData

import datetime
import os
import typing


class ACOShortestPathOutputWriter:

    @staticmethod
    def writeOutputToFile(filePath: str, data: ACOShortestPathOutputData):
        contentToWrite = data.getDataAsString()

        file = open(filePath, "a")
        file.write(contentToWrite)

        if data.printAllPaths:
            file.write("\nAll paths:\n")
            allPathsFile = open(data.pathToAllPathsFile, "r")

            pathFromFile = allPathsFile.readline()
            while pathFromFile:
                file.write(pathFromFile)

            allPathsFile.close()
        file.close()

    @staticmethod
    def createOutputFile(outputDataDirPath: str, launchingTimeAndDate: datetime.datetime, inputFilename: str,
                         vertexStartInd: int, vertexEndInd: int, pheromoneInfluence: float,
                         desirabilityInfluence: float,
                         evaporationCoefficent: float, itersNum: int) -> typing.Union[str, None]:
        """
        Creates output file with unique name.
        :param outputDataDirPath:
        :param launchingTimeAndDate:
        :param inputFilename:
        :param vertexStartInd:
        :param vertexEndInd:
        :param pheromoneInfluence:
        :param desirabilityInfluence:
        :param evaporationCoefficent:
        :param itersNum:
        :return: If file was created successfully: file's absolute path, else: None
        """

        outputFilename = ACOShortestPathOutputWriter.createOutputFilename(launchingTimeAndDate, inputFilename,
                                                                          vertexStartInd, vertexEndInd,
                                                                          pheromoneInfluence, desirabilityInfluence,
                                                                          evaporationCoefficent, itersNum)

        outputFilePath = os.path.abspath(os.path.join(outputDataDirPath, outputFilename))

        try:
            outputFile = open(outputFilePath, "x")
            outputFile.close()
        except Exception as e:
            return None

        return outputFilePath

    @staticmethod
    def createOutputFilename(launchingTimeAndDate: datetime.datetime, inputFilename: str,
                             vertexStartInd: int, vertexEndInd: int, pheromoneInfluence: float,
                             desirabilityInfluence: float,
                             evaporationCoefficent: float, itersNum: int):
        """
        Creates unique output filename in format: inputFilename_launchTimeAndDate_parameters.
        launchTimeAndDate in format: Year_Month_Day_Hour_Minute
        :param launchingTimeAndDate:
        :param inputFilename:
        :param vertexStartInd:
        :param vertexEndInd:
        :param pheromoneInfluence:
        :param desirabilityInfluence:
        :param evaporationCoefficent:
        :param itersNum:
        :return: Unique output filename.
        """
        outputFilename = inputFilename.split('.')[0]
        strLaunchingTimeAndDate = launchingTimeAndDate.strftime("%Y_%m_%d_%H_%M")

        outputFilename += "_{}_{}_{}_{}_{}_{}_{}.txt".format(strLaunchingTimeAndDate, str(vertexStartInd),
                                                             str(vertexEndInd),
                                                             str(pheromoneInfluence), str(desirabilityInfluence),
                                                             str(evaporationCoefficent), str(itersNum))

        return outputFilename
