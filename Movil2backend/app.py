from flask import Flask, jsonify,json
from config.db import  db, ma, app
from api.cliente import Cliente, ruta_clientes
from api.aerolinea import Aerolinea, ruta_Aerolinea
from api.avion import Avion, ruta_Avion
from api.aeropuerto import Aeropuerto, ruta_Aeropuertos
from api.reserva import Reserva, ruta_reservas
from api.vuelo  import Vuelo, ruta_Vuelo

app.register_blueprint(ruta_clientes,url_prefix = '/api')
app.register_blueprint(ruta_reservas, url_prefix = '/api')
app.register_blueprint(ruta_Aerolinea, url_prefix = '/api')
app.register_blueprint(ruta_Vuelo, url_prefix = '/api')
app.register_blueprint(ruta_Aeropuertos, url_prefix = '/api')

app.register_blueprint(ruta_Avion, url_prefix = '/api')

@app.route('/')
def index():
    return "Hola Mundo"

@app.route('/dostablas', methods=['POST'])
def dostabla():
    datos = {}
    resultado = db.session.query(Cliente,Reserva). \
        select_from(Cliente).join(Reserva).all()
    i=0
    for clientes, reservas in resultado:
        i+=1
        datos[i]={
            'cliente':clientes.nombre,
            'reserva': reservas.id, 
        }
    return datos

@app.route('/dostablas1', methods=['POST'])
def dostabla1():
    datos = {}
    resultado = db.session.query(Aerolinea,Avion). \
        select_from(Aerolinea).join(Avion).all()
    i=0
    for aerolinea,avion in resultado:
        i+=1
        datos[i]={
            'aerolinea':aerolinea.nombre,
            'avion':avion.id,
        }
    return datos

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')