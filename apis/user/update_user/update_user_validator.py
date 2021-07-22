from utils.utils import validate_parameters

update_user_body_schema = {
    'user_name': {
        'nullable': False,
        'required': False
    },
    'user_password': {
        'nullable': False,
        'required': False
    },
    'user_email': {
        'nullable': False,
        'required': False
    },    
}

class UpdateUserValidator:

    def __call__(self, request):
        body_validation_errors = validate_parameters(request.json, update_user_body_schema)
        return body_validation_errors