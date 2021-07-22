from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from models.user import User
from utils.utils import json_message


class UpdateUserFlow:
    def __call__(self, request, bcrypt):

        user_obj = User.objects(
            id=get_jwt_identity()
        ).first()

        if 'user_name' in request.json:
            user_obj.user_name = request.json['user_name']

        if 'user_password' in request.json:
            user_obj.user_password = bcrypt.generate_password_hash(request.json['user_password']).decode('utf-8')
        
        if 'user_email' in request.json:
            user_obj.user_email = request.json['user_email']

        user_obj.save()

        return json_message("Usuario actualizado")

