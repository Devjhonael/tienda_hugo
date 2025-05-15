from db_config import db
from sqlalchemy import Column,Integer,Text,String

class Category(db.Model):
    __tablename__ = 'categorias'
    id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    
    name = Column('nombre', String(45), nullable=False)
    
    description = Column('descripcion', Text)