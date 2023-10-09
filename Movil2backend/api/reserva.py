from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.reserva import Reserva, ReservasSchema
from models.cliente import Cliente, ClientesSchema

ruta_reservas = Blueprint("ruta_reserva", __name__)

reserva_schema = ReservasSchema()
reservas_schema = ReservasSchema(many=True)

@ruta_reservas.route('/reservas', methods=['GET'])
def reserva():
    resultall = Reserva.query.all() #Select * from Clientes
    resultado_reserva= reservas_schema.dump(resultall)
    return jsonify(resultado_reserva)


@ruta_reservas.route('/saveReserva', methods=['POST'])
def save():
    idcliente = request.json["idcliente"]
    idavion = request.json["idavion"]
    fecha_salida = request.json["fecha_salida"]
    fecha_llegada = request.json["fecha_llegada"]
    new_reserva = Reserva(
        idcliente,
        idavion,
        fecha_salida,
        fecha_llegada,
    )
    db.session.add(new_reserva)
    db.session.commit()
    return "datos guardado con exito"


@ruta_reservas.route('/deleteReserva/<int:id>', methods=['DELETE'])
def eliminar(id):
    reserva = Reserva.query.get(id)
    db.session.delete(reserva)
    db.session.commit()
    return "datos eliminado con exito"

@ruta_reservas.route('/updateReserva/<int:id>', methods=['PUT'])
def update():
    id = request.json["id"]
    idcliente = request.json["idcliente"]
    idavion = request.json["idavion"]
    fecha_salida = request.json["fecha_salida"]
    fecha_llegada = request.json["fecha_llegada"]
    reserva = Reserva.query.get(id)
    if reserva:
        print(reserva)
        reserva.idcliente = idcliente
        reserva.idavion = idavion
        reserva.fecha_salida = fecha_salida
        reserva.fecha_llegada = fecha_llegada
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"
