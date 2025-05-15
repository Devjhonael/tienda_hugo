from db_config import db
from sqlalchemy import Column,Integer,String,DateTime,Text
from datetime import datetime

class User(db.Model):
    __tablename__ = 'usuarios'
    id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)

    name = Column('nombre', String(90), nullable=False)
    
    email = Column('email', String(90), nullable=False, unique=True)
    
    password = Column('password', Text, nullable=False)
    
    address = Column('direccion', String(255))
    
    phone = Column('telefono', String(20))
    
    registered_at = Column('fecha_registro', DateTime, default=datetime.utcnow)
