import yfinance as yf
from datetime import datetime

def get_ytd_performance(ticker: str) -> float:
    stock = yf.Ticker(ticker)
    hist = stock.history(start=f"{datetime.now().year}-01-01")
    
    if hist.empty:
        raise ValueError(f"No data found for ticker '{ticker}'.")

    start_price = hist["Close"].iloc[0]
    end_price = hist["Close"].iloc[-1]

    return ((end_price - start_price) / start_price) * 100
