import requests
import config

# Your Alpha Vantage API key
api_key = config.api_key

'''
# Function to make an API call to Alpha Vantage
def alpha_vantage_api_call(function, symbol):
    base_url = 'https://www.alphavantage.co/query'
    params = {
        'function': function,
        'symbol': symbol,
        'apikey': api_key
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"API call failed with status code: {response.status_code}")
        return None

# Example usage
function = 'GLOBAL_QUOTE'  # Replace with the desired Alpha Vantage function
symbol = 'AAPL'  # Replace with the desired stock symbol

data = alpha_vantage_api_call(function, symbol)

# Process and print the data
if data is not None:
    # Check for error message in the response
    if 'Error Message' in data:
        print(f"API error: {data['Error Message']}")
    else:
        # Extract and print relevant information from the response
        # Modify this section based on your specific requirements
        global_quote = data['Global Quote']
        
        print("Global Quote:")
        print(f"Symbol: {global_quote['01. symbol']}")
        print(f"Open: {global_quote['02. open']}")
        print(f"High: {global_quote['03. high']}")
        print(f"Low: {global_quote['04. low']}")
        print(f"Price: {global_quote['05. price']}")
        print(f"Volume: {global_quote['06. volume']}")
        print(f"Latest trading day: {global_quote['07. latest trading day']}")
        print(f"Previous close: {global_quote['08. previous close']}")
        print(f"Change: {global_quote['09. change']}")
        print(f"Change percent: {global_quote['10. change percent']}")


'''


# Function to make an API call to Alpha Vantage
def alpha_vantage_api_call(function, symbol):
    base_url = 'https://www.alphavantage.co/query'
    params = {
        'function': function,
        'symbol': symbol,
        'apikey': api_key
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"API call failed with status code: {response.status_code}")
        return None

# Example usage
function = 'TIME_SERIES_DAILY'  # Replace with the desired Alpha Vantage function
symbol = 'AAPL'  # Replace with the desired stock symbol

data = alpha_vantage_api_call(function, symbol)

# Process and print the data
if data is not None:
    # Check for error message in the response
    if 'Error Message' in data:
        print(f"API error: {data['Error Message']}")
    else:
        # Extract and print historical stock data
        time_series = data['Time Series (Daily)']
        
        print("Date\t\t\tOpen\t\tHigh\t\tLow\t\tClose\t\tVolume")
        for date, details in time_series.items():
            open_price = details['1. open']
            high_price = details['2. high']
            low_price = details['3. low']
            close_price = details['4. close']
            volume = details['5. volume']
            
            print(f"{date}\t{open_price}\t{high_price}\t{low_price}\t{close_price}\t{volume}")
