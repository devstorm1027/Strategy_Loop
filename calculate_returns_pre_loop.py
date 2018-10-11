import pandas as pd


class Strategy_loop(object):

    def calculate_returns(self, dfHistory, dfStrategyList):
        Parameter1_list = list(dfStrategyList['Parameter1'])
        Parameter2_list = list(dfStrategyList['Parameter2'])
        Parameter3_list = list(dfStrategyList['Parameter3'])
        Strategy_ID_list = list(dfStrategyList['StrategyID'])

        for i, v in enumerate(Strategy_ID_list):
            Parameter1 = Parameter1_list[i]
            Parameter2 = Parameter2_list[i]
            Parameter3 = Parameter3_list[i]
            return_header = 'Strategy{}Return'.format(str(v))
            dfHistory[return_header] = (dfHistory['Open'] * Parameter1)-(dfHistory['Volume'] * Parameter2)+(Parameter1 * Parameter3)

        dfHistory = dfHistory.drop('Open', axis=1)
        dfHistory = dfHistory.drop('Volume', axis=1)

        cols = dfHistory.columns.tolist()
        cols = cols[1:2] + cols[0:1] + cols[2:]

        dfHistory = dfHistory.reindex(columns=cols)
        dfHistory.to_csv('dfOutput.csv', index=False)

        return dfHistory

if __name__ == '__main__':
    dfStrategyList = pd.read_csv('StrategyList_short.csv')
    dfHistory = pd.read_csv('dfHistory_short.csv')

    strategy_loop = Strategy_loop()
    strategy_loop.calculate_returns(dfHistory, dfStrategyList)
