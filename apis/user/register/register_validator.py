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
        'required': True
    },    
}

class RegisterValidator:
    '''
    Clase que inicia sesión
    '''
    def __call__(self, request):
        body_validation_errors = validate_parameters(request.json, register_body_schema)
        return body_validation_errors