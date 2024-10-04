#Aquí irán las funciones CRUD para interactuar con la base de datos.

from sqlalchemy.orm import Session
from . import models, schemas

# Función para crear una mascota
def create_mascota(db: Session, mascota: schemas.MascotaCreate):
    db_mascota = models.Mascota(**mascota.dict())
    db.add(db_mascota)
    db.commit()
    db.refresh(db_mascota)
    return db_mascota

# Función para obtener una lista de mascotas
def get_mascotas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Mascota).offset(skip).limit(limit).all()

# Función para crear un dueño
def create_dueño(db: Session, dueño: schemas.DueñoCreate):
    db_dueño = models.Dueño(**dueño.dict())
    db.add(db_dueño)
    db.commit()
    db.refresh(db_dueño)
    return db_dueño

# Función para obtener una lista de dueños
def get_dueños(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Dueño).offset(skip).limit(limit).all()
