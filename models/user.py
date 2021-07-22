'''
user.py: Modulo para definir el modelo Usuario
'''
from mongoengine import Document, StringField, DateTimeField, BooleanField


class User(Document):
    '''
    Clase que define el modelo usuario
    '''
    user_name = StringField(required=True)
    user_email = StringField(required=True)
    user_password = StringField(required=True)
    user_verified = BooleanField(required=True)
    created_at = DateTimeField(required=True)
    updated_at = DateTimeField(required=True)

    def to_json(self):
        '''
        Metodo que devuelve los atributos de la clase en formato json
        '''
        user_dict = {
            'user_id': str(self.pk),
            "user_name": self.user_name,
            "user_email": self.user_email,
            "user_password": self.user_password,
            "user_verified": self.user_verified,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
        return user_dict