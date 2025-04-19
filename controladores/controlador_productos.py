import sqlalchemy as db
from sqlalchemy.orm import Session
from persistence.modelo_productos import ProductosModelo
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError

class ControladorProductoRepository():
    def __init__(self):
        self.engine = db.create_engine('mysql+pymysql://proyectoinventario_easierbaby:9ba541562e0fa4efa6d4be650b0ba273db1359fb@07880.h.filess.io:61001/proyectoinventario_easierbaby', echo=True, future=True)

    def register(self, producto: ProductosModelo):
        with Session(self.engine) as session:
            session.add(producto)
            session.commit()
            
    def obtener_productosAll(self) -> List[ProductosModelo]:
        with Session(self.engine) as session:
                productos = session.query(ProductosModelo).all()
        return productos