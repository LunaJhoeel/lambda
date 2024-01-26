import yfinance as yf

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


def get_stock_price(ticker_symbol):
    try:
        ticker = yf.Ticker(ticker_symbol)
        # Fetch latest closing price
        todays_data = ticker.history(period='1d')
        return todays_data['Close'].iloc[0]
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

