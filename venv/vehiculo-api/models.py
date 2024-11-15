from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

# Modelo Vehiculo
class Vehiculo(db.Model):
    placa = db.Column(db.String(10), primary_key=True)
    color = db.Column(db.String(20), nullable=False)
    modelo = db.Column(db.String(20), nullable=False)
    marca = db.Column(db.String(20), nullable=False)

# Esquema para la serialización
class VehiculoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Vehiculo
        load_instance = True
