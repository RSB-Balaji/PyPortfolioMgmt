from datetime import datetime as dt

from portfolio import PortfolioSet
from portfolio import Portfolio
from capm import Capm

start = dt(2018,1,1)
end = dt(2018,12,31)

p1 = PortfolioSet(["JNJ","PG","V"])

p1.getDailyReturns(start, end)
#p1.plotReturns()

c = Capm(p1)
opt = c.calcOptPortfolio(0.004,1000)
#c.plotCAL()
c.plotSML("JNJ")