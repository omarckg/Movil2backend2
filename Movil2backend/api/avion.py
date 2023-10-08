from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.avion import Avion, AvionesSchema

ruta_Avion = Blueprint("ruta_Avion", __name__)

Avion_schema = AvionesSchema()
Aviones_schema = AvionesSchema(many=True)

@ruta_Avion.route('/Aviones', methods=['GET'])
def avion():
    resultall = Avion.query.all() #Select * from Clientes
    resultado_Avion= Aviones_schema.dump(resultall)
    return jsonify(resultado_Avion)

@ruta_Avion.route("/savecliente", methods=["POST"])
def save():
    id_aerolinea = request.json["id_aerolinea"]
    modelo_avion = request.json["modelo_avion"]
    new_avion = Avion(
        modelo_avion,
        id_aerolinea,
    )
    db.session.add(new_avion)
    db.session.commit()
    return "datos guardado con exito"

@ruta_Avion.route("/updatecliente", methods=["PUT"])
def Update():
    id = request.json["id"]
    id_aerolinea = request.json["nombre"]
    modelo_avion= request.json["correo"]
    avion = Avion.query.get(id)
    if avion:
        print(avion)
        avion.id_aerolinea = id_aerolinea
        avion.modelo_avion = modelo_avion
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"
    
@ruta_Avion.route("/deletecliente/<id>", methods=["GET"])
def eliminar(id):
    avion = Avion.query.get(id)
    db.session.delete(avion)
    db.session.commit()
    return jsonify(
        Avion_schema.dump(avion),
    )