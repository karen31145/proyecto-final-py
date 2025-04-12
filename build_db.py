from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://proyectoinventario_easierbaby:9ba541562e0fa4efa6d4be650b0ba273db1359fb@07880.h.filess.io:61001/proyectoinventario_easierbaby")

# Probar la conexión
with engine.connect() as connection:
    result = connection.execute(text("SELECT NOW()"))
    for row in result:
        print(row)

