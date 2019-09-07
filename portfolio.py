from datetime import datetime as dt

import numpy as np 
import scipy.stats as stats
import pandas as pd 
from pandas_datareader import data
import matplotlib.pyplot as plt
import statsmodels.api as sm

from prettytable import PrettyTable

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

    def getDailyReturns(self, startDate, endDate):
        """
        Obtains daily prices of assets from yahoo finance form 
        startDate to endDate. Log returns are calculated and 
        stored to dReturns(DataFrame).
        """
        self.startDate = startDate
        self.endDate = endDate

        price = data.DataReader(self.tickers,'yahoo',self.startDate,self.endDate)['Adj Close']
        self.dReturns = pd.DataFrame(np.log(price)-np.log(price).shift(1),index=price.index)
        self.dReturns.columns = self.tickers
        self.dReturns.dropna(inplace  = True)

    def plotReturns(self ):
        """
        Plots Returns of all stocks in the Portfolio set.
        """
        self.dReturns.plot()

    def plotRetDist(self, ticker, bins):
        """
        Plots Returns distribution of given stock(ticker). Density distribution 
        and Normal distribution are plotted on top of histrogram.
        
        Parameters:
        -----------
        ticker (str): Ticker symbol of stock from the PortfolioSet
        bins (int): Number of bins in the histogram.
        """
        mu = self.dReturns[ticker].mean()
        std = self.dReturns[ticker].std()

        plt.hist(self.dReturns[ticker],bins,density=True)
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin,xmax,1000)
        p = stats.norm.pdf(x,mu,std)
        self.dReturns[ticker].plot.density(label ="Density curve")
        plt.plot(x,p,'k',linewidth =2, label ="Normal Distribution")
        plt.title("Distribution of daily returns (bins :"+str(bins)+")")
        plt.legend()
        plt.xlabel("Returns")
        plt.show()

class Portfolio:
    """
    Portfolio class is holds set assets and their respective contribution 
    to the Portfolio.
    """
    def __init__(self, portfolioSet, weights):
        self.portSet = portfolioSet
        self.weights = weights

    def setWeights(self, weights):
        """
        Assigns weight to each asset of the Portfolio.
        """
        if(self._validateWeights(weights)):
            self.weights = np.array(weights)
        
    def _validateWeights(self ,weights):
        try:
            if (np.sum(weights) == 1.0):
                raise
        except:
            print("Weights don't add up to 1.0")
            
    def getPortReturns(self ):
        """
        Calculates and returns the net Portfolio Returns.
        """
        mu = np.array(self.portSet.dReturns.mean())
        self.returns = np.sum(self.weights*mu)
        return self.returns

    def getPortRisk(self ):
        """
        Calculates and returns the net Portfolio Risk.
        """
        cov = self.portSet.dReturns.cov()
        self.risk = np.dot(self.weights.T,np.dot(cov,self.weights))
        return self.risk

    def printInfo(self ):
        """
        Prints a table of information about the Portfolio. Informations 
        like tickers, Weights, Returns, Risk.
        """
        table1 = PrettyTable(field_names=["Tickers","Weights"],header= True)
        for i in range(0,len(self.portSet.tickers)):
            table1.add_row([self.portSet.tickers[i],self.weights[i]])
        print(table1)

        table2 = PrettyTable(field_names= ["Portfolio Return","Portfolio Risk"],header=True)
        table2.add_row([self.getPortReturns(),self.getPortRisk()])
        print(table2)