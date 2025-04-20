import sqlalchemy as db
from sqlalchemy.orm import Session
from persistence.modelo_productos import ProductosModelo
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
from datetime import datetime


class ControladorProductoRepository():
    def __init__(self):
        self.engine = db.create_engine('mysql+pymysql://proyectoinventario_easierbaby:9ba541562e0fa4efa6d4be650b0ba273db1359fb@07880.h.filess.io:61001/proyectoinventario_easierbaby', echo=True, future=True)

    def register(self, producto: ProductosModelo):
        with Session(self.engine) as session:
            session.add(producto)
            session.commit()
            
    def update(self, producto_modificado: ProductosModelo):
        with Session(self.engine) as session:
            producto = session.query(ProductosModelo).filter_by(sku=producto_modificado.sku).first()
            if producto:
                producto.nombre = producto_modificado.nombre
                producto.descripcion = producto_modificado.descripcion  
                producto.id_categoria = producto_modificado.id_categoria
                producto.stock_actual = producto_modificado.stock_actual
                producto.stock_minimo = producto_modificado.stock_minimo
                producto.id_proveedor = producto_modificado.id_proveedor
                producto.precio_compra = producto_modificado.precio_compra
                producto.precio_venta = producto_modificado.precio_venta
                producto.id_almacen = producto_modificado.id_almacen
                producto.fecha_creacion = producto_modificado.fecha_creacion
                producto.indicadorHabilitado = True
                # ... otros campos que quieras actualizar
                session.commit()
                
    def inhabilitar(self, _sku):
        with Session(self.engine) as session:
            producto = session.query(ProductosModelo).filter_by(sku=_sku).first()
            if producto:
                producto.indicadorHabilitado = False
                producto.fecha_creacion = datetime.now()
                # ... otros campos que quieras actualizar
                session.commit()            

    def obtener_productosAll(self) -> List[ProductosModelo]:
        with Session(self.engine) as session:
                productos = session.query(ProductosModelo).all()
        return productos
    
    def getSku(self, _sku: str):
        producto: ProductosModelo = None
        with Session(self.engine) as session:
            producto = session.query(ProductosModelo).filter_by(
            sku=_sku).first()
        return producto