from sqlalchemy import Column, String, Integer, Date, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ProductosModelo(Base):
    __tablename__ = "productos"
    id_producto =  Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(20))
    descripcion = Column(String(100))
    sku = Column(String(20))
    id_categoria = Column(Integer)
    id_proveedor = Column(Integer)
    precio_compra = Column(Float)
    precio_venta = Column(Float)
    stock_actual = Column(Float)
    stock_minimo = Column(Float)
    id_almacen = Column(Integer)
    fecha_creacion = Column(Date)
    indicadorHabilitado = Column(Integer)  # 1 = habilitado, 0 = deshabilitado