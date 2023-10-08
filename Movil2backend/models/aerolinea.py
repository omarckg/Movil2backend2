from config.db import  db, ma, app

class Aerolinea(db.Model):
    __tablename__ = "tblAerolinea"

    id = db.Column(db.Integer, primary_key =True)
    nombre_aerolinea = db.Column(db.String(50))

    def __init__(self, nombre_aerolinea) :
       self.nombre_aerolinea = nombre_aerolinea
       
with app.app_context():
    db.create_all()

class AerolineasSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre_aerolinea')