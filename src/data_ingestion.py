from datetime import datetime 
from pathlib import Path
from typing import List
import yfinance as yf
import os

class DataIngestion:
    def __init__(self, tickers : List[str], start_date : str = None, end_date : str = None, interval : str = '1d', save_dir : str = 'data'):
        self.tickers = tickers 
        self.start_date = start_date
        self.end_date = end_date 
        self.interval = interval 
        self.save_dir = save_dir
        os.makedirs(save_dir, exist_ok=True)
    
    def validate_args(self) -> None:
        ''''
        Validate the passing arguments to avoid future conflits
        '''
        if self.tickers is None:
            raise 'No tickers were provided!'
        elif self.start_date is None:
            raise 'Start date is not provided :('
        elif self.end_date is None:
            raise 'End date is not provided ;('
        else:
            print('All arguments are properly passed [-_-]')
            
    def fetch_store(self) -> None:
        '''
        Fetched the data from yahoo finance API and stored it.
        '''
        # validate arguments
        self.validate_args()
        
        for ticker in self.tickers:
            data = yf.download([ticker], start=self.start_date, end=self.end_date, interval=self.interval) 
            
            # make separate directory to save the fetch stocks depends on user
            UID = datetime.now().strftime('%d%m%Y%H')
            dir_path = f'data/user_{UID}'
            os.makedirs(dir_path,exist_ok=True)
            
            self.save_dir = dir_path 
            file_path = os.path.join(self.save_dir,Path(f'{ticker}.csv'))
            data.to_csv(file_path)
            print(f'Fetched data saved sucessfully at {file_path} of ticker : {ticker}')