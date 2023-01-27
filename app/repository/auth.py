from sqlalchemy.orm import Session
from app.db import models
from fastapi import HTTPException, status
from app.hashing import Hash

def auth_user(usuario, db: Session):
    usuario = usuario.dict()
    user = db.query(models.User).filter(models.User.username == usuario["username"]).first()
    if not user:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f'No existe el usuario con el username: {usuario["username"]}, por lo tanto no se realizo el login'
        )
        
    if not Hash.verify_password(usuario["password"], user.password):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Contrasena incorrecta"
        )
    