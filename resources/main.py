import requests
from raw_data import raw_model
import schedule
import time

DBT_API_ENDPOINT = "http://dbt_container:5000/run-dbt"

def load_raw_and_run_dbt():

    response = requests.get("https://swapi.dev/api/")
    endpoints = [k for k in response.json().keys()]

    for e in endpoints:
        raw_model(e)
        time.sleep(1)
    
    response = requests.post(DBT_API_ENDPOINT)
    if response.status_code == 200:
        print("dbt run successfully triggered")
    else:
        print("Failed to trigger dbt run")

if __name__ == '__main__':
    load_raw_and_run_dbt()

    while True:
        schedule.every(1).day.do(load_raw_and_run_dbt)
