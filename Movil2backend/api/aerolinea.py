from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.aerolinea import Aerolinea, AerolineasSchema

ruta_Aerolinea = Blueprint("ruta_Aerolinea", __name__)

Aerolinea_schema = AerolineasSchema()
Aerolineas_schema = AerolineasSchema(many=True)

@ruta_Aerolinea.route('/Aerolineas', methods=['GET'])
def aerolinea():
    resultall = Aerolinea.query.all() 
    resultado_Aerolinea= Aerolineas_schema.dump(resultall)
    return jsonify(resultado_Aerolinea)


@ruta_Aerolinea.route("/saveaerolinea", methods=["POST"])
def save():
    nombre_aerolinea = request.json["nombre_aerolinea"]
    new_aerolinea = Aerolinea(
        nombre_aerolinea,
    )
    db.session.add(new_aerolinea)
    db.session.commit()
    return "datos guardado con exito"


@ruta_Aerolinea.route("/updateaerolinea", methods=["PUT"])
def Update():
    id = request.json["id"]
    nombre_aerolinea = request.json["nombre_aerolinea"]
    aerolinea = Aerolinea.query.get(id)
    if aerolinea:
        print(aerolinea)
        aerolinea.nombre_aerolinea= nombre_aerolinea
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"


@ruta_Aerolinea.route("/deleteaerolinea/<id>", methods=["GET"])
def eliminar(id):
    aerolinea = Aerolinea.query.get(id)
    db.session.delete(aerolinea)
    db.session.commit()
    return jsonify(
        Aerolinea_schema.dump(aerolinea),
        )