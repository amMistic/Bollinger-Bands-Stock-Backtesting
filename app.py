import os
import streamlit as st
from typing import List
from src.process import process


def main():
    st.title('Backtesting Trading Strategy Using Bollinger Bands')
    
    tickers = [
    "SELECT ALL","AAPL", "MSFT", "AMZN", "NVDA", "GOOGL", "META", "TSLA", "BRK.B", "JPM", "V",
    "JNJ", "PG", "UNH", "MA", "PFE", "XOM", "CVX", "KO", "PEP", "MRK",
    "DIS", "ADBE", "INTC", "CRM", "AVGO", "COST", "NFLX", "AMD", "PYPL", "QCOM",
    "T", "VZ", "TXN", "CSCO", "MMM", "HON", "ABBV", "BMY", "AMGN", "LLY",
    "TMO", "ISRG", "DHR", "LMT", "RTX", "BA", "SBUX", "MCD", "NKE", "LULU"
    ]

    # initialized session state and it components
    if "result" not in st.session_state:
        st.session_state["result"] = None
    if 'display' not in st.session_state:
        st.session_state['display'] = False

    with st.sidebar:
        
        # Select Ticker
        selection_box = st.multiselect(
            label='Select Stock(s)',
            options=tickers,
            default=['AAPL'])
        
        if 'SELECT ALL' in selection_box:
            selection_box = tickers[1:]
        
        # start_date input
        start_date = st.date_input('Select Start Date', format='DD/MM/YYYY')
        
        # End date Input
        end_date = st.date_input('Select End Date', format='DD/MM/YYYY')
        
        # Interval
        interval = st.slider(label='Select Interval(Days)', min_value=1, max_value=31)
        interval = f'{interval}d'

        submit = st.button('Submit')
        if submit:
            with st.spinner('Processing...'):
                st.session_state['result'] = process(selection_box, start_date, end_date, interval)
            st.session_state['display'] = True

    if st.session_state['display']:
        trades = st.session_state['result'][0]
        graphs = st.session_state['result'][1]
        
        if len(selection_box) > 2:
            select_figure = st.slider('Select Stock Index', 0, len(selection_box)-1)
            
            st.subheader('Trades:\n')
            st.dataframe(trades[select_figure])
            
            st.subheader('Visuals for each selected stocks:\n')
            st.plotly_chart(graphs[select_figure])
        else:
            st.subheader('Trades:\n')
            st.dataframe(trades[0])
            
            st.subheader('Visuals for each selected stocks:\n')
            st.plotly_chart(graphs[0])
            
    
        
if __name__ == '__main__':
    main()
    