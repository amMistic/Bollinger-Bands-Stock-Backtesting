import pandas as pd

class  BollingerBandsStrategy:
    def __init__(self, window_size : int = 20, std_deviation : float = 2):
        self.window_size = window_size
        self.std_deviation = std_deviation
    
    def strategy(self, data : pd.DataFrame) -> pd.DataFrame:
        '''
        Apply the Boillinger Bands Strategy on fetched data.
        '''
        
        # Validate data is provided or not
        if data is None:
            raise 'No data is Provided! Please pass `data` :/ '
        
        # ensure values are numeric
        data['Close'] = pd.to_numeric(data['Close'], errors='coerce')

        # applying boiler band strategy
        data['SMA'] = data['Close'].rolling(window=self.window_size).mean()
        data['Upper_Band'] = data['SMA'] + self.std_deviation * data['Close'].rolling(window=self.window_size).std()
        data['Lower_Band'] = data['SMA'] - self.std_deviation * data['Close'].rolling(window=self.window_size).std()
        data['Buy'] = data['Close'] < (data['Lower_Band'] * 0.98)
        data['Sell'] = data['Close'] >= data['Upper_Band']

        # # Steps to avoid getting NAN at first few row equal to window size
        data.bfill(inplace=True)
        
        # replace the `Price` feature with `Date`
        data.rename(columns={"Price": "Date"}, inplace=True)
        
        # returned modified dataframe 
        return data

         