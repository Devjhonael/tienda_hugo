from db_config import db
from sqlalchemy import Column,Integer,Numeric,ForeignKey

class SaleProduct(db.Model):
    __tablename__ = 'ventas_productos'

    id = Column('ventaproducto_id', Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    
    quantity = Column('cantidad', Integer)
    
    price = Column('precio', Numeric(10, 2))

    sale_id=Column('venta_id',Integer,ForeignKey('ventas.id',ondelete='RESTRICT'),nullable=False)

    product_id=Column('producto_id',Integer,ForeignKey('productos.id',ondelete='RESTRICT'),nullable=False)