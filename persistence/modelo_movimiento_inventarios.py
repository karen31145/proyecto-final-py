from sqlalchemy import Column
from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MovimientoInventariosModel(Base):
    __tablename__ = "Movimiento_Inventarios"
    
    id_proveedor = Column(Integer, primary_key=True, autoincrement=True)
    tipo_movimiento = Column(String(50), nullable=False)
    cantidad = Column(String(100), nullable=False)
    proveedor = Column(String(15), nullable=False)
    id_almacen = Column(String(50), nullable=False)
    referencia = Column(String(10), nullable=False)  # Cambiado a String para almacenar la fecha como texto
    observaciones = Column(String(20), nullable=False)  # Cambiado a String para almacenar el estado como texto
    