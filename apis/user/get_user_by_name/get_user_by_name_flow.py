from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from models.user import User
from utils.utils import json_message
import re


class GetUserByNameFlow:
    def __call__(self, request):

        user_name = request.args.get('user_name')
        user_name_regex = re.compile('.*{}.*'.format(user_name))

        users_list = User.objects(
            user_name= user_name_regex
        )

        if len(users_list) > 0:
            users_jsons_list = []
            users_jsons_list = list(map(lambda user_obj: user_obj.to_json(), users_list))

            return jsonify({"users": users_jsons_list})

        return json_message("No hay usuarios")
