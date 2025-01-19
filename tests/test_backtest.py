from src.boillinger_bands_strategy import BollingerBandsStrategy
from src.backtest import BackTest
import pandas as pd
import os

def test_backtest():
    # load the dataframe
    file_path = 'data\\AAPL.csv'
    df = pd.read_csv(file_path)
    df.rename(columns={'Price' : 'Date'}, inplace=True)
    df = df[2:]
    print('DataFrame:\n')
    print(df.head())
    
    
    # # load the strategy object
    # strategy = BollingerBandsStrategy()
    # update_df = strategy.strategy(df)
    
    # print('Updated DataFrame:\n')
    # print(update_df.head())
    
    # # load backtest object
    # bt = BackTest()
    # trades = bt.run(data=update_df)
    
    # print('\n\n')
    # print(trades.head())

if __name__ == '__main__':
    test_backtest()