from .get_user_by_name_validator import GetUserByNameValidator
from .get_user_by_name_flow import GetUserByNameFlow


class GetUserByName:

    def __call__(self, request):

        get_user_by_name_validation = GetUserByNameValidator()
        get_user_by_name_validation_errors = get_user_by_name_validation(request)
        if get_user_by_name_validation_errors:
            return get_user_by_name_validation_errors

        get_user_by_name_flow = GetUserByNameFlow()
        return get_user_by_name_flow(request)

            
