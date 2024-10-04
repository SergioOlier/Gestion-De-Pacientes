#Aquí se iniciará la aplicación FastAPI.

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine, init_db

# Crear las tablas en la base de datos
init_db()

# Instancia de la aplicación FastAPI
app = FastAPI()

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta de prueba
@app.get("/")
def read_root():
    return {"mensaje": "¡Hola, mundo!"}

# Crear una mascota
@app.post("/mascotas/", response_model=schemas.Mascota)
def create_mascota(mascota: schemas.MascotaCreate, db: Session = Depends(get_db)):
    return crud.create_mascota(db=db, mascota=mascota)

# Obtener una lista de mascotas
@app.get("/mascotas/", response_model=list[schemas.Mascota])
def read_mascotas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_mascotas(db, skip=skip, limit=limit)
