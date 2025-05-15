from flask import request
from flask_restful import Resource
from db_config import db
from models.order import Order
from schemas.order_schema import order_schema,orders_schema
from marshmallow import ValidationError


class OrderListResource(Resource):
    def get(self):
        try:
            orders = db.session.query(Order).all()
            if orders is None:
                raise Exception('no hay orden')
            return {
                'content': orders_schema.dump(orders),
                'message': "Lista de orden"
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
            order = order_schema.load(request.json)
            print(order)
            new_order = Order(shipping_address=order.shipping_address,
                            status=order.status,
                            total=order.total,
                            user_id=order.user_id
                            )

            db.session.add(new_order)
            db.session.commit()
            error = None
            return order_schema.dump(new_order), 201

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


class OrderResource(Resource):
    def get(self, id):
        try:
            order = db.session.query(
                Order).filter_by(id=id).first()
            if order is None:
                raise Exception('No se encontraron ordenes')

            error = None
            return order_schema.dump(order)

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
            order = db.session.query(
                Order).filter_by(id=id).first()

            if order is None:
                raise Exception('no se encontro orden')

            #  Deserializa solo los campos presentes en el request
            order_schema.load(request.json, partial=True)

            for key, value in request.json.items():
                setattr(order, key, value)
            db.session.commit()

            error = None
            return {
                "content": order_schema.dump(order),
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
            order = db.session.query(
                Order).filter_by(id=id).first()

            print(order)

            if order is None:
                raise Exception('orden no encontrado')

            db.session.delete(order)
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
