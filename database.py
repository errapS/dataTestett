from models import Actors
import datetime

class CreateRecord:
    def create_person(self, **kwargs):
        for field in ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender']:
            if kwargs.get(field) == 'unknown':
                kwargs[field] = None


        Actors.create(
            name = kwargs['name'],
            height = kwargs['height'],
            mass = kwargs['mass'],
            hair_color = kwargs['hair_color'],
            skin_color = kwargs['skin_color'],
            eye_color = kwargs['eye_color'],
            birth_year = kwargs['birth_year'],
            gender = kwargs['gender']
        )

        
    def create_many(self, data):
        Actors.insert_many(data, fields=[Actors.name,
                                         Actors.height,
                                         Actors.mass,
                                         Actors.hair_color,
                                         Actors.skin_color,
                                         Actors.eye_color,
                                         Actors.birth_year,
                                         Actors.gender]).execute()
        
        Actors().save()

# class UpdateRecord:
#     def update_person(self):
#         current_date = datetime.datetime.now().strftime("%Y_%m_%d")
#         partition_name = f"people_{current_date}"
#         Actors.update
#         try:
#         with db.atomic():
#             db.execute_sql(f"""
#                 CREATE TABLE IF NOT EXISTS {partition_name}
#                 PARTITION OF people
#                 FOR VALUES FROM ('{current_date} 00:00:00') TO ('{current_date} 23:59:59')
#             """)
#     except OperationalError as e:
#         print(f"Error creating partition: {str(e)}")

