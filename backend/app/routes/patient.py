from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Patient

router = APIRouter(prefix="/patients", tags=["Patients"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_patient(name: str, age: int, db: Session = Depends(get_db)):
    patient = Patient(name=name, age=age)
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

@router.get("/")
def get_patients(db: Session = Depends(get_db)):
    return db.query(Patient).all()

@router.delete("/{id}")
def delete_patient(id: int, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == id).first()
    if patient:
        db.delete(patient)
        db.commit()
        return {"msg": "Deleted"}
    return {"msg": "Not Found"}