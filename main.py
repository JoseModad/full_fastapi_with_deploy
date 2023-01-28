# Fastapi
from fastapi import FastAPI

# Uvicorn
import uvicorn

# Instancia Router
from app.routers import user
from app.db.database import Base, engine
from app.routers import user, auth


# Instancia de Fastapi
app = FastAPI()

# Instancias Router
app.include_router(user.router)
app.include_router(auth.router)



# Corriendo la aplicacion
if __name__=="__main__":
    uvicorn.run("main:app", port = 8000, reload = True)