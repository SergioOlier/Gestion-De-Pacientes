#Las rutas para manejar las peticiones relacionadas a dueños

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Dueño)
def create_dueño(dueño: schemas.DueñoCreate, db: Session = Depends(get_db)):
    return crud.create_dueño(db=db, dueño=dueño)

@router.get("/", response_model=list[schemas.Dueño])
def read_dueños(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_dueños(db, skip=skip, limit=limit)

@router.get("/{dueño_id}", response_model=schemas.Dueño)
def read_dueño(dueño_id: int, db: Session = Depends(get_db)):
    db_dueño = crud.get_dueño(db, dueño_id)
    if db_dueño is None:
        raise HTTPException(status_code=404, detail="Dueño no encontrado")
    return db_dueño
