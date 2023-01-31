from fastapi.testclient import TestClient

import sys
import os
import time

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Carga de la ruta para importar el modulo app del main
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from main import app
from app.db.models import Base
from app.hashing import Hash
from app.db.database import get_db

# Carga la ruta de la base de datos de prueba
db_path = os.path.join(os.path.dirname(__file__), "test.db")

db_uri = "sqlite:///{}".format(db_path)
SQLALCHEMY_DATABASE_URL = db_uri

engine_test = create_engine(db_uri, connect_args = {"check_same_thread": False})

TestingSessionLocal = sessionmaker(bind = engine_test, autocommit = False, autoflush = False)

Base.metadata.create_all(bind = engine_test)


cliente = TestClient(app)


def insertar_usuario_prueba():
    
    password_hash = Hash.hash_password('0000')
    
    engine_test.execute(
        f"""
        INSERT INTO usuario(username, password, nombre, apellido, direccion, telefono, correo)
        values
        ('prueba', '{password_hash}', 'pruebanombre', 'pruebaapellido', 'pruebadireccion', 22222222, 'prueba@gmail.com')
        """         
    )
    
    
insertar_usuario_prueba() 


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
 

app.dependency_overrides[get_db] =  override_get_db 

def test_crear_usuario():
    time.sleep(2)
    usuario = {
        "username": "marty",
        "password": "0000",
        "nombre": "martina",
        "apellido": "modad",
        "direccion": "blocker",
        "telefono": 23232323,
        "correo": "martina@hotmail.com",
        "creacion_user": "2023-01-30T20:15:27.362232"
    }
    response = cliente.post("/user/", json = usuario)
    assert response.status_code == 201    
    assert response.json()["Respuesta"] == "Usuario creado satisfactoriamente"
    
    
    
def test_delete_database():
    db_path = os.path.join(os.path.dirname(__file__), 'test.db') 
    os.remove(db_path)