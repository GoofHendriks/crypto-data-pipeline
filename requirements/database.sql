CREATE TABLE crypto_prices (
    id SERIAL PRIMARY KEY,
    symbol TEXT NOT NULL,
    date TIMESTAMP NOT NULL,
    price NUMERIC NOT NULL,
    market_cap NUMERIC,
    volume_24h NUMERIC,
    change_24h NUMERIC
);
 
