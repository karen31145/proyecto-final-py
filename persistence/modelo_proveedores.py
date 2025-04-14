from sqlalchemy import Column
from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ProveedoresModel(Base):
    __tablename__ = "proveedores"
    
    id_proveedor = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    contacto = Column(String(100), nullable=False)
    telefono = Column(String(15), nullable=False)
    email = Column(String(50), nullable=False)
    direccion = Column(String(10), nullable=False)  # Cambiado a String para almacenar la fecha como texto
    indicador_habilitado = Column(Integer, nullable=False)  # Cambiado a String para almacenar el estado como 
    