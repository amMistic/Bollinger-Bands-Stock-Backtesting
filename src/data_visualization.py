import pandas as pd
import plotly.graph_objects as go


# Function to generate stock graph as HTML
def generate_graph_html(data, stock_name):
    fig = go.Figure()

    # Close Price
    fig.add_trace(go.Scatter(
        x=data.index, y=data['Close'], name='Close Price', line=dict(color='blue')
    ))
    # Bollinger Bands
    fig.add_trace(go.Scatter(
        x=data.index, y=data['Upper_Band'], name='Upper Band', line=dict(color='red', dash='dash')
    ))
    fig.add_trace(go.Scatter(
        x=data.index, y=data['Lower_Band'], name='Lower Band', line=dict(color='green', dash='dash')
    ))
    # SMA
    fig.add_trace(go.Scatter(
        x=data.index, y=data['SMA'], name='SMA', line=dict(color='orange')
    ))

    # Signals
    fig.add_trace(go.Scatter(
        x=data[data['Buy']].index, y=data[data['Buy']]['Close'], mode='markers', name='Buy',
        marker=dict(color='green', size=10, symbol='triangle-up')
    ))
    fig.add_trace(go.Scatter(
        x=data[data['Sell']].index, y=data[data['Sell']]['Close'], mode='markers', name='Sell',
        marker=dict(color='red', size=10, symbol='triangle-down')
    ))

    fig.update_layout(title=f"{stock_name} - Bollinger Bands", xaxis_title="Days", yaxis_title="Price")
    return fig

