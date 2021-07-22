from .get_users_validator import GetUsersValidation
from .get_users_flow import GetUsersFlow


class GetUsers:

    def __call__(self, request):

        get_users_validation = GetUsersValidation()
        get_users_validation_errors = get_users_validation(request)
        if get_users_validation_errors:
            return get_users_validation_errors

        get_users_flow = GetUsersFlow()
        return get_users_flow(request)

            
