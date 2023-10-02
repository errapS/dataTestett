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

class People(BaseModel):
    person_id = AutoField()
    name = CharField(max_length=200)
    height = IntegerField()
    mass = IntegerField()
    hair_color = CharField(max_length=20)
    skin_color = CharField(max_length=20)
    eye_color = CharField(max_length=20)
    birth_year = CharField(max_length=20)
    gender = CharField(max_length=10)
    created_on = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIME")])

    class Meta:
        table_name = 'people'
