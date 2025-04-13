import sqlalchemy as db
from sqlalchemy.orm import Session
from persistence.modelo_proveedores import ProveedoresModel
from typing import List
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

class ControladorProveedores():
    def __init__(self):
        self.engine=db.create_engine('mysql+pymysql://proyectoinventario_easierbaby:9ba541562e0fa4efa6d4be650b0ba273db1359fb@07880.h.filess.io:61001/proyectoinventario_easierbaby' echo=True, future=True)
        
        
    def register(self,nombre,contacto,telefono,email,direccion,indicador_habilitado):
        proveedor=ProveedoresModel()
        proveedor.nombre=nombre
        proveedor.contacto=contacto
        proveedor.telefono=telefono
        proveedor.email=email
        proveedor.direccion=direccion
        proveedor.indicador_habilitado=indicador_habilitado
        
        with Session(self.engine) as session:
            session.add(proveedor)
            session.commit()