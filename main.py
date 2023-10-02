from database import *
from API_calls import *

if __name__ =="__main__":

    print('Requesting peoples...')

    people = PeopleAPI().get()['results']

    print('Request OK')
    print('Creating records for peoples....') 
    for person in people:
        CreateRecord().create_person(
            name = person['name'],
            height = person['height'],
            mass = person['mass'],
            hair_color = person['hair_color'],
            skin_color = person['skin_color'],
            eye_color = person['eye_color'],
            birth_year = person['birth_year'],
            gender = person['gender']
        )

    print('Done')