# Crypto Data Pipeline with Airflow & PostgreSQL

## Overview
This project automates the collection and storage of cryptocurrency price data using Apache Airflow and PostgreSQL. 
It fetches real-time prices from the CoinGecko API, stores the data in a PostgreSQL database, and schedules automated data collection using Airflow.

## Features
- Fetches real-time cryptocurrency prices (Bitcoin, Ethereum, Solana) using the CoinGecko API
- Stores the data in a PostgreSQL database
- Uses Apache Airflow to schedule and monitor data ingestion
- Runs in a Dockerized environment for easy deployment

## Technologies Used
- Python
- Apache Airflow
- PostgreSQL
- Docker
- CoinGecko API

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/GoofHendriks/crypto-data-pipeline.git
cd crypto-data-pipeline
```

### 2. Start Docker Containers

```sh
cd docker 
docker-compose up -d
```

### 3. Run the Scraper Manually (For Testing)

```sh
docker exec -it airflow-webserver python3 /opt/airflow/dags/fetch_crypto_prices.py
```

### 4. Check Data in PostgreSQL

```sh
docker exec -it postgres psql -U airflow -d airflow -c "SELECT * FROM crypto_prices LIMIT 10;"
```

### 5. Access the Airflow UI
- Open **http://localhost:8080**
- Login Credentials:
  - **Username:** `admin`
  - **Password:** `admin`
- Enable the `crypto_scraper` DAG to run automatically.

## DAG Automation Status
The DAG **`crypto_scraper`** is set to run **every 10 minutes (`*/10 * * * *`)**.

## Project Structure
```sh
crypto-data-pipeline/
│── docker/
│   ├── dags/                # Airflow DAGs (data ingestion scripts)
│   │   ├── crypto_scraper_dag.py
│   │   ├── fetch_crypto_prices.py
│   ├── docker-compose.yml    # Docker configuration for PostgreSQL & Airflow
│── data/                     # Raw or processed data (if applicable)
│── database/                 # Database setup scripts
│── README.md                 # Project documentation
```
