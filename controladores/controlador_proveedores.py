import sqlalchemy as db
from sqlalchemy.orm import Session
from persistence.modelo_proveedores import ProveedoresModel
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError


class ControladorProveedoresReposito():
    def __init__(self):
        self.engine = db.create_engine('mysql+pymysql://proyectoinventario_easierbaby:9ba541562e0fa4efa6d4be650b0ba273db1359fb@07880.h.filess.io:61001/proyectoinventario_easierbaby', echo=True, future=True)
        
        
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

    def update(self, id_proveedor, nombre, contacto, telefono, email, direccion, indicador_habilitado):
        try:
            with Session(self.engine) as session:
                proveedor = session.query(ProveedoresModel).filter_by(id=id_proveedor).one()

                proveedor.nombre = nombre
                proveedor.contacto = contacto
                proveedor.telefono = telefono
                proveedor.email = email
                proveedor.direccion = direccion
                proveedor.indicador_habilitado = indicador_habilitado

                session.commit()
                print("Proveedor actualizado correctamente")

        except NoResultFound:
            print(f"No se encontró un proveedor con id {id_proveedor}")
        except IntegrityError as e:
            print("Error de integridad al actualizar el proveedor:", e)
        except Exception as e:
            print("Error inesperado al actualizar:", e)

    def obtener_proveedores(self) -> List[ProveedoresModel]:
            with Session(self.engine) as session:
                productos = session.query(ProveedoresModel).all()
            return productos

    def getByName(self, name: str):
        proveedores: ProveedoresModel = None
        with Session(self.engine) as session:
            proveedores = session.query(ProveedoresModel).filter_by(
            nombre=name).first()
        return proveedores