class PortfolioSet:
    """
    PortfolioSet class holds set of assets and it's information 
    that are used to form a Portfolio.
    """
    def __init__(self, tickers):
        """
        Parameters:
        -----------
        tickers (list) : A list of ticker symbols(str) of stocks.
        """
        self.tickers = tickers

    def getReturns(self, startDate, endDate):
        self.dReturns
        self.startDate
        self.endDate

    def plotReturns(self ):
        """
        Plots Returns of all stocks in the Portfolio set.
        """

    def plotRetDist(self, ticker, bins):
        """
        Plots Returns distribution of given stock(ticker). Density distribution 
        and Normal distribution are plotted on top of histrogram.
        """
    
class Portfolio:
    """
    Portfolio class is holds set assets and their respective contribution 
    to the Portfolio.
    """
    def __init__(self, portfolioSet, weights):
        self.portSet = portfolioSet
        self.weights = weights
    
    def setWeights(self, weights)
        """
        Assigns weight to each asset of the Portfolio.
        """
        self.weights = weights
            
    def getPortReturns(self ):
        """
        Calculates and returns the net Portfolio Returns.
        """
        self.returns

    def getPortRisk(self ):
        """
        Calculates and returns the net Portfolio Risk.
        """
        self.risk

    def printInfo(self ):
        """
        Prints a table of information about the Portfolio. Informations 
        like tickers, Weights, Returns, Risk.
        """