import pandas_datareader.data as data
from pandas_datareader.famafrench import get_available_datasets

import statsmodels.api as sm

class FamaFrench:
    """
    FamaFrench class is implementation of the Fama-French three factor model.
    """
    def __init__(self, portfolioSet):
        self.portSet = portfolioSet

    def printThreeFactorDataList(self ):
        """
        Obtains the list of datasets from Kenneth French data library related 
        to the 3 factor model.
        http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html
        (Kenneth French data library)
        """
        ffData = get_available_datasets()
        self.ff3DataList = [dataset for dataset in ffData if '3_Factors' in dataset]
        for i in range(0, len(self.ff3DataList)):
            print(i,'.',self.ff3DataList[i])

    def getThreeFactorData(self, datasetIdx):
        """
        Obtains the given dataset (datasetIdx) from the Kenneth French library.
        Parameters:
        -----------
        datasetIdx (int) :  index of datasets obtained from getThreeFactorDataList().
        """
        df3Factor = data.DataReader(self.ff3DataList[datasetIdx], 'famafrench', self.portSet.startDate, self.portSet.endDate)
        self.ff3FactorData = df3Factor[0]
        self.ff3FactorData.index = self.ff3FactorData.index.astype('datetime64[ns]')
        print(self.ff3FactorData.head())

    def fitModel(self , ticker):
        """
        Fits the Three Factor model to given ticker from the portfolioSet.
        """
        dropIdx = set(self.ff3FactorData.index).difference(set(self.portSet.dReturns.index.intersection(self.ff3FactorData.index)))
        self.ff3FactorData.drop(index =dropIdx, inplace =True)

        xRet = (self.portSet.dReturns[ticker]*100 - self.ff3FactorData['RF'])

        Y = xRet
        X = self.ff3FactorData.iloc[ :, 0:3]
        X = sm.add_constant(X)

        self.model = sm.OLS(Y,X)
        result = self.model.fit()
        print(result.summary())

        return result