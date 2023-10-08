from config.db import  db, ma, app

class Avion(db.Model):
    __tablename__ = "tblAvion"

    id = db.Column(db.Integer, primary_key =True)
    id_aerolinea = db.Column(db.Integer, db.ForeignKey('tblAerolinea.id'))
    modelo_avion = db.Column(db.String(50))

    def __init__(self, nombre_aerolinea) :
       self.nombre_aerolinea = nombre_aerolinea
       
with app.app_context():
    db.create_all()

class AvionesSchema(ma.Schema):
    class Meta:
        fields = ('id','id_aerolinea','modelo_avion')