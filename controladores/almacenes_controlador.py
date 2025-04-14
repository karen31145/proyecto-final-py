import sqlalchemy as db 
from persistence.modelo_almacenes import Alamacenes
from sqlalchemy.orm import Session
from typing import List  # Asegúrate de importar List de typing
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

class almacenesRepository():
    def __init__(self):
        self.engine = db.create_engine('mysql+pymysql://proyectoinventario_easierbaby:9ba541562e0fa4efa6d4be650b0ba273db1359fb@07880.h.filess.io:61001/proyectoinventario_easierbaby', echo=True, future=True)

    def register(self, nombre, ubicacion):
        almacenes = Alamacenes()
        almacenes.nombre = nombre
        almacenes.ubicacion= ubicacion
        with Session(self.engine) as session:
            session.add(almacenes)
            session.commit()
    
    def modificar(self, nombre, ubicacion, id_almacen):
        try:
            # Buscar el producto en la base de datos
            with Session(self.engine) as session:
                almacen = session.query(Alamacenes).filter_by(id=id_almacen).one()

                # Actualizar los atributos del producto
                almacen.nombre = nombre
                almacen.ubicacion = ubicacion

                # Confirmar los cambios en la base de datos
                session.commit()
                print(f"almacen con ID {id_almacen} actualizado correctamente.")
                return True
        except NoResultFound:
            print(f"No se encontró ningún almacen con ID {id_almacen}. No se realizó ninguna modificación.")
            return False
        except Exception as e:
            print(f"Error al actualizar el producto: {e}")
            return False
 
    def obtener_Almacenes(self) -> List[Alamacenes]:
        with Session(self.engine) as session:
            productos = session.query(Alamacenes).all()
        return productos
    
    def eliminar(self, id_almacen):
        with Session(self.engine) as session:
            almacen = session.query(Alamacenes).filter_by(id=id_almacen).first()
            if almacen:
                try:
                    session.delete(almacen)
                    session.commit()
                    print(f"Producto con ID {id_almacen} eliminado correctamente.")
                except IntegrityError as e:
                    session.rollback()
                    print(f"No se pudo eliminar el almacen con ID {id_almacen}. Error: {e}")
            else:
                print(f"No se encontró ningún almacen con ID {id_almacen}.")

    def getByName(self, name: str):
        almacen: Alamacenes = None
        with Session(self.engine) as session:
            almacen = session.query(Alamacenes).filter_by(
            nombre=name).first()
        return almacen