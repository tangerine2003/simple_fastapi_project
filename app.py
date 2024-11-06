from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated

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

    # Store a JSON object with the Drugs information that will be loaded into the webpage
    # Return this dataset to the webpage

    # In the webpage create a loop and load the items into the table dynamically.
drugs_data = [
    {"drug_name": "Albuterol", "manufacturer": "Teva Pharmaceuticals", "description": "Used to treat or prevent bronchospasm in people with reversible obstructive airway disease."},
    {"drug_name": "Amlodipine", "manufacturer": "Pfizer", "description": "Used to treat high blood pressure and prevent chest pain (angina)."},
    {"drug_name": "Amoxicillin", "manufacturer": "GSK (GlaxoSmithKline)", "description": "Antibiotic used to treat various bacterial infections."},
    {"drug_name": "Atorvastatin", "manufacturer": "Pfizer", "description": "Used to lower cholesterol and reduce the risk of heart disease."},
    {"drug_name": "Carvedilol", "manufacturer": "Roche", "description": "Used to treat heart failure and hypertension."},
    {"drug_name": "Citalopram", "manufacturer": "Lundbeck", "description": "Used to treat depression."},
    {"drug_name": "Escitalopram", "manufacturer": "Lundbeck", "description": "Used to treat depression and generalized anxiety disorder."},
    {"drug_name": "Fluticasone", "manufacturer": "GSK (GlaxoSmithKline)", "description": "A corticosteroid used to treat asthma and allergies."},
    {"drug_name": "Furosemide", "manufacturer": "Sanofi", "description": "Used to treat fluid retention (edema) in people with congestive heart failure, liver disease, or kidney disorder."},
    {"drug_name": "Gabapentin", "manufacturer": "Pfizer", "description": "Used to treat nerve pain and seizures."},
    {"drug_name": "Hydrochlorothiazide", "manufacturer": "Novartis", "description": "A diuretic used to treat high blood pressure and fluid retention (edema)."},
    {"drug_name": "Ibuprofen", "manufacturer": "Pfizer", "description": "A nonsteroidal anti-inflammatory drug (NSAID) used to reduce fever and treat pain or inflammation."},
    {"drug_name": "Levothyroxine", "manufacturer": "AbbVie", "description": "Treats hypothyroidism, a condition where the thyroid gland doesn't produce enough hormones."},
    {"drug_name": "Lisinopril", "manufacturer": "AstraZeneca", "description": "An ACE inhibitor used to treat high blood pressure and heart failure."},
    {"drug_name": "Losartan", "manufacturer": "Merck & Co.", "description": "Used to treat high blood pressure and protect the kidneys from damage due to diabetes."},
    {"drug_name": "Metformin", "manufacturer": "Sun Pharmaceutical", "description": "Improves blood sugar control in people with type 2 diabetes."},
    {"drug_name": "Metoprolol", "manufacturer": "AstraZeneca", "description": "Used to treat high blood pressure, angina, and heart failure."},
    {"drug_name": "Montelukast", "manufacturer": "Merck & Co.", "description": "Prevents asthma attacks and treats allergies."},
    {"drug_name": "Omeprazole", "manufacturer": "AstraZeneca", "description": "Treats gastroesophageal reflux disease (GERD) and other conditions caused by excess stomach acid."},
    {"drug_name": "Prednisone", "manufacturer": "Pfizer", "description": "A corticosteroid used to treat a variety of inflammatory conditions and autoimmune diseases."},
    {"drug_name": "Sertraline", "manufacturer": "Pfizer", "description": "Used to treat depression, anxiety disorders, and PTSD."},
    {"drug_name": "Simvastatin", "manufacturer": "Merck & Co.", "description": "Lowers cholesterol and triglycerides in the blood."},
    {"drug_name": "Tramadol", "manufacturer": "Janssen Pharmaceuticals", "description": "Used to treat moderate to severe pain."},
    {"drug_name": "Trazodone", "manufacturer": "Teva Pharmaceuticals", "description": "Used to treat depression and anxiety disorders."}
    ]

@app.get("/manage_drugs", response_class=HTMLResponse)
async def manage_drugs(request: Request):
    # Pass the drugs_data to the template
    return templates.TemplateResponse("index.html", {"request": request, "table_data": drugs_data})

@app.get("/login", response_class=HTMLResponse)
async def patient_login(request: Request):
    return templates.TemplateResponse(
        request=request, name="patient_login.html"
    )

# @app.post("/login")
# async def patient_login_post(username: Annotated[str, Form()], password: Annotated[str, Form()]):
#     # Authenticate user here, then redirect as needed
#     return RedirectResponse(url="/", status_code=303)

@app.post("/login_user")
async def login():
    return RedirectResponse(url="/", status_code=303)
    

@app.get("/patient_profile", response_class=HTMLResponse)
async def patient_profile(request: Request):
    return templates.TemplateResponse(
        request=request, name="patient_profile.html"
    )

@app.get("/contactus_page", response_class=HTMLResponse)
async def contactus_page(request: Request):
    return templates.TemplateResponse(
        request=request, name="contactus_page.html"
    )

@app.get("/healthinfo_page", response_class=HTMLResponse)
async def healthinfo_page(request: Request):
    return templates.TemplateResponse(
        request=request, name="healthinfo_page.html"
    )

@app.get("/registration_form", response_class=HTMLResponse)
async def registration_form(request: Request):
    return templates.TemplateResponse(
        request=request, name="registration_form.html"
    )
