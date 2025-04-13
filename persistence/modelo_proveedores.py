from sqlalchemy import column
from sqlalchemy import String, integer, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ProveedoresModel(Base):
    __tablename__ = "proveedores"
    
    id_proveedor = column(integer, primary_key=True, autoincrement=True)
    nombre = column(String(50), nullable=False)
    contacto = column(String(100), nullable=False)
    telefono = column(String(15), nullable=False)
    email = column(String(50), nullable=False)
    direccion = column(String(10), nullable=False)  # Cambiado a String para almacenar la fecha como texto
    indicador_habilitado = column(integer(1), nullable=False)  # Cambiado a String para almacenar el estado como 
    
    def __repr__(self):
        return f'proveedores({self.id_proveedor}, {self.nombre}, {self.contacto}, {self.telefono}, {self.email}, {self.direccion}, {self.indicador_habilitado})'
    
    def __str__(self):
        return f'proveedores({self.id_proveedor}, {self.nombre}, {self.contacto}, {self.telefono}, {self.email}, {self.direccion}, {self.indicador_habilitado})'
    