from db_config import db
from sqlalchemy import Column,Integer,ForeignKey,Enum,DateTime,Numeric
from datetime import datetime
import enum

class EnumStatus(enum.Enum):
    completado="completado"
    anulado="anulado"


class Sale(db.Model):
    __tablename__ = 'ventas'
    id = Column('id',Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)

    sale_date = Column('fecha_venta',DateTime, default=datetime.utcnow)
    
    status = Column('estado_venta',Enum(EnumStatus))

    total = Column('total',Numeric(10, 2))
    
    user_id=Column('usuario_id',Integer,ForeignKey('usuarios.id',ondelete='RESTRICT'),nullable=False)