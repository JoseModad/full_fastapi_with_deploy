# Fastapi
from fastapi import APIRouter, Depends

# Schemas
from app.schemas import User, UserId
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models


# Instancia Fastapi
router = APIRouter(
    prefix = "/user",
    tags = ["Users"]
    )


# Lista de prueba
usuarios = []


# Rutas

@router.get("/ruta1")
def ruta1():
    return {"mensaje": "Bienvenido a Fastapi"}


@router.get("/")
def obtener_usuarios(db: Session = Depends(get_db)):
    data = db.query(models.User).all()
    print(data)
    return usuarios
    


@router.post("/")
def crear_usuario(user: User):
    usuario = user.dict()
    usuarios.append(usuario)    
    return {"Respuesta": "Usuario creado satisfactoriamente"}


@router.get("/{user_id}")
def obtener_usuario(user_id: int):
    for user in usuarios:
        if user["id"] == user_id:
            return {"usuario": user}
        
        return {"respuesta": "usuario no encontrado"}
    

@router.post("/obtener_usuario")
def obtener_usuario(user_id: UserId):
    for user in usuarios:
        if user["id"] == user_id.id:
            return {"usuario": user}
        
        return {"respuesta": "usuario no encontrado"}
    
    
@router.delete("/{user_id}")
def eliminar_usuario(user_id: int):
    for index, user in enumerate(usuarios):        
        if user["id"] == user_id:
            usuarios.pop(index)
            return {"respuesta": "Usuario eliminado correctamente"}
    return {"Respuesta": "Usuario no encontrado"}    
        


@router.put("/{user_id}")
def actualizar_usuario(user_id: int, updateUser: User):
    for index, user in enumerate(usuarios):        
        if user["id"] == user_id:
            usuarios[index]["id"] = updateUser.dict()["id"]
            usuarios[index]["nombre"] = updateUser.dict()["nombre"]
            usuarios[index]["apellido"] = updateUser.dict()["apellido"]
            usuarios[index]["direccion"] = updateUser.dict()["direccion"]
            usuarios[index]["telefono"] = updateUser.dict()["telefono"]
            return {"Usuario actualizado correctamente"}
    return {"Usuario no encontrado"}