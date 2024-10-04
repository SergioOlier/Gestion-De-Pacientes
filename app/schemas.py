#Esquemas de Pydantic para validar y serializar los datos.

from pydantic import BaseModel
from datetime import date

# Esquema para crear una mascota (entrada)
class MascotaCreate(BaseModel):
    nombre: str
    nombre_dueño: str
    fecha_nacimiento: date
    diagnostico: str
    peso: float
    altura: float
    fecha_ingreso: date
    tipo_sangre: str
    carnet_vacuna: str
    tipo_sexo: str
    tipo_raza: str

# Esquema para devolver una mascota (salida)
class Mascota(BaseModel):
    id: int
    nombre: str
    nombre_dueño: str
    fecha_nacimiento: date
    diagnostico: str
    peso: float
    altura: float
    fecha_ingreso: date
    tipo_sangre: str
    carnet_vacuna: str
    tipo: str
    sexo: str
    raza: str

    class Config:
        orm_mode = True
