from .update_user_validator import UpdateUserValidator
from .update_user_flow import UpdateUserFlow


class UpdateUser:

    def __call__(self, request, bcrypt):

        update_user_validation = UpdateUserValidator()
        update_user_validation_errors = update_user_validation(request)
        if update_user_validation_errors:
            return update_user_validation_errors

        update_user_flow = UpdateUserFlow()
        return update_user_flow(request, bcrypt)

            
