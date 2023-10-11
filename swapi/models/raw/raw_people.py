import pandas as pd
import requests
import time

def model(dbt, fal):

    response = requests.get("https://swapi.dev/api/people/")
    data = response.json()
    if not data['next']:
        return pd.DataFrame(data['results'])

    results = data['results']
    while True:
        response = requests.get(data['next'])
        data = response.json()
        results.extend(data['results'])
        if not data['next']:
            break
        time.sleep(.5)
    
    return pd.DataFrame(results)
