from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class CategoriaModelo(Base):
    __tablename__ = "categorias"
    id_categoria =  Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(20))
    descripcion = Column(String(500))