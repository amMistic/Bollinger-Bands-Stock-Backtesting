import pandas as pd

class BackTest:
    def __init__(self):
        pass
    
    def run(self, data : pd.DataFrame):
        if data is None:
            raise 'No data is provided!!'
        
        trades = []
        holding = False
        buying_price = 0
        
        for index, row in data.iterrows():
            if row['Buy'] and not holding:
                holding = True
                buying_price = row['Close']
                trades.append({
                    'token' : row.name,
                    'date_in' : row['Date'],
                    'buy_price' : buying_price
                })
            
            elif row['Sell'] and holding:
                holding = False
                sell_price = row['Close']
                trade = trades[-1]
                trade.update({
                    'data_out' : row['Date'],
                    'sell_price' : sell_price,
                    'profit_percentage' : ((sell_price - buying_price)/ buying_price) * 100
                })
        
        # print('Trades:\n',trades)
        return trades