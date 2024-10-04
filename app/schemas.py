#Esquemas de Pydantic para validar y serializar los datos.

from pydantic import BaseModel
from datetime import date
from typing import List, Optional

# Esquema para crear una mascota (entrada)
class MascotaCreate(BaseModel):
    nombre: str
    fecha_nacimiento: date
    diagnostico: str
    peso: float
    altura: float
    fecha_ingreso: date
    tipo_sangre: str
    carnet_vacuna: bool
    tipo: str
    sexo: str
    raza: str

# Esquema para el dueño
class DueñoCreate(BaseModel):
    nombre: str
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    correo: Optional[str] = None
    contacto_emergencia: Optional[str] = None

# Esquema para devolver una mascota (salida)
class Mascota(MascotaCreate):
    id: int
    dueños: List[Optional[int]]  # IDs de los dueños relacionados

    class Config:
        orm_mode = True

# Esquema para devolver un dueño (salida)
class Dueño(DueñoCreate):
    id: int
    mascotas: List[Optional[int]]  # IDs de las mascotas relacionadas

    class Config:
        from_attributes = True
