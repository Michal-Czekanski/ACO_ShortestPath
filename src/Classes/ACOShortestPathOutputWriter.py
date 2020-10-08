import datetime


class ACOShortestPathOutputWriter:

    

    @staticmethod
    def createOutpuFilename(launchingTimeAndDate: datetime.datetime, inputFilename: str,
                            vertexStartInd: int, vertexEndInd: int, pheromoneInfluence: float,
                            desirabilityInfluence: float,
                            evaporationCoefficent: float, itersNum: int):
        """
        Creates unique output filename in format: inputFilename_launchTimeAndDate_parameters
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
        strLaunchingTimeAndDate = launchingTimeAndDate.strftime("%d_%m_%Y")

        outputFilename += "_{}_{}_{}_{}_{}_{}_{}.txt".format(strLaunchingTimeAndDate, str(vertexStartInd),
                                                             str(vertexEndInd),
                                                             str(pheromoneInfluence), str(desirabilityInfluence),
                                                             str(evaporationCoefficent), str(itersNum))

        return outputFilename
