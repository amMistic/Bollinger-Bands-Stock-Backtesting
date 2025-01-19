from src.boillinger_bands_strategy import BollingerBandsStrategy
import pandas as pd
import os 

def test_bbs():
    # load dataset
    file_path = 'data\\GOOGL.csv'
    df = pd.read_csv(file_path)
    df = df.iloc[2:]        # avoid title and date row
    
    # Display original fetched data
    print('Before Apply Boillinger Bands Strategy\n')
    print(df.head())
    print('\n\n')
    
    strategy = BollingerBandsStrategy()
    updated_df = strategy.strategy(df) 
    
    # display updated
    print('After Applying Boillinger Band Strategy\n')
    print(updated_df.head())
    
    return updated_df

if __name__ == '__main__':
    test_bbs()