from models import People

class CreateRecord:
    def create_person(self, **kwargs):
        People.create(
            name = kwargs['name'],
            height = kwargs['height'],
            mass = kwargs['mass'],
            hair_color = kwargs['hair_color'],
            skin_color = kwargs['skin_color'],
            eye_color = kwargs['eye_color'],
            birth_year = kwargs['birth_year'],
            gender = kwargs['gender']
        )