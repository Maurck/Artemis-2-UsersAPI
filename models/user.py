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
    user_description = StringField(required=False, default="")
    user_img_url = StringField(required=False, default="")
    user_img_public_id = StringField(required=False, default="")
    user_verified = BooleanField(required=True)
    user_created_at = DateTimeField(required=True)
    user_updated_at = DateTimeField(required=True)

    def to_json(self):
        '''
        Metodo que devuelve los atributos de la clase en formato json
        '''
        user_dict = {
            'user_id': str(self.pk),
            "user_name": self.user_name,
            "user_email": self.user_email,
            "user_password": self.user_password,
            "user_description": self.user_description,
            "user_img_url": self.user_img_url,
            "user_img_public_id": self.user_img_public_id,
            "user_verified": self.user_verified,
            "user_created_at": self.user_created_at,
            "user_updated_at": self.user_updated_at
        }
        return user_dict