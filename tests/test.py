from portfolio import PortfolioSet
from portfolio import Portfolio
from capm import Capm
from famafrench import FamaFrench

start = '2018-01-01'
end = '2018-12-31'

#Portfolio testing 
ps1 = PortfolioSet(["JNJ","PG","V"])
ps1.getDailyReturns(start, end)
#ps1.plotReturns()

#p1 = Portfolio(ps1, [0.4,0.3,0.3])

# CAPM testing 
c = Capm(ps1)
opt = c.calcOptPortfolio(0.004,1000)
#c.plotCAL()
c.plotSML("JNJ")

#FamaFrench testing
#f = FamaFrench(ps1)
#f.printThreeFactorDataList()
#f.getThreeFactorData(11)
#f.fitModel("PG")
