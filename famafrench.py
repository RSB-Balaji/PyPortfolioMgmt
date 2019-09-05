class FamaFrench:
    """
    FamaFrench class is implementation of the Fama-French three factor model.
    """
    def __init__(self, portfolioSet):
        self.portSet = portfolioSet

    def getThreeFactorList(self ):
        """
        Obtains the list of datasets from Kenneth French data library related 
        to the 3 factor model.
        """

    def getThreeFactorData(self, datasetIdx):
        """
        Obtains the datasets metioned from the Kenneth French library.

        Parameters:
        -----------
        datasetIdx (int) :  index of datasets obtained from getThreeFactorList.
        """
    
    def fitModel(self ):
        """
        Fits the Three Factor model to given portfolioSet.
        """
    
    def printSummary(self ):
        """
        Prints the summary of fitted model.
        """