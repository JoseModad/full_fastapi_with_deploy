# Fastapi
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

# Schemas
from sqlalchemy.orm import Session
from app.db.database import get_db
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
def login(usuario: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    auth_token = auth.auth_user(usuario, db)
    return auth_token