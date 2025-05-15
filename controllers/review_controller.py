from flask import request
from flask_restful import Resource
from db_config import db
from models.review import Review
from schemas.review_schema import review_schema, reviews_schema
from marshmallow import ValidationError


class ReviewListResource(Resource):
    def get(self):
        try:
            reviews = db.session.query(Review).all()
            if reviews is None:
                raise Exception('no hay review')
            return {
                'content': reviews_schema.dump(reviews),
                'message': "Lista de review"
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
            review = review_schema.load(request.json)
            print(review)
            new_review = Review(rating=review.rating,
                            comment=review.comment,
                            user_id=review.user_id,
                            product_id=review.product_id
                            )

            db.session.add(new_review)
            db.session.commit()
            error = None
            return review_schema.dump(new_review), 201

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


class ReviewResource(Resource):
    def get(self, id):
        try:
            review = db.session.query(
                Review).filter_by(id=id).first()
            if review is None:
                raise Exception('No se encontraron review')

            error = None
            return review_schema.dump(review)

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
            review = db.session.query(
                Review).filter_by(id=id).first()

            if review is None:
                raise Exception('no se encontro review')

            #  Deserializa solo los campos presentes en el request
            review_schema.load(request.json, partial=True)

            for key, value in request.json.items():
                setattr(review, key, value)
            db.session.commit()

            error = None
            return {
                "content": review_schema.dump(review),
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
            review = db.session.query(
                Review).filter_by(id=id).first()

            print(review)

            if review is None:
                raise Exception('review no encontrado')

            db.session.delete(review)
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
