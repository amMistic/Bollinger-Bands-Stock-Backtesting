import os
import pandas as pd
import streamlit as st
from typing import List, Tuple
from streamlit_carousel import carousel


from src.backtest import BackTest
from src.data_ingestion import DataIngestion
from src.data_visualization import generate_graph_html
from src.boillinger_bands_strategy import BollingerBandsStrategy

def process(tickers : List[str], start_date : str, end_date : str, interval : str = '1d') -> Tuple[pd.DataFrame, list] :
    '''
    Whole process from loading stocks to applying boillinger band strategy 
    
    Args:
        tickers : List of all stocks user interested
        start_date : Starting date of stock 
        end_date : Ending Date to stock
        interval : Interval between each stock details
        
    Returns:
        Updated DataFrame after applying Boillinger Band Strategy on Raw Data.
        DataFrame Contain details like Stock name, date in, buying price, date out, selling price, net profit .
    
    '''
    # Initialized the data frame to store stocks details
    final_results = []
    html_graphs = []
    
    # Get the stocks details
    di = DataIngestion(tickers=tickers, start_date=start_date, end_date=end_date, interval=interval)
    di.fetch_store()
    
    # load the object
    strategy = BollingerBandsStrategy()
    
    # load the backtest object
    bt = BackTest()
    
    stocks_csv = os.listdir(di.save_dir)
    for csv in stocks_csv:
        file_path = os.path.join(di.save_dir,csv)
        
        # load the file 
        df = pd.read_csv(file_path)
        df = df[2:]
        
        # apply boillinger bands strategy
        update_df = strategy.strategy(df)
        
        # get the trades 
        trades = bt.run(update_df)
        final_results.append(trades)
        
        # get stocks name
        stockname = str(csv.split('.')[0])
        
        # store the graphs to display 
        graph = generate_graph_html(update_df, stock_name=stockname)
        html_graphs.append(graph)

    return final_results, html_graphs

# def save_graphs( fig, stock_name, output_dir="graphs/") : 
#     '''
#     Save the stocks visuals in graphs directory.
    
#     Args:
#         fig : Visual graph of stock trends in specificed time period.
#         stock_name : Name of stock
#         output_dir : Output directory name where graphs will going to save.
        
#     '''
#     # ensure output_dir is present
#     os.makedirs(output_dir, exist_ok=True)
    
#     image_path = os.path.join(output_dir, f'{stock_name}.png')
#     fig.write_file(image_path)
    