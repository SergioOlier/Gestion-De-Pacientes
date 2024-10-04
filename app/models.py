#Definiciones de las tablas de la base de datos usando SQLAlchemy.

from sqlalchemy import Column, Integer, String, ForeignKey, Date, DECIMAL, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class Dueño(Base):
    __tablename__ = "dueño"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    telefono = Column(String(15))
    direccion = Column(String(255))
    correo = Column(String(100))
    contacto_emergencia = Column(String(100))
    
    mascotas = relationship("DueñoMascota", back_populates="dueño")

class Mascota(Base):
    __tablename__ = "mascota"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    fecha_nacimiento = Column(Date)
    diagnostico = Column(String(255))
    peso = Column(DECIMAL(5, 2))
    altura = Column(DECIMAL(5, 2))
    fecha_ingreso = Column(Date)
    tipo_sangre = Column(String(5))
    carnet_vacuna = Column(Boolean)
    tipo = Column(String(50))
    sexo = Column(String(10))
    raza = Column(String(50))
    
    dueños = relationship("DueñoMascota", back_populates="mascota")

class DueñoMascota(Base):
    __tablename__ = "dueño_mascota"

    dueño_id = Column(Integer, ForeignKey("dueño.id"), primary_key=True)
    mascota_id = Column(Integer, ForeignKey("mascota.id"), primary_key=True)
    
    dueño = relationship("Dueño", back_populates="mascotas")
    mascota = relationship("Mascota", back_populates="dueños")
