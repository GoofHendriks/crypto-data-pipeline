from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Default settings for the DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 3, 7),  # Start from today
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    "crypto_scraper",
    default_args=default_args,
    description="Fetches crypto prices and stores them in PostgreSQL",
    schedule_interval="*/10 * * * *",  # Runs every 10 minutes
    catchup=False,
)

# Task: Run the Crypto Scraper Script
run_scraper = BashOperator(
    task_id="run_crypto_scraper",
    bash_command="python3 /opt/airflow/dags/fetch_crypto_prices.py",
    dag=dag,
)

run_scraper  # Task execution
 
