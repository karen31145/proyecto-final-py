from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Alamacenes(Base):
    __tablename__ = "almacenes"
    id_almacen =  Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(20))
    ubicacion = Column(String(500))