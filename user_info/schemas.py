from user_info.models import User, Email, PhoneNumber
from user_info import ma

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

class EmailSchema(ma.ModelSchema):
    class Meta:
        model = Email

class PhoneNumberSchema(ma.ModelSchema):
    class Meta:
        model = PhoneNumber