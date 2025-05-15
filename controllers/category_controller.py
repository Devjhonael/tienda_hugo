from flask import request
from flask_restful import Resource
from db_config import db
from models.category import Category
from schemas.category_schema import category_schema, categorys_schema
from marshmallow import ValidationError


class CategoryListResource(Resource):
    def get(self):
        try:
            categorys = db.session.query(Category).all()
            if categorys is None:
                raise Exception('no hay categoria')
            return {
                'content': categorys_schema.dump(categorys),
                'message': "Lista de categorias"
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
            category = category_schema.load(request.json)
            print(category)
            new_category = Category(
                name=category.name,
                description=category.description
            )

            db.session.add(new_category)
            db.session.commit()
            error = None
            return category_schema.dump(new_category), 201

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


class CategoryResource(Resource):
    def get(self, id):
        try:
            category = db.session.query(
                Category).filter_by(id=id).first()
            if category is None:
                raise Exception('No se encontraron categorias')

            error = None
            return category_schema.dump(category)

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
            category = db.session.query(
                Category).filter_by(id=id).first()

            if category is None:
                raise Exception('no se encontro categorias')

            #  Deserializa solo los campos presentes en el request
            category_schema.load(request.json, partial=True)

            for key, value in request.json.items():
                setattr(category, key, value)
            db.session.commit()

            error = None
            return {
                "content": category_schema.dump(category),
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
            category = db.session.query(
                Category).filter_by(id=id).first()

            print(category)

            if category is None:
                raise Exception('categoria no encontrado')

            db.session.delete(category)
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
