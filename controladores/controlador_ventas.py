import sqlalchemy as db 
from persistence.modelo_ventas import VentaModelo
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

class VentasRepository():
    def __init__(self):
        self.engine = db.create_engine(
            'mysql+pymysql://proyectoinventario_easierbaby:9ba541562e0fa4efa6d4be650b0ba273db1359fb@07880.h.filess.io:61001/proyectoinventario_easierbaby',
            echo=True,
            future=True
        )

    def register(self,id_producto ,cantidad, fecha, codigo_venta):
        nueva_venta = VentaModelo(id_producto=id_producto, cantidad=cantidad, fecha=fecha, codigo_venta=codigo_venta)
        with Session(self.engine) as session:
            session.add(nueva_venta)
            session.commit()

    def modificar(self, cantidad, fecha, codigo_venta, id_venta):
        try:
            with Session(self.engine) as session:
                venta = session.query(VentaModelo).filter_by(id_venta=id_venta).one()
                venta.cantidad = cantidad
                venta.fecha = fecha
                venta.codigo_venta = codigo_venta
                session.commit()
                print(f"Venta con ID {id_venta} actualizada correctamente.")
                return True
        except NoResultFound:
            print(f"No se encontró venta con ID {id_venta}.")
            return False
        except Exception as e:
            print(f"Error al actualizar la venta: {e}")
            return False

    def obtener_Ventas(self) -> List[VentaModelo]:
        with Session(self.engine) as session:
            return session.query(VentaModelo).all()

    def eliminar(self, id_venta):
        with Session(self.engine) as session:
            venta = session.get(VentaModelo, id_venta).filter_by(id_venta=id_venta).first()
            if venta:
                try:
                    session.delete(venta)
                    session.commit()
                    print(f"Venta con ID {id_venta} eliminada correctamente.")
                except IntegrityError as e:
                    session.rollback()
                    print(f"No se pudo eliminar la venta con ID {id_venta}. Error: {e}")
            else:
                print(f"No se encontró ninguna venta con ID {id_venta}.")

    def getByCodigo(self, code: str):
        with Session(self.engine) as session:
            return session.query(VentaModelo).filter_by(codigo_venta=code).first()