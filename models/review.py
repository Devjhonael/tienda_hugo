from db_config import db
from sqlalchemy import Column,Integer,Text,DateTime
from sqlalchemy.sql.schema import ForeignKey
from datetime import datetime

class Review(db.Model):
    __tablename__ = 'resenias'

    id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    
    rating = Column('calificacion', Integer)
    
    comment = Column('comentario', Text)
    
    date = Column('fecha', DateTime, default=datetime.utcnow)

    user_id=Column('usuario_id',Integer,ForeignKey(column='usuarios.id',ondelete='RESTRICT'),nullable=False)

    product_id=Column('producto_id',Integer,ForeignKey('productos.id',ondelete='RESTRICT'),nullable=False)