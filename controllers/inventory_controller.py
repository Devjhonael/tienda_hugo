from flask import request
from flask_restful import Resource
from db_config import db
from models.inventory import Inventory
from schemas.inventory_schema import inventory_schema,inventorys_schema
from marshmallow import ValidationError


class InventoryListResource(Resource):
    def get(self):
        try:
            inventorys = db.session.query(Inventory).all()
            if inventorys is None:
                raise Exception('no hay inventario')
            return {
                'content': inventorys_schema.dump(inventorys),
                'message': "Lista de inventario"
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
            inventory = inventory_schema.load(request.json)
            print(inventory)
            new_inventory = Inventory(quantity=inventory.quantity,
                            movement_type=inventory.movement_type,
                            product_id=inventory.product_id
                            )

            db.session.add(new_inventory)
            db.session.commit()
            error = None
            return inventory_schema.dump(new_inventory), 201

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


class InventorytResource(Resource):
    def get(self, id):
        try:
            inventory = db.session.query(
                Inventory).filter_by(id=id).first()
            if inventory is None:
                raise Exception('No se encontraron inventario')

            error = None
            return inventory_schema.dump(inventory)

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
            inventory = db.session.query(
                Inventory).filter_by(id=id).first()

            if inventory is None:
                raise Exception('no se encontro inventario')

            #  Deserializa solo los campos presentes en el request
            inventory_schema.load(request.json, partial=True)

            for key, value in request.json.items():
                setattr(inventory, key, value)
            db.session.commit()

            error = None
            return {
                "content": inventory_schema.dump(inventory),
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
            inventory = db.session.query(
                Inventory).filter_by(id=id).first()

            print(inventory)

            if inventory is None:
                raise Exception('inventario no encontrado')

            db.session.delete(inventory)
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
