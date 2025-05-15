from db_config import db
from sqlalchemy import Column,Integer,String,DateTime,Numeric,Enum
from sqlalchemy.sql.schema import ForeignKey
from datetime import datetime
# from enum import Enum

# class EnumStatus(Enum):
#     pendiente='pendiente'    
#     enviado='enviado'
#     entregado='entregado'
#     cancelado='cancelado'

class Order(db.Model):
    __tablename__ = 'pedidos'
    id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)

    shipping_address = Column('direccion_envio', String(225))
    
    status = Column('estado', Enum('pendiente','enviado','entregado','cancelado'))
    
    total = Column('total', Numeric(10, 2))
    
    order_date = Column('fecha_pedido', DateTime, default=datetime.utcnow)
    
    user_id=Column('usuario_id',Integer,ForeignKey('usuarios.id',ondelete='RESTRICT'),nullable=False)