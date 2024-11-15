from flask import Flask, request, jsonify
from models import db, ma, Vehiculo, VehiculoSchema
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
ma.init_app(app)

vehiculo_schema = VehiculoSchema()
vehiculos_schema = VehiculoSchema(many=True)

@app.route('/')
def index():
    return jsonify({"message": "Bienvenido a la API de Vehículos"}), 200


# Crear base de datos
@app.before_first_request
def create_tables():
    db.create_all()

# Rutas CRUD
@app.route('/vehiculos', methods=['POST'])
def create_vehiculo():
    data = request.get_json()
    vehiculo = Vehiculo(**data)
    db.session.add(vehiculo)
    db.session.commit()
    return vehiculo_schema.jsonify(vehiculo), 201

@app.route('/vehiculos', methods=['GET'])
def get_vehiculos():
    vehiculos = Vehiculo.query.all()
    return vehiculos_schema.jsonify(vehiculos)

@app.route('/vehiculos/<placa>', methods=['GET'])
def get_vehiculo(placa):
    vehiculo = Vehiculo.query.get_or_404(placa)
    return vehiculo_schema.jsonify(vehiculo)

@app.route('/vehiculos/<placa>', methods=['PUT'])
def update_vehiculo(placa):
    vehiculo = Vehiculo.query.get_or_404(placa)
    data = request.get_json()
    for key, value in data.items():
        setattr(vehiculo, key, value)
    db.session.commit()
    return vehiculo_schema.jsonify(vehiculo)

@app.route('/vehiculos/<placa>', methods=['DELETE'])
def delete_vehiculo(placa):
    vehiculo = Vehiculo.query.get_or_404(placa)
    db.session.delete(vehiculo)
    db.session.commit()
    return jsonify({"message": "Vehículo eliminado"}), 200

if __name__ == '__main__':
    app.run(debug=True)
