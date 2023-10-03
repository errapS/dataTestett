from peewee import *
import config

database = PostgresqlDatabase(
    host=config.DATABASES['HOST'],
    port=config.DATABASES['PORT'],
    database=config.DATABASES['NAME'],
    user=config.DATABASES['USER'],
    password=config.DATABASES['PASSWORD']
    )

class BaseModel(Model):
    class Meta:
        database = database

class Actors(BaseModel):
    person_id = AutoField()
    name = CharField(max_length=200)
    height = IntegerField()
    mass = DecimalField()
    hair_color = CharField(max_length=50)
    skin_color = CharField(max_length=50)
    eye_color = CharField(max_length=50)
    birth_year = CharField(max_length=50)
    gender = CharField(max_length=20)
    created_on = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIME")])

    class Meta:
        table_name = 'people'
        
