from flask import request
from flask_restful import Resource
from db_config import db
from models.cart import Cart
from schemas.cart_schema import cart_schema,carts_schema
from marshmallow import ValidationError


class CartListResource(Resource):
    def get(self):
        try:
            carts = db.session.query(Cart).all()
            if carts is None:
                raise Exception('no hay cart')
            return {
                'content': carts_schema.dump(carts),
                'message': "Lista de cart"
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
            cart = cart_schema.load(request.json)
            print(cart)
            new_cart = Cart(user_id=cart.user_id)

            db.session.add(new_cart)
            db.session.commit()
            error = None
            return cart_schema.dump(new_cart), 201

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


class CartResource(Resource):
    def get(self, id):
        try:
            cart = db.session.query(
                Cart).filter_by(id=id).first()
            if cart is None:
                raise Exception('No se encontraron cart')

            error = None
            return cart_schema.dump(cart)

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
            cart = db.session.query(
                Cart).filter_by(id=id).first()

            if cart is None:
                raise Exception('no se encontro cart')

            #  Deserializa solo los campos presentes en el request
            cart_schema.load(request.json, partial=True)

            for key, value in request.json.items():
                setattr(cart, key, value)
            db.session.commit()

            error = None
            return {
                "content": cart_schema.dump(cart),
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
            cart = db.session.query(
                Cart).filter_by(id=id).first()

            print(cart)

            if cart is None:
                raise Exception('cart no encontrado')

            db.session.delete(cart)
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
