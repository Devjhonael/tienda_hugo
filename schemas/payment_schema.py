from marshmallow_config import ma
from models.payment import Payment

class PaymentSchema(ma.SQLAlchemySchema):
    class Meta:
        model=Payment
        load_instance=True

payment_schema=PaymentSchema()
payments_schema=PaymentSchema(many=True)
