from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.aeropuerto import Aeropuerto, AeropuertosSchema

ruta_Aeropuertos = Blueprint("ruta_Aeropuerto", __name__)

Aeropuerto_schema = AeropuertosSchema()
Aeropuertos_schema = AeropuertosSchema(many=True)

@ruta_Aeropuertos.route('/Aeropuertos', methods=['GET'])
def aeropuerto():
    resultall =  Aeropuerto.query.all() #Select * from Clientes
    resultado_Aeropuerto = Aeropuertos_schema.dump(resultall)
    return jsonify(resultado_Aeropuerto)

@ruta_Aeropuertos.route("/saveaeropuerto", methods=["POST"])
def save():
    nombre_aeropuerto = request.json["nombre_aeropuerto"]
    ciudad = request.json["ciudad"]
    pais = request.json["pais"]
    new_aeropuerto = Aeropuerto(
        nombre_aeropuerto,
        ciudad,
        pais,
    )
    db.session.add(new_aeropuerto)
    db.session.commit()
    return "datos guardado con exito"


@ruta_Aeropuertos.route("/updateaeropuerto", methods=["PUT"])
def Update():
    id = request.json["id"]
    nombre_aeropuerto = request.json["nombre_aeropuerto"]
    ciudad = request.json["ciudad"]
    pais = request.json["pais"]
    aeropuerto = Aeropuerto.query.get(id)
    if aeropuerto:
        print(aeropuerto)
        aeropuerto.nombre_aeropuerto =  nombre_aeropuerto
        aeropuerto.ciudad = ciudad
        aeropuerto.pais = pais
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"


@ruta_Aeropuertos.route("/deleteaeropuerto/<id>", methods=["GET"])
def eliminar(id):
    aeropuerto = Aeropuerto.query.get(id)
    db.session.delete(aeropuerto)
    db.session.commit()
    return jsonify(
        Aeropuerto_schema.dump(aeropuerto),
        )