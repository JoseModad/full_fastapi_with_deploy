# Fastapi
from fastapi import FastAPI

# Uvicorn
import uvicorn

# Pydantic
from pydantic import BaseModel


# Typing
from typing import Optional

# Python
from datetime import datetime


# Instancia de fastapi
app = FastAPI()

# Lista de prueba
usuarios = []


# User Models
class User(BaseModel):      # Schema
    id: int
    nombre: str
    apellido: str
    direccion: Optional[str]
    telefono: int
    creacion_user: datetime = datetime.now()
    

class UserId(BaseModel):
    id: int

# Rutas

@app.get("/ruta1")
def ruta1():
    return {"mensaje": "Bienvenido a Fastapi"}


@app.get("/user")
def obtener_usuarios():
    return usuarios


@app.post("/user")
def crear_usuario(user: User):
    usuario = user.dict()
    usuarios.append(usuario)    
    return {"Respuesta": "Usuario creado satisfactoriamente"}


@app.get("/user/{user_id}")
def obtener_usuario(user_id: int):
    for user in usuarios:
        if user["id"] == user_id:
            return {"usuario": user}
        
        return {"respuesta": "usuario no encontrado"}
    

@app.post("/obtener_usuario")
def obtener_usuario(user_id: UserId):
    for user in usuarios:
        if user["id"] == user_id.id:
            return {"usuario": user}
        
        return {"respuesta": "usuario no encontrado"}
    
    
@app.delete("/user/{user_id}")
def eliminar_usuario(user_id: int):
    for index, user in enumerate(usuarios):        
        if user["id"] == user_id:
            usuarios.pop(index)
            return {"respuesta": "Usuario eliminado correctamente"}
    return {"Respuesta": "Usuario no encontrado"}    
        


@app.put("/user/{user_id}")
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
            

# Corriendo la aplicacion
if __name__=="__main__":
    uvicorn.run("main:app", port = 8000, reload = True)

