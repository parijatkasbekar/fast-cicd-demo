from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/images", StaticFiles(directory="images"), name="images")

@app.get("/")
def read_form(request: Request):
    return templates.TemplateResponse("fancy_form.html", {"request": request})

@app.post("/")
def create_greeting(request: Request, name: str = Form(...)):
    return templates.TemplateResponse("fancy_greeting.html", {"request": request, "name": name})
