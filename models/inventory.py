from db_config import db
from sqlalchemy import Column,Integer,DateTime,Enum ,ForeignKey
from datetime import datetime

# import enum

# class EnumType(enum.Enum):
#     ENTRADA="ENTRADA"
#     SALIDA="SALIDA"

class Inventory(db.Model):
    __tablename__ = 'inventarios'
    
    id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    
    quantity = Column('cantidad', Integer)
    
    movement_type = Column('tipo_movimiento', Enum('entrada','salida'))
    
    movement_date = Column('fecha_movimiento', DateTime, default=datetime.utcnow)
    
    product_id=Column('producto_id',Integer,ForeignKey('productos.id',ondelete="RESTRICT"),nullable=False)