import sqlalchemy as db
from sqlalchemy.orm import Session
from persistence.modelo_productos import ProductosModelo
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor


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

    def update_all(self, productos_modificados: List[ProductosModelo]):
        with Session(self.engine) as session:
            for producto_modificado in productos_modificados:
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
            session.commit()  # Se hace solo UNA vez al final, para todos
                
    def inhabilitar(self, _sku):
        with Session(self.engine) as session:
            producto = session.query(ProductosModelo).filter_by(sku=_sku).first()
            if producto:
                producto.indicadorHabilitado = False
                producto.fecha_creacion = datetime.now()
                # ... otros campos que quieras actualizar
                session.commit()            

    def obtener_productosAll(self) -> List[ProductosModelo]:
        def tarea():
            with Session(self.engine) as session:
                return session.query(ProductosModelo).all()

        with ThreadPoolExecutor(max_workers=1) as executor:
            futuro = executor.submit(tarea)
            return futuro.result()
        
    def findByIndicadorHabilitado(self) -> List[ProductosModelo]:
        def tarea():
            with Session(self.engine) as session:
                return session.query(ProductosModelo)\
                              .filter((ProductosModelo.indicadorHabilitado == True) & (ProductosModelo.stock_actual >= 1))\
                              .all()

        with ThreadPoolExecutor(max_workers=1) as executor:
            futuro = executor.submit(tarea)
            return futuro.result()
        

    def getSku(self, _sku: str):
        producto: ProductosModelo = None
        with Session(self.engine) as session:
            producto = session.query(ProductosModelo).filter_by(
            sku=_sku).first()
        return producto