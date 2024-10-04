from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#La URL de conexión de MariaDB
SQLALCHEMY_DATABASE_URL = "mariadb+mariadbconnector://root:1234@localhost:3306/veterinaria"

#Para crear el motor de base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#Para crear una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base de modelos de SQLAlchemy
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# Verificar conexión
"""
def verify_connection():
    try:
        # Intentar conectarse a la base de datos
        with engine.connect() as connection:
            print("Conexión a la base de datos exitosa")
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

# Testear la conexión directamente
if __name__ == "__main__":
    verify_connection()
"""
