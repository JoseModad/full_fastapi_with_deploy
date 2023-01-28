# Pydantic
from pydantic import BaseModel

# Typing
from typing import Optional, Union

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
    
    
class UpdateUser(BaseModel):
    username : str = None
    password : str = None
    nombre: str = None
    apellido: str = None
    direccion: str = None
    telefono: int = None
    correo : str = None
    
    
class ShowUser(BaseModel):
    username : str
    nombre : str
    correo : str
    class Config():
        orm_mode = True
        
        
class Login(BaseModel):
    username: str
    password: str
    

# Schemes Crypto-Jose
   
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None
