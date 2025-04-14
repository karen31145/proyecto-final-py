import sqlalchemy as db 
from persistence.modelo_categorias import CategoriaModelo
from sqlalchemy.orm import Session
from typing import List  # Asegúrate de importar List de typing
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

class CategoriasRepository():
    def __init__(self):
        self.engine = db.create_engine('mysql+pymysql://proyectoinventario_easierbaby:9ba541562e0fa4efa6d4be650b0ba273db1359fb@07880.h.filess.io:61001/proyectoinventario_easierbaby', echo=True, future=True)

    def register(self, nombre, descripcion):
        categoria = categoria()
        categoria.nombre = nombre
        categoria.descripcion= descripcion
        with Session(self.engine) as session:
            session.add(categoria)
            session.commit()
    
    def modificar(self, nombre, descripcion, id_categoria):
        try:
            # Buscar el producto en la base de datos
            with Session(self.engine) as session:
                almacen = session.query(CategoriaModelo).filter_by(id=id_categoria).one()

                # Actualizar los atributos del producto
                almacen.nombre = nombre
                almacen.ubicacion = descripcion

                # Confirmar los cambios en la base de datos
                session.commit()
                print(f"categoria con ID {id_categoria} actualizado correctamente.")
                return True
        except NoResultFound:
            print(f"No se encontró categoria con ID {id_categoria}. No se realizó ninguna modificación.")
            return False
        except Exception as e:
            print(f"Error al actualizar el producto: {e}")
            return False
 
    def obtener_Categorias(self) -> List[CategoriaModelo]:
        with Session(self.engine) as session:
            productos = session.query(CategoriaModelo).all()
        return productos
    
    def eliminar(self, id_categoria):
        with Session(self.engine) as session:
            Categorias = session.query(Categorias).filter_by(id=id_categoria).first()
            if Categorias:
                try:
                    session.delete(Categorias)
                    session.commit()
                    print(f"Producto con ID {id_categoria} eliminado correctamente.")
                except IntegrityError as e:
                    session.rollback()
                    print(f"No se pudo eliminar el almacen con ID {id_categoria}. Error: {e}")
            else:
                print(f"No se encontró ningún almacen con ID {id_categoria}.")

    def getByName(self, name: str):
        categoria: CategoriaModelo = None
        with Session(self.engine) as session:
            categoria = session.query(CategoriaModelo).filter_by(
            nombre=name).first()
        return categoria