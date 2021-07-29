'''
register.py: Modulo para el registro
'''
from datetime import datetime
from utils.utils import json_message
from models.user import User


class RegisterFlow:
    '''
    Clase que registra a un usuario
    '''
    def __call__(self, request, bcrypt):

        req_user_email = request.form['user_email']

        user_obj = User.objects(
            user_email=req_user_email
        ).first()

        if user_obj is None:
            new_user = User(
                user_name=request.form['user_name'],
                user_password=bcrypt.generate_password_hash(request.form['user_password']).decode('utf-8'),
                user_email=req_user_email,
                user_verified=True,
                user_created_at=datetime.now(),
                user_updated_at=datetime.now()
            )

            new_user.save()
            return json_message("Usuario registrado")

        return json_message("Usuario ya registrado")
