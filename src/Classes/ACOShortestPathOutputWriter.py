import datetime


class ACOShortestPathOutputWriter:

    

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
