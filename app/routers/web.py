from fastapi.templating import Jinja2Templates
from fastapi import Request, APIRouter


router = APIRouter()

templates = Jinja2Templates(directory = "app/templates")


@router.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@router.get("/register")
def registration(request: Request):
    return templates.TemplateResponse("create_user.html", {"request": request})


@router.post("/register")
async def registration(request: Request):
    form = await request.form()
    usuario = {
        "username": form.get("username"),
        "password": form.get("password"),
        "nombre": form.get("nombre"),
        "apellido": form.get("apellido"),
        "direccion": form.get("direccion"),
        "telefono": form.get("telefono"),
        "correo": form.get("correo")
    }
    print(usuario)
    return templates.TemplateResponse("create_user.html", {"request": request})
