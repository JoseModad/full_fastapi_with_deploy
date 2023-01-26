from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os


load_dotenv()


USER_CONTRAS = os.getenv("USER_CONTRAS")
BASE_DE_DATOS = os.getenv("BASE_DE_DATOS")

# Conexion a la base de datos
SQLALCHEMY_DATABASE_URL = f"postgresql://{USER_CONTRAS}@localhost:5432/{BASE_DE_DATOS}"

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
