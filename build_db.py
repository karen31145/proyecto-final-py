import sqlalchemy as db 
import persistence.modelo as mod

engine = db.create_engine('mysql+pymysql://proyectoinventario_easierbaby:9ba541562e0fa4efa6d4be650b0ba273db1359fb@07880.h.filess.io:61001/proyectoinventario_easierbaby', echo=True, future=True)
mod.Base.metadata.create_all(engine)
