import sqlalchemy as db 
from persistence.modelo_categorias import CategoriaModelo
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

class CategoriasRepository():
    def __init__(self):
        self.engine = db.create_engine(
            'mysql+pymysql://proyectoinventario_easierbaby:9ba541562e0fa4efa6d4be650b0ba273db1359fb@07880.h.filess.io:61001/proyectoinventario_easierbaby',
            echo=True,
            future=True
        )

    def register(self, nombre, descripcion):
        nueva_categoria = CategoriaModelo(nombre=nombre, descripcion=descripcion)
        with Session(self.engine) as session:
            session.add(nueva_categoria)
            session.commit()
    
    def modificar(self, nombre, descripcion, id_categoria):
        try:
            with Session(self.engine) as session:
                categoria = session.query(CategoriaModelo).filter_by(id_categoria=id_categoria).one()
                categoria.nombre = nombre
                categoria.descripcion = descripcion
                session.commit()
                print(f"Categoría con ID {id_categoria} actualizada correctamente.")
                return True
        except NoResultFound:
            print(f"No se encontró categoría con ID {id_categoria}.")
            return False
        except Exception as e:
            print(f"Error al actualizar la categoría: {e}")
            return False

    def obtener_Categorias(self) -> List[CategoriaModelo]:
        with Session(self.engine) as session:
            categorias = session.query(CategoriaModelo).all()
        return categorias
    
    def eliminar(self, id_categoria):
        with Session(self.engine) as session:
            categoria = session.query(CategoriaModelo).filter_by(id_categoria=id_categoria).first()
            if categoria:
                try:
                    session.delete(categoria)
                    session.commit()
                    print(f"Categoría con ID {id_categoria} eliminada correctamente.")
                except IntegrityError as e:
                    session.rollback()
                    print(f"No se pudo eliminar la categoría con ID {id_categoria}. Error: {e}")
            else:
                print(f"No se encontró ninguna categoría con ID {id_categoria}.")

    def getByName(self, name: str):
        with Session(self.engine) as session:
            return session.query(CategoriaModelo).filter_by(nombre=name).first()
