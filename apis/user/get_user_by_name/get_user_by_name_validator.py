from utils.utils import validate_parameters

get_user_query_schema = {
    'user_name': {
        'nullable': False,
        'required': True
    }
}

class GetUserByNameValidator:
    
    def __call__(self, request):
        query_validation_errors = validate_parameters(request.args, get_user_query_schema)
        return query_validation_errors