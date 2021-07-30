from utils.utils import validate_parameters

register_body_schema = {
    'user_name': {
        'nullable': False,
        'required': True
    },
    'user_password': {
        'nullable': False,
        'required': True
    },
    'user_email': {
        'nullable': False,
        'required': True,
        'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    },    
}

class RegisterValidator:

    def __call__(self, request):
        body_validation_errors = validate_parameters(request.form, register_body_schema)
        return body_validation_errors