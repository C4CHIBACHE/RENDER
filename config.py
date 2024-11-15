import os

# Configuración de la base de datos
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///vehiculo.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
