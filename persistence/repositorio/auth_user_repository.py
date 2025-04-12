import sqlalchemy as db 
from persistence.modelo import Aut_user
from sqlalchemy.orm import Session

class AuthUserRepository():
    def __init__(self):
        self.engine = db.create_engine('mysql+pymysql://proyectoinventario_easierbaby:9ba541562e0fa4efa6d4be650b0ba273db1359fb@07880.h.filess.io:61001/proyectoinventario_easierbaby', echo=True, future=True)

    def getUserByUserName(self, user_name: str):
        user: Aut_user = None
        with Session(self.engine) as session:
            user = session.query(Aut_user).filter_by(
                nombre_usuario=user_name).first()
            return user
        
    def insertUser(self, user: Aut_user):
        with Session(self.engine) as session:
            session.add(user)
            session.commit()