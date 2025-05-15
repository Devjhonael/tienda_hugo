from db_config import db
from sqlalchemy import Column,Integer,ForeignKey

class CartProduct(db.Model):
    __tablename__ = 'carritos_productos'

    id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)

    quantity = Column('cantidad', Integer)

    car_id=Column('carrito_id',Integer,ForeignKey('carritos.id',ondelete='RESTRICT'),nullable=False)

    product_id=Column('producto_id',Integer,ForeignKey('productos.id',ondelete='RESTRICT'),nullable=False)