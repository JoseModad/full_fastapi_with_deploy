# Pydantic
from pydantic import BaseModel

# Typing
from typing import Optional

# Python
from datetime import datetime



# User Models
class User(BaseModel):      # Schema
    id: int
    nombre: str
    apellido: str
    direccion: Optional[str]
    telefono: int
    correo = str
    creacion_user: datetime = datetime.now()
    

class UserId(BaseModel):
    id: int