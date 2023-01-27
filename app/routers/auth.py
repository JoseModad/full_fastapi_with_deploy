# Fastapi
from fastapi import APIRouter, Depends, status

# Schemas
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas import Login
from app.repository import auth


# Typing
from typing import List


# Instancia Fastapi
router = APIRouter(
    prefix = "/login",
    tags = ["Login"]
)


# Rutas

@router.post("/", status_code = status.HTTP_200_OK)
def login(usuario: Login, db: Session = Depends(get_db)):
    auth.auth_user(usuario, db)
    return {"respuesta": "Login aceptado"}