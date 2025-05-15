from flask import request
from flask_restful import Resource
from db_config import db
from models.product import Product
from schemas.product_schema import product_schema,products_schema
from marshmallow import ValidationError


class ProductListResource(Resource):
    def get(self):
        try:
            products = db.session.query(Product).all()
            if products is None:
                raise Exception('no hay productos')
            return {
                'content': products_schema.dump(products),
                'message': "Lista de usuarios"
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
            product = product_schema.load(request.json)
            print(product)
            new_product = Product(name=product.name,
                            description=product.description,
                            price=product.price,
                            stock=product.stock,
                            added_at=product.added_at,
                            category_id=product.category_id
                            )

            db.session.add(new_product)
            db.session.commit()
            error = None
            return product_schema.dump(new_product), 201

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


class ProductResource(Resource):
    def get(self, id):
        try:
            product = db.session.query(
                Product).filter_by(id=id).first()
            if product is None:
                raise Exception('No se encontraron productos')

            error = None
            return product_schema.dump(product)

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
            product = db.session.query(
                Product).filter_by(id=id).first()

            if product is None:
                raise Exception('no se encontro producto')

            #  Deserializa solo los campos presentes en el request
            product_schema.load(request.json, partial=True)

            for key, value in request.json.items():
                setattr(product, key, value)
            db.session.commit()

            error = None
            return {
                "content": product_schema.dump(product),
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
            product = db.session.query(
                Product).filter_by(id=id).first()

            print(product)

            if product is None:
                raise Exception('producto no encontrado')

            db.session.delete(product)
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
