from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.patient import router as patient_router

app = FastAPI()

# ✅ CORS FIX (ADD THIS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(patient_router)

@app.get("/")
def home():
    return {"msg": "Backend running 🚀"}