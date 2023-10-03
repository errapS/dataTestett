import requests

class ActorsAPI:
    ''' The people function only returns ten persons from the movies '''
    def get(self):
        results = requests.get('https://swapi.dev/api/people')
        return results.json()

    ''' This is slow, but it returns all the actors from the API '''
    def getAll(self):
        all_people = []
        i = 1
        err_count = 0
        while err_count < 5:
            print("log-count: ", i)
            url = f'https://swapi.dev/api/people/{i}'
            results = requests.get(url)
            i += 1
            
            if results.status_code == 200:
                person_data = results.json()
                all_people.append(person_data)
            else:
                err_count += 1
                print("ERROR: ", results.status_code)

        return all_people
        
        
    
