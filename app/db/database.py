from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from core.config import settings


# Conexion a la base de datos
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# Interaccion con la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Como estan los datos actualmente
SessionLocal = sessionmaker(bind = engine, autocommit = False, autoflush = False)

# Base para crear modelos
Base = declarative_base()


# Devuelve la sesion de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
