from flask import request
from flask_restful import Resource
from db_config import db
from models.user import User
from schemas.user_schema import user_schema, users_schema
from marshmallow import ValidationError


class UserListResource(Resource):
    def get(self):
        try:
            users = db.session.query(User).all()
            if users is None:
                raise Exception('no hay usuarios')
            return {
                'content': users_schema.dump(users),
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
            user = user_schema.load(request.json)
            print(user)
            new_user = User(name=user.name,
                            email=user.email,
                            password=user.password,
                            address=user.address,
                            phone=user.phone
                            )

            db.session.add(new_user)
            db.session.commit()
            error = None
            return user_schema.dump(new_user), 201

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


class UserResource(Resource):
    def get(self, id):
        try:
            user = db.session.query(
                User).filter_by(id=id).first()
            if user is None:
                raise Exception('No se encontraron usuarios')

            error = None
            return user_schema.dump(user)

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
            user = db.session.query(
                User).filter_by(id=id).first()

            if user is None:
                raise Exception('no se encontro usuarios')

            #  Deserializa solo los campos presentes en el request
            user_schema.load(request.json, partial=True)

            for key, value in request.json.items():
                setattr(user, key, value)
            db.session.commit()

            error = None
            return {
                "content": user_schema.dump(user),
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
            user = db.session.query(
                User).filter_by(id=id).first()

            print(user)

            if user is None:
                raise Exception('usuario no encontrado')

            db.session.delete(user)
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
