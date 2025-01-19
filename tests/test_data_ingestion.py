import os
import pandas as pd
from src.data_ingestion import DataIngestion

def test_di():
    # Fetch data and stored it.
    tickers = [
    "AAPL", "MSFT", "AMZN", "NVDA", "GOOGL", "META", "TSLA", "BRK.B", "JPM", "V",
    "JNJ", "PG", "UNH", "MA", "PFE", "XOM", "CVX", "KO", "PEP", "MRK",
    "DIS", "ADBE", "INTC", "CRM", "AVGO", "COST", "NFLX", "AMD", "PYPL", "QCOM",
    "T", "VZ", "TXN", "CSCO", "MMM", "HON", "ABBV", "BMY", "AMGN", "LLY",
    "TMO", "ISRG", "DHR", "LMT", "RTX", "BA", "SBUX", "MCD", "NKE", "LULU"
    ]
    start_date = '2022-01-01'
    end_date = '2022-12-31'
    interval = '1d'
    
    # fetch and store the Apple Stocks data
    di = DataIngestion(tickers, start_date, end_date, interval)
    di.fetch_store()
    
if __name__ == '__main__':
    test_di()