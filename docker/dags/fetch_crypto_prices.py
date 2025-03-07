import requests
import psycopg2
from datetime import datetime

DB_NAME = "airflow"  
DB_USER = "airflow"  
DB_PASSWORD = "airflow"  
DB_HOST = "postgres"
DB_PORT = "5432"


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
            "volume_24h": values.get("usd_24h_vol", None),
            "change_24h": values.get("usd_24h_change", None)
        })
    
    return records

def store_in_postgres(records):
    """
    Store crypto data in PostgreSQL database.
    """
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        )
        cur = conn.cursor()

        for record in records:
            cur.execute("""
                INSERT INTO crypto_prices (symbol, date, price, market_cap, volume_24h, change_24h)
                VALUES (%s, %s, %s, %s, %s, %s);
            """, (record["symbol"], record["date"], record["price"], record["market_cap"], record["volume_24h"], record["change_24h"]))

        conn.commit()
        cur.close()
        conn.close()
        print("✅ Data successfully stored in PostgreSQL.")

    except Exception as e:
        print(f"⚠️ Error storing data in PostgreSQL: {e}")

def main():
    """
    Fetch and store crypto price data in PostgreSQL.
    """
    print("Fetching cryptocurrency prices...")
    records = fetch_crypto_data()
    store_in_postgres(records)

if __name__ == "__main__":
    main()
