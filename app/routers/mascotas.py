#Las rutas para manejar las peticiones relacionadas a mascotas

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Mascota)
def create_mascota(mascota: schemas.MascotaCreate, db: Session = Depends(get_db)):
    return crud.create_mascota(db=db, mascota=mascota)

@router.get("/", response_model=list[schemas.Mascota])
def read_mascotas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_mascotas(db, skip=skip, limit=limit)

@router.get("/{mascota_id}", response_model=schemas.Mascota)
def read_mascota(mascota_id: int, db: Session = Depends(get_db)):
    db_mascota = crud.get_mascota(db, mascota_id)
    if db_mascota is None:
        raise HTTPException(status_code=404, detail="Mascota no encontrada")
    return db_mascota
