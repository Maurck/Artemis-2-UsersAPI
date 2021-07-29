from flask_jwt_extended import get_jwt_identity
import cloudinary
import cloudinary.uploader
from models.user import User
from utils.utils import json_message


class UpdateUserFlow:
    def __call__(self, request, bcrypt):

        user_obj = User.objects(
            id=get_jwt_identity()
        ).first()

        if "user_image" in request.files:
            upload_result = cloudinary.uploader.upload(request.files["user_image"])
            user_obj.user_img_url = upload_result["url"]

        if "user_description" in request.form:
            user_obj.user_description = request.form["user_description"]

        if 'user_name' in request.form:
            user_obj.user_name = request.form['user_name']

        if 'user_password' in request.form:
            user_obj.user_password = bcrypt.generate_password_hash(request.form['user_password']).decode('utf-8')
        
        if 'user_email' in request.form:
            user_obj.user_email = request.form['user_email']

        user_obj.save()

        return json_message("Usuario actualizado")

