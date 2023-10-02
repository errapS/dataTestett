import requests

class PeopleAPI:
    def get(self):
        results = requests.get('https://swapi.dev/api/people')
        return results.json()


