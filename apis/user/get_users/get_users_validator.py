from utils.utils import validate_parameters

get_users_query_schema = {
    "from": {
        "type": "integer",
        'coerce': int,
        "min": 0,
        "max": 255,
        "required": False,
        "default": 0
    },
    "limit": {
        "type": "integer",
        'coerce': int,
        "min": 0,
        "max": 255,
        "required": False,
        "default": 0
    } 
}

class GetUsersValidation:

    def __call__(self, request):
        
        query_validation_errors = validate_parameters(request.args.copy(), get_users_query_schema)
        return query_validation_errors

