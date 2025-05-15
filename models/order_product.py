from db_config import db
from sqlalchemy import Column,Integer,Numeric,ForeignKey

class OrderProduct(db.Model):
    __tablename__ = 'pedidos_productos'
    
    id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    
    quantity = Column('cantidad', Integer)
    
    price = Column('precio', Numeric(10, 2))
    
    order_id=Column('pedido_id',Integer,ForeignKey('pedidos.id',ondelete='RESTRICT'),nullable=False)

    product_id=Column('producto_id',Integer,ForeignKey('productos.id',ondelete="RESTRICT"),nullable=False)
