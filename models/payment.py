from db_config import db
from sqlalchemy import Column,Integer,Numeric,String,DateTime
from sqlalchemy.sql.schema import ForeignKey
from datetime import datetime

class Payment(db.Model):
    __tablename__ = 'pagos'
    id = Column('pago_id', Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)

    amount = Column('monto', Numeric(10, 2))
    
    method = Column('metodo_pago', String(50))
    
    status = Column('estado_pago', String(50))
    
    payment_date = Column('fecha_pago', DateTime, default=datetime.utcnow)
    
    order_id=Column('pedido_id',Integer,ForeignKey(column='pedidos.id',ondelete='RESTRICT'),nullable=False)

