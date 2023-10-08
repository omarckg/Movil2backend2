from config.db import  db, ma, app

class Reserva(db.Model):
    __tablename__ = "tblreserva"

    id = db.Column(db.Integer, primary_key =True)
    idcliente = db.Column(db.Integer, db.ForeignKey('tblcliente.id'))
    idavion = db.Column(db.Integer, db.ForeignKey('tblAvion.id'))
    fecha_salida = db.Column(db.String(50))
    fecha_llegada = db.Column(db.String(50))
   
   
with app.app_context():
    db.create_all()

class ReservasSchema(ma.Schema):
    class Meta:
        fields = ('id','idcliente','idavion','fecha_salida','fecha_llegada')
