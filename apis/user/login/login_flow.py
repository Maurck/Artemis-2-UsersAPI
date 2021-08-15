from flask import jsonify
from flask_jwt_extended import create_access_token
from utils.utils import json_message
from models.user import User


class LoginFlow:

    def __call__(self, request, bcrypt):

        user_email = request.form['user_email']
        user_password = request.form['user_password']

        user_obj = User.objects(
            user_email=user_email
        ).first()


        if user_obj is not None:
            # password verification
            if bcrypt.check_password_hash(user_obj.user_password, user_password):
                jwt_token_identity = {
                    'user_id': user_obj.to_json()["user_id"],
                    'user_name': user_obj.to_json()["user_name"]
                }
                access_token = create_access_token(identity=jwt_token_identity)
                return jsonify({
                    "token": access_token,
                    "user": user_obj.to_json()
                })

            return json_message("Contraseña incorrecta")

        return json_message("El usuario no está registrado")
