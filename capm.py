from datetime import datetime as dt

import numpy as np
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt
import statsmodels.api as sm

from portfolio import PortfolioSet
from portfolio import Portfolio
from portfolio import _getFromQuandl

class Capm:
	"""
	Capm class is implementation of Capital Asset Pricing Model.
	"""
	def __init__(self, portfolioSet):
		"""
		Initializes the portfolio set on which CAPM concepts are to be applied.
		"""
		self.portSet = portfolioSet

	def calcOptPortfolio(self, riskFreeRate, nRandPortfolio):
		"""
		Calculates and returns the optimum Portfolio (Portfolio obj).

		Parameters:
		-----------
		riskFreeRate (float) : Risk-free rate of return.
		nRandPortfolio (int) : Number of Random Portfolios.
		"""
		self.riskFreeRate = riskFreeRate

		mu = list(self.portSet.dReturns.mean())
		cov = self.portSet.dReturns.cov()
		sd = list(self.portSet.dReturns.std())

		_mu = []
		_sd = []
		_sr = []
		_weights = []

		np.random.seed(555)
		i = 1
		while i <= nRandPortfolio:
			#generating random weights for portfolio
			w = np.random.random(len(mu))
			w /= np.sum(w)
			_weights.append(w)
			#mean of the portfolio
			m = np.sum(w*mu)
			_mu.append(m)
			#std of the portfolio
			s = np.sqrt(np.dot(w.T,np.dot(cov,w)))
			_sd.append(s)
			#sharpe ratio
			_sr.append((m - riskFreeRate)/s)
			i += 1
		
		maxSharpeRatioIdx = np.argmax(_sr)
		self.__mOptPort = _mu[maxSharpeRatioIdx]
		self.__sOptPort = _sd[maxSharpeRatioIdx]
		self.__maxSharpeRatio = _sr[maxSharpeRatioIdx]
		self.__wOptPort = _weights[maxSharpeRatioIdx]
		print(self.__wOptPort)
		self.optPort = Portfolio(self.portSet, self.__wOptPort)
		self.optPort.printInfo()
		self._plotEfficientFrontier(_mu, _sd)
		return self.optPort

	def getMaxSharpeRatio(self ):
		"""
		Returns the max Sharpe Ratio.
		"""
		return self.__maxSharpeRatio

	def _plotEfficientFrontier(self, _mu, _sd):
		"""
		Plots Efficient Frontier for the given Portfolio.
		"""
		#risk return plot
		plt.figure()
		plt.axhline(0, linewidth= 0.5, color="black")
		plt.axvline(0, linewidth= 0.5, color="black")

		mu = list(self.portSet.dReturns.mean())
		sd = list(self.portSet.dReturns.std())

		plt.scatter(x= _sd, y= _mu, s=4**2)
		plt.scatter(self.optPort.getPortRisk(), self.optPort.getPortReturns(), s= 6**2, c="black", label="Optimum Portfolio")
		plt.scatter(x= sd, y= mu, s= 6**2, c="brown")
		for i in range(0,len(self.portSet.tickers)):
			plt.annotate(self.portSet.tickers[i], xy=(sd[i],mu[i]))

		plt.title("Efficient Frontier")
		plt.xlabel("Standard Deviation")
		plt.ylabel("Mean Returns")
		plt.legend()
		plt.show()

	def plotCAL(self ):
		"""
		Plots Capital Allocation Line.
		"""
		mu = [self.riskFreeRate, ]
		mu.extend(list(self.portSet._getListPortMeans()))

		sd = [0.00, ]
		sd.extend(list(self.portSet._getListPortStd()))

		names = ["Rf", ]
		names.extend(list(self.portSet.tickers))

		slope = self.getMaxSharpeRatio()
		intercept = self.riskFreeRate
		x = np.divide(list(range(0,8)),100)
		abline = [slope*i + intercept for i in x]

		plt.figure()
		plt.axhline(0, linewidth= 0.5, color= "black")
		plt.axvline(0, linewidth= 0.5, color= "black")

		plt.plot(x, abline)
		plt.scatter(x =self.optPort.getPortRisk(),y =self.optPort.getPortReturns(),s =6**2, c="blue", label ="Tangent Portfolio")
		plt.scatter(x =sd, y =mu, c ="red", s =6**2)
		for i in range(0,len(names)):
			plt.annotate(names[i], xy=(sd[i],mu[i]))

		plt.title("Capital Allocation Line")
		plt.xlabel("Standard Deviation")
		plt.ylabel("Mean Returns")
		plt.legend()
		plt.show()

	def getWeightsfromCAL(self, std):
		"""
		Returns weights of portfolio on the CAL for given risk(std).

		Parameters:
		-----------
		std (float) : Standard deviation value on the Capital Allocation Line.
		"""
		optPortRisk = self.optPort.getPortRisk()
		return dict({"Risk-Free":round((1-std/optPortRisk),2),"Risky":round(std/optPortRisk)})

	def plotSML(self, ticker):
		"""
		Plots Security Market Line for given ticker with the Market Portfolio(S&P500).

		Parameters:
		-----------
		ticker (str) : Ticker of stock from Portfolio.
		"""
		st = pd.DataFrame(self.portSet.dReturns[ticker])

		sp500 = _getFromQuandl('SPY',self.portSet.startDate, self.portSet.endDate)
		sp500 = pd.DataFrame((np.log(sp500) - np.log(sp500).shift()), index =sp500.index)
		sp500.dropna(inplace =True)

		X = sp500.values
		Y = st.values

		#X_ = sm.add_constant(X)
		
		#model = sm.OLS(Y - self.riskFreeRate, X_).fit()

		#X2 = np.linspace(X.min(),X.max(),100)
		#Y_h = X2*model.params[1] + model.params[0]
		#print(model.summary())

		#plt.figure()
		#plt.scatter(X,Y,alpha =0.3)
		#plt.plot(X2,Y_h,'r',alpha =1)
		#plt.xlabel("S&P500")
		#plt.ylabel(ticker)
		#plt.title("Security Market Line")
		#plt.show()