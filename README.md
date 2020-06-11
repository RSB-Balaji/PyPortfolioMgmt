# PyPortfolioMgmt

PyPortfolioMgmt is a library that implements concepts of **multi-factor** model for portoflio management.
It aims to indentify, capture and relate the factors to asset prices, and use this information to 
build portfolios.

PyPortfolioMgmt is designed by keeping in mind the perspective of a **researcher** who wants to study and
analyse multiple factors that contribute to fluctuations in asset prices.

## Table of contents
- [Table of contents](https://github.com/RSB-Balaji/PyPortfolioMgmt/tree/readme#table-of-contents)
- [Getting started](https://github.com/RSB-Balaji/PyPortfolioMgmt/tree/readme#getting-started)
- [An overview of portfolio management](https://github.com/RSB-Balaji/PyPortfolioMgmt/tree/readme#an-overview-of-portfolio-management)
- [Factor theory](https://github.com/RSB-Balaji/PyPortfolioMgmt/tree/readme#factor-theory)
- [Capital Asset Pricing Model](https://github.com/RSB-Balaji/PyPortfolioMgmt/tree/readme/#capital-asset-pricing-model)
- [Multi-Factor Model](https://github.com/RSB-Balaji/PyPortfolioMgmt/tree/readme#multi-factor-model)
- [Workflow](https://github.com/RSB-Balaji/PyPortfolioMgmt/tree/readme#workflow)

### Getting started
For installation,

```
pip install pyportmgmt
```
### An overview of portfolio management
Portfolio Management is the art and science of combining assets with different expected returns and 
volatilities, so that one can decide on mathematically optimal allocation which minimises the risk
for a target return - the set of all such optimal portfolio is reffered to as efficient frontier.
Harry Markowitz's 1952 paper is the undeniable classic which explains this.

The key insights is,
A portfolio must have
  - **minimised risk** (for a given target return)
  - **maximised returns** (for a given target risk)
        
### Factor theory
>"Factors are to assets, what nutritions are to food."

Assets earn risk premiums because they are exposed to underlying factor risks.

Takeaways from factor theory,
  - Factors matters, not assets.
  - Assets of bundles of factors.
  - Different investor need different risk factor.

### Capital Asset Pricing Model
The **Capital Asset Pricing Model (CAPM)**, the first theory of factor risk, states that
assets that crash when the market loses money are risky and therefore must reward their 
holders with high risk premiums. While the CAPM defines bad times as low market returns,
mutifactor models capture multiple definitions of bad times across many factors and states
of nature.

Takeaways from CAPM model,
  - Don't hold an individual asset, hold a factor.
  - Each investor has his/her own optimal exposure of factor risk.
  - The average investor holds the market.
  - The factor risk premium has an economic story.
  - Risk is factor exposure.
  - Assets paying off in bad times,have low risk premiums.

CAPM predicts that asset risk premiums depend only on the asset's beta and there is 
only one factor that matters, the market portfolio.

Functions of CAPM supported by the package,
  - Calculating Optimum Portfolio
  - Obtaining Max Sharpe Ratio
  - Plotting Efficient Frontier
  - Plotting Capital Allocation Line
  - Plotting Security Market Line
  
#### A quick example
```python
from datetime import datetime as dt

from pyportmgmt import PortfolioSet
from pyportmgmt imoprt Portfolio
from pyportmgmt import Capm

# start date and end dates of daily returns for portfolioSet
startDate = dt(2018,1,1)
endDate = dt(2018,12,31)

# creating portfolioSet object for given tickers
portSet = PortfolioSet(tickers= ["JNJ","PG","V"])
# obtain daily prices and calc log returns
portSet.getReturns(startDate, endDate)

# creating Capm object for the created PortfolioSet object
c = Capm(portSet)
#obtain the optimum portfolio
optPort = c.calcOptPortfolio(riskFreeRate= 0.004, nRandPortfolio= 1000)
c.plotSML(ticker= "JNJ")
```
 
### Multi-Factor Model
Multi-factor model recognize that bad times can be defined more broadly than 
just bad returns on the market portfolio. Each factor in a multi-factor model 
provides its own definition of bad times.

#### Fama-French Three Factor Model
Fama-French three factor model is one such multi-factor model. This model 
focuses on three factors,
  - Capm market factor
  - SMB (size factor) 
  - HML (value factor)

A quick example
```python
from datetime import datetime as dt

from pyportmgmt import PortfolioSet
from pyportmgmt imoprt Portfolio
from pyportmgmt import FamaFrench

# start date and end dates of daily returns for portfolioSet
startDate = dt(2018,1,1)
endDate = dt(2018,12,31)

# creating portfolioSet object for given tickers
portSet = PortfolioSet(tickers= ["JNJ","PG","V"])
# obtain daily prices and calc log returns
portSet.getReturns(startDate, endDate)

# creating FamaFrench object
f = FamaFrench(portSet)
f.printThreeFactorDataList()
# index value obtained from results of previous function
f.getThreeFactorData(index = 11)
f.fitModel(ticker ="PG")
```

### Workflow
![](flowdiag.png)
