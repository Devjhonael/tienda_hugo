from flask import request
from flask_restful import Resource
from db_config import db
from models.sale import Sale

from schemas.sale_schema import sale_schema,sales_schema
from marshmallow import ValidationError


class SaleListResource(Resource):
    def get(self):
        try:
            sales = db.session.query(Sale).all()
            if sales is None:
                raise Exception('no hay sales')
            return {
                'content': sales_schema.dump(sales),
                'message': "Lista de sales"
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
            sale = sale_schema.load(request.json)
            print(sale)
            new_sale = sale(namstatuse=sale.status,
                            total=sale.total,
                            user_id=sale.user_id
                            )

            db.session.add(new_sale)
            db.session.commit()
            error = None
            return sale_schema.dump(new_sale), 201

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


class SaleResource(Resource):
    def get(self, id):
        try:
            sale = db.session.query(
                Sale).filter_by(id=id).first()
            if sale is None:
                raise Exception('No se encontraron sales')

            error = None
            return sale_schema.dump(sale)

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
            sale = db.session.query(
                Sale).filter_by(id=id).first()

            if sale is None:
                raise Exception('no se encontro sales')

            #  Deserializa solo los campos presentes en el request
            sale_schema.load(request.json, partial=True)

            for key, value in request.json.items():
                setattr(sale, key, value)
            db.session.commit()

            error = None
            return {
                "content": sale_schema.dump(sale),
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
            sale = db.session.query(
                Sale).filter_by(id=id).first()

            print(sale)

            if sale is None:
                raise Exception('sale no encontrado')

            db.session.delete(sale)
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
