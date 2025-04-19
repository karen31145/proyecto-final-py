from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class VentaModelo(Base):
    __tablename__ = "ventas"
    
    id_ventas = Column(Integer, primary_key=True, autoincrement=True)  # Renombrado a id_venta
    id_producto = Column(Integer)  # Si quieres mantener la relación con el producto
    cantidad = Column(Integer)  # Mejor como Integer si es una cantidad numérica
    fecha = Column(Date)  # Cambio a Date si es una fecha
    codigo_venta = Column(String(500))

    def __repr__(self):
        return f"<Venta(id_venta={self.id_venta}, id_producto={self.id_producto}, cantidad={self.cantidad}, fecha={self.fecha}, codigo_venta={self.codigo_venta})>"
