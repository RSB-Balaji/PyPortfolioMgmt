from datetime import datetime as dt

from portfolio import PortfolioSet
from portfolio import Portfolio

start = dt(2018,1,1)
end = dt(2018,12,31)

p1 = PortfolioSet(["AAPL","TSLA","F"])

p1.getDailyReturns(start, end)
p1.plotReturns()

port = Portfolio(p1, [0.1,0.2,0.7])
