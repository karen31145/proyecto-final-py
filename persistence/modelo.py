from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class _Aut_user(Base):
    _tablename_ = "usuarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20))
    password = Column(String(20))

