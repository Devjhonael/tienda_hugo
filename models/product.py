from db_config import db
from sqlalchemy import Column,Integer,String,Numeric,Text,DateTime
from sqlalchemy.sql.schema import ForeignKey
from datetime import datetime


class Product(db.Model):
    __tablename__ = 'productos'
    id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)

    name = Column('nombre', String(255), nullable=False)
    
    description = Column('descripcion', Text)
    
    price = Column('precio', Numeric(10, 2))
    
    stock = Column('stock', Integer)
    
    added_at = Column('fecha_agregado', DateTime, default=datetime.utcnow)
    
    category_id=Column('categoria_id',Integer,ForeignKey('categorias.id',ondelete='RESTRICT'),nullable=False)