# Fastapi
from fastapi import FastAPI

# Uvicorn
import uvicorn

# Instancia Router
from app.routers import user
from app.db.database import Base, engine
from app.routers import user


def create_tables():
    Base.metadata.create_all(bind = engine)

create_tables()


# Instancia de fastapi
app = FastAPI()
app.include_router(user.router)



# Corriendo la aplicacion
if __name__=="__main__":
    uvicorn.run("main:app", port = 8000, reload = True)

