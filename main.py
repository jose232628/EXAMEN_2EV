from httpx import request
from data.database import database
from typing import Annotated

from data.dao.dao_hospitales import DaoHospitales

from data.modelo.menu import Menu

from typing import Union

from fastapi import FastAPI, Request,Form



from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="./static"), name="static")


templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):

    menu = Menu(True, True)

    hospitales = DaoHospitales().get_all(database)

    return templates.TemplateResponse(
        request= request, name="index.html", context={"menu": menu,"hospitales": hospitales}
    )

######################################################## DATA BASE ##############################################################


@app.get("/database")
def get_hospitales(request: Request, nombre : str = "Steven"):

    menu = Menu(True, True)

    hospitales = DaoHospitales().get_all(database)

    return templates.TemplateResponse(
        request=request, name="database.html", context={"menu": menu,"hospitales": hospitales}
    )

@app.post("/numpacientes")
def numero_pacientes(request: Request, numero_pacientes):
    menu = Menu(True, True)
    dao = DaoHospitales()

    dao.get_num(database, numero_pacientes)
    
    hospitales =  dao.get_all(database)
    menu = Menu(True, True)
    return templates.TemplateResponse(
    request=request, name="database_numero.html", context={"menu" : menu, "hospitales": hospitales} )

@app.get("/formaddhospitales")
def form_add_hospitales(request: Request):
    menu = Menu(True, True)

    hospitales = DaoHospitales().get_all(database)

    return templates.TemplateResponse(
        request=request, name="formaddartistas.html", context={"menu": menu,"hospitales": hospitales}
    )

@app.post("/addhospitales")
def add_hospitales(request: Request, nombre: Annotated[str, Form()] = None):
    if nombre is None:
        return templates.TemplateResponse(
        request=request, name="formaddartistas.html", context={"hospitales": hospitales}
        )
    
    dao = DaoHospitales()
    dao.insert(database, nombre)
    
    hospitales =  dao.get_all(database)
    menu = Menu(True, True)
    return templates.TemplateResponse(
    request=request, name="añadido.html", context={"menu" : menu, "hospitales": hospitales}
)
    
@app.get("/delhospital")
def form_delete_hospitales(request: Request):
    menu = Menu(True, True)
    dao = DaoHospitales()
    
    hospitales =  dao.get_all(database)
    return templates.TemplateResponse(
        request=request, name="formdelartistas.html", context={"menu" : menu, "hospitales" :hospitales}
    )

@app.post("/delhospitales")
def del_hospitales(request: Request,hospital_id:Annotated[str, Form()] ):
    dao = DaoHospitales()
    dao.delete(database, hospital_id)
    hospitales =  dao.get_all(database)
    menu = Menu(True, True)
    return templates.TemplateResponse(
    request=request, name="eliminado.html", context={"menu" : menu, "hospitales": hospitales} )

@app.get("/formupdatehospital")
def form_update_hospital(request: Request):
    menu = Menu(True, True)
    dao = DaoHospitales()
    hospitales = dao.get_all(database)
    
    return templates.TemplateResponse(
        request=request,
        name="formupdateartista.html",
        context={"menu": menu, "hospitales": hospitales}
    )

@app.post("/updatehospital")
def update_hospital(request: Request, hospital_id: Annotated[str, Form()], nuevo_numero_pacientes: Annotated[int, Form()]):
    menu = Menu(True, True)
    dao = DaoHospitales()

    hospitales = dao.get_all(database)
    
    return templates.TemplateResponse(
        request=request,
        name="actualizado.html",
        context={"menu": menu, "hospitales": hospitales}
    )