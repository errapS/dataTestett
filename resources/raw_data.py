import pandas as pd
import requests
import time
from sqlalchemy import create_engine

def raw_model(endpoint: str):

    engine = create_engine('postgresql://user:assword@postgres_container:5432/swapipostgres')    

    response = requests.get(url=f"https://swapi.dev/api/{endpoint}/")
    data = response.json()

    if not data['next']:
        return pd.DataFrame(data['results']).to_sql('raw_' + endpoint, con=engine, if_exists='replace')

    results = data['results']
    while True:
        response = requests.get(data['next'])
        data = response.json()
        results.extend(data['results'])
        if not data['next']:
            break
        time.sleep(5)
    
    return pd.DataFrame(results).to_sql('raw_' + endpoint, con=engine, if_exists='replace')

