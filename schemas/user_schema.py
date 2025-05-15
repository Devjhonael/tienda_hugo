from marshmallow_config import ma
from models.user import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        # exclude = ["id"]

user_schema=UserSchema()
users_schema=UserSchema(many=True)