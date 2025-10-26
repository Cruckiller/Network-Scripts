import requests

# Your API key from CoinMarketCap
API_KEY = "YOUR_API_KEY"

# Base URL for the quotes endpoint
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

# Parameters for the request (we want Bitcoin, symbol = BTC)
parameters = {
    "symbol": "BTC",
    "convert": "USD"
}

# Headers (API key goes here)
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": API_KEY,
}

# Make the request
response = requests.get(url, headers=headers, params=parameters)

# Convert the response to JSON
data = response.json()

print(response.status_code)   # should be 200
print(data)                   # see the whole JSON

# Extract Bitcoin price
btc_price = data["data"]["BTC"]["quote"]["USD"]["price"]

print(f"Current Bitcoin Price: ${btc_price:,.2f}")