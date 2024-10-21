from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="home.html"
    )

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id, "name": "This is my item"},
    )

@app.get("/manage_drugs", response_class=HTMLResponse)
async def manage_drugs(request: Request):
    return templates.TemplateResponse(
        request=request, name="manage_drugs.html"
    )

@app.get("/Patient_login", response_class=HTMLResponse)
async def Patient_login(request: Request):
    return templates.TemplateResponse(
        request=request, name="Patient_login.html"
    )

@app.get("/patient_profile", response_class=HTMLResponse)
async def patient_profile(request: Request):
    return templates.TemplateResponse(
        request=request, name="patient_profile.html"
    )

@app.get("/ContactUs_Page", response_class=HTMLResponse)
async def ContactUs_Page(request: Request):
    return templates.TemplateResponse(
        request=request, name="ContactUs_Page.html"
    )

@app.get("/HealthInfo_Page", response_class=HTMLResponse)
async def HealthInfo_Page(request: Request):
    return templates.TemplateResponse(
        request=request, name="HealthInfo_Page.html"
    )

@app.get("/registration_form", response_class=HTMLResponse)
async def registration_form(request: Request):
    return templates.TemplateResponse(
        request=request, name="registration_form.html"
    )
