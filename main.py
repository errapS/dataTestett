from database import *
from API_calls import *
import schedule
import datetime

def get_actors():
    print('Requesting actors...')

    actors = ActorsAPI().getAll()

    print('Request OK')
    print('Creating records for actors...')

    for person in actors:
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
    

def get_actors_bulk():
    print('Requesting actors...')

    actors = ActorsAPI().get()['results']

    print('Request OK')
    print('Creating records for actors...')
  
    CreateRecord().create_many(actors)

    print('Done')




if __name__ =="__main__":

    schedule.every().minute.do(get_actors_bulk)
    # schedule.every().day.at("00:00").do(get_actors_bulk)   #daily update

    while True:
        schedule.run_pending()


