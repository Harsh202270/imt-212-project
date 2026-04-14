from fastapi import FastAPI
from app.routes.patient import router as patient_router

app = FastAPI()

app.include_router(patient_router)

@app.get("/")
def home():
    return {"msg": "Backend running 🚀"}