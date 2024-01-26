from src.get_data import get_stock_price

# stock_data = get_stock_price('AAPL')
# print(f'Apple stock price was {stock_data}')

def lambda_handler(event, context):
    # Fetching Apple stock data
    stock_data = get_stock_price('AAPL')
    print(stock_data)
    return {
        'statusCode': 200,
        'body': stock_data
    }
    
