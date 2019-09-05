class Capm:
	"""
	Capm class is implementation of Capital Asset Pricing Model.
	"""
	def __init__(self, portfolioSet):
		"""
		Initializes the portfolio set on which CAPM concepts are to be applied.
		"""
		self.portSet = portfolioSet

	def calcOptPortfolio(self, riskFreeRate):
		"""
		Calculates and returns the optimum Portfolio (Portfolio obj).

		Parameters:
		-----------

		riskFreeRate (float) : Risk-free rate of return.
		"""
		self.riskFreeRate

		self.optPortfolio 

		return self.optPortfolio

	def getMaxSharpeRatio(self ):
		"""
		Returns the max Sharpe Ratio.
		"""
		self.maxSharpeRatio

	def plotEfficientFrontier(self ):
		"""
		Plots Efficient Frontier for the given Portfolio.
		"""

	def plotCAL(self ):
		"""
		Plots Capital Allocation Line.
		"""

	def getWeightsfromCAL(self, std):
		"""
		Returns weights of portfolio on the CAL for given risk(std).

		Parameters:
		-----------

		std (float) : Standard deviation value on the Capital Allocation Line.
		"""

	def plotSML(self, ticker):
		"""
		Plots Security Market Line for given ticker with the Market Portfolio(S&P500).

		Parameters:
		-----------
		ticker (str) : Ticker of stock from Portfolio.
		"""