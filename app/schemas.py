# Pydantic
from pydantic import BaseModel

# Typing
from typing import Optional

# Python
from datetime import datetime


# User Models
class User(BaseModel):      # Schema
    username : str
    password : str
    nombre: str
    apellido: str
    direccion: Optional[str]
    telefono: int
    correo : str
    creacion_user: datetime = datetime.now()
    

class UserId(BaseModel):
    id: int
    
    
class ShowUser(BaseModel):
    username : str
    nombre : str
    correo : str
    class Config():
        orm_mode = True