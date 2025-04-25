from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from persistence.modelo_productos import ProductosModelo
from persistence.base import Base

class VentaModelo(Base):
    __tablename__ = "ventas"

    id_ventas = Column(Integer, primary_key=True, autoincrement=True)  # Renombrado a id_venta
    id_producto = Column(Integer, ForeignKey("productos.id_producto"))  # Si quieres mantener la relación con el producto
    cantidad = Column(Integer)  # Mejor como Integer si es una cantidad numérica
    fecha = Column(Date)  # Cambio a Date si es una fecha
    codigo_venta = Column(String(500))
    producto = relationship(lambda: ProductosModelo)

    

    def __repr__(self):
        return f"<Venta(id_venta={self.id_venta}, id_producto={self.id_producto}, cantidad={self.cantidad}, fecha={self.fecha}, codigo_venta={self.codigo_venta})>"
