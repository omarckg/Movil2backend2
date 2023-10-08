from flask import Flask, jsonify,json
from config.db import  db, ma, app
from api.aeropuerto import Aeropuerto, ruta_Aeropuertos
from api.reserva import Reserva, ruta_reservas
from api.avion import Avion, ruta_Avion
from api.vuelo  import Vuelo, ruta_Vuelo
from api.aerolinea import Aerolinea, ruta_Aerolinea
from api.cliente import Cliente, ruta_clientes

app.register_blueprint(ruta_clientes,url_prefix = '/api')
app.register_blueprint(ruta_reservas, url_prefix = '/api')
app.register_blueprint(ruta_Aerolinea, url_prefix = '/api')

@app.route('/')
def index():
    return "Hola Mundo"

@app.route('/dostablas', methods=['GET'])
def dostabla():
    datos = {}
    resultado = db.session.query(Cliente, Reserva). \
        select_from(Cliente).join(Reserva).all()
    i=0
    for clientes, reservas in resultado:
        i+=1
        datos[i]={
            'cliente':clientes.nombre,
            'reserva': reservas.id, 
        }
    return datos

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')