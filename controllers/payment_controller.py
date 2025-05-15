from flask import request
from flask_restful import Resource
from db_config import db
from models.payment import Payment
from schemas.payment_schema import payment_schema,payments_schema
from marshmallow import ValidationError


class PaymentListResource(Resource):
    def get(self):
        try:
            payments = db.session.query(Payment).all()
            if payments is None:
                raise Exception('no hay payments')
            return {
                'content': payments_schema.dump(payments),
                'message': "Lista de payments"
            }, 200
        except Exception as err:
            return {
                "content": err.args[0],
                "message": "Error Inesperado"
            }
        finally:
            db.session.close()

    def post(self):
        try:
            payment = payment_schema.load(request.json)
            print(payment)
            new_payment = Payment(amount=payment.amount,
                            method=payment.method,
                            status=payment.status,
                            order_id=payment.order_id,
                            )

            db.session.add(new_payment)
            db.session.commit()
            error = None
            return payment_schema.dump(new_payment), 201

        except ValidationError as err:
            error = err
            return {
                'message': 'Error de validación',
                'errores': error.messages
            }, 500
        except Exception as err:
            error = err

            return {
                "message": "error Desconocido"
            }, 500
        finally:
            if error is not None:
                db.session.rollback()
            db.session.close()


class PaymentResource(Resource):
    def get(self, id):
        try:
            payment = db.session.query(
                Payment).filter_by(id=id).first()
            if payment is None:
                raise Exception('No se encontraron payment')

            error = None
            return payment_schema.dump(payment)

        except Exception as err:
            error = err
            return {
                "message": error.args[0]
            }, 404
        finally:
            if error is not None:
                db.session.rollback()
            db.session.close()

    def put(self, id):
        try:
            payment = db.session.query(
                Payment).filter_by(id=id).first()

            if payment is None:
                raise Exception('no se encontro payment')

            #  Deserializa solo los campos presentes en el request
            payment_schema.load(request.json, partial=True)

            for key, value in request.json.items():
                setattr(payment, key, value)
            db.session.commit()

            error = None
            return {
                "content": payment_schema.dump(payment),
                "message": "datos actualizado correctamente"
            }, 201

        except ValidationError as err:
            error = err
            return {
                'message': 'Error de validación',
                'errores': error.messages
            }, 500
        except Exception as err:
            error = err

            return {
                "message": "error Desconocido"
            }, 500
        finally:
            if error is not None:
                db.session.rollback()
            db.session.close()

    def delete(self, id):
        try:
            payment = db.session.query(
                Payment).filter_by(id=id).first()

            print(payment)

            if payment is None:
                raise Exception('payment no encontrado')

            db.session.delete(payment)
            db.session.commit()
            error = None
            return {
                "content": "",
                "message": ""
            }, 204
        except Exception as err:
            error = err
            return {
                "message": error.args[0]
            }, 404
        finally:
            db.session.close()
