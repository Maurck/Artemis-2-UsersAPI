from flask import jsonify
from models.user import User
from utils.utils import json_message


class GetUsersFlow:

    def __call__(self, request):

            from_index = request.args.get('from', type=int, default=0)
            limit_index = request.args.get('limit', type=int, default=0)

            users_list = User.objects().limit(limit_index).skip(from_index)

            print(users_list)

            if len(users_list) > 0:
                users_jsons_list = []
                users_jsons_list = list(map(lambda user_obj: user_obj.to_json(), users_list))

                return jsonify({"users": users_jsons_list})

            return json_message("No hay usuarios")
