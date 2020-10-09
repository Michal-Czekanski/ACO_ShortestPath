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
                pathFromFile = allPathsFile.readline()

            allPathsFile.close()
        file.close()

    @staticmethod
    def createOutputFile(outputDataDirPath: str, inputFilename: str, vertexStartInd: int, vertexEndInd: int,
                         pheromoneInfluence: float, desirabilityInfluence: float, evaporationCoefficent: float,
                         itersNum: int) -> typing.Union[str, None]:
        """
        Creates output file with unique name.
        :param outputDataDirPath:
        :param inputFilename:
        :param vertexStartInd:
        :param vertexEndInd:
        :param pheromoneInfluence:
        :param desirabilityInfluence:
        :param evaporationCoefficent:
        :param itersNum:
        :return: If file was created successfully: file's absolute path, else: None
        """

        outputFilename = ACOShortestPathOutputWriter.createOutputFilename(inputFilename, vertexStartInd, vertexEndInd,
                                                                          pheromoneInfluence, desirabilityInfluence,
                                                                          evaporationCoefficent, itersNum)

        outputFilePath = os.path.abspath(os.path.join(outputDataDirPath, outputFilename))

        try:
            outputFile = open(outputFilePath, "x")
            outputFile.close()
        except FileExistsError:
            outputFile = open(outputFilePath, "a")
            outputFile.close()
        except Exception:
            return None

        return outputFilePath

    @staticmethod
    def createOutputFilename(inputFilename: str, vertexStartInd: int, vertexEndInd: int, pheromoneInfluence: float,
                             desirabilityInfluence: float, evaporationCoefficent: float, itersNum: int):
        """
        Creates unique output filename in format: inputFilename__parameters.
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

        outputFilename += "_{}_{}_{}_{}_{}_{}.txt".format(str(vertexStartInd),
                                                          str(vertexEndInd),
                                                          str(pheromoneInfluence), str(desirabilityInfluence),
                                                          str(evaporationCoefficent), str(itersNum))

        return outputFilename
