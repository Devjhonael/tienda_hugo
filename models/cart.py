from db_config import db
from sqlalchemy import Column,Integer,DateTime,ForeignKey
from datetime import datetime


class Cart(db.Model):
    __tablename__ = 'carritos'
    id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)

    created_at = Column('fecha_creacion', DateTime, default=datetime.utcnow)
    
    user_id=Column('usuario_id',Integer,ForeignKey(column='usuarios.id',ondelete='RESTRICT'),nullable=False)