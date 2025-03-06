import requests
import pandas as pd
from datetime import datetime

def fetch_crypto_data():
    """
    Fetch real-time cryptocurrency prices from the CoinGecko API.
    """
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,solana",
        "vs_currencies": "usd",
        "include_market_cap": "true",
        "include_24hr_vol": "true",
        "include_24hr_change": "true"
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    records = []
    for coin, values in data.items():
        records.append({
            "symbol": coin.upper(),
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "price": values["usd"],
            "market_cap": values.get("usd_market_cap", None),
            "24h_vol": values.get("usd_24h_vol", None),
            "24h_change": values.get("usd_24h_change", None)
        })
    
    return pd.DataFrame(records)

def save_to_csv(df, filename):
    """
    Save processed crypto data to a CSV file.
    """
    df.to_csv(filename, index=False)
    print(f"Crypto data saved to {filename}")

def main():
    """
    Fetch and process crypto price data.
    """
    print("Fetching cryptocurrency prices...")
    df = fetch_crypto_data()
    save_to_csv(df, "../data/crypto_prices.csv")  # Save in the data folder

if __name__ == "__main__":
    main()
 
