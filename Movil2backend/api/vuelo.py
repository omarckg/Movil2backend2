from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.vuelo import Vuelo,  VuelosSchema

ruta_Vuelo = Blueprint("ruta_Vuelo", __name__)

Vuelo_schema =  VuelosSchema()
Vuelos_schema =  VuelosSchema(many=True)

@ruta_Vuelo.route('/Vuelos', methods=['GET'])
def vuelo():
    resultall = Vuelo.query.all() #Select * from Clientes
    resultado_Vuelo=  Vuelos_schema.dump(resultall)
    return jsonify(resultado_Vuelo)



@ruta_Vuelo.route("/savevuelo", methods=["POST"])
def save():
    idreserva = request.json["idreserva"]
    idavion= request.json["idavion"]
    idaeropuerto = request.json["idaeropuerto"]
    new_vuelo = Vuelo(
        idreserva,
        idavion,
        idaeropuerto,
    )
    db.session.add(new_vuelo)
    db.session.commit()
    return "datos guardado con exito"


@ruta_Vuelo.route("/updatevuelo", methods=["PUT"])
def Update():
    id = request.json["id"]
    idreserva = request.json["nombre_aeropuerto"]
    idavion = request.json["ciudad"]
    idaeropuerto = request.json["pais"]
    vuelo = Vuelo.query.get(id)
    if vuelo:
        print(vuelo)
        vuelo.idreserva = idreserva
        vuelo.idavion = idavion
        vuelo.idaeropuerto = idaeropuerto
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"


@ruta_Vuelo.route("/deleteaeropuerto/<id>", methods=["GET"])
def eliminar(id):
    vuelo = Vuelo.query.get(id)
    db.session.delete(vuelo)
    db.session.commit()
    return jsonify(
        Vuelo_schema.dump(Vuelo),
        )