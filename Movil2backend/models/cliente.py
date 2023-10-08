from config.db import  db, ma, app

class Cliente(db.Model):
    __tablename__ = "tblcliente"

    id = db.Column(db.Integer, primary_key =True)
    nombre_cliente = db.Column(db.String(50))
    correo_cliente = db.Column(db.String(50))
    telefono_cliente = db.Column(db.String(10))

  

with app.app_context():
    db.create_all()

class ClientesSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre_cliente ','correo_cliente','telefono_cliente')
