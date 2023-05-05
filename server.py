from flask import (
    Flask, 
    )
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid;

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/'
db = SQLAlchemy(app)

#Models

class Cursos(db.Model):
    __tablename__ = 'Curso'
    id = db.Column(db.String(7), nullable=False, default=lambda: str(uuid.uuid4()), server_default=db.text("uuid_generate_v4()"))
    nombre = db.Column(db.String(30), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    descripcion = db.Column(db.String(500), nullable=False)
    foto = db.Column(db.String(500), nullable=True)
    cupos_disponibles = db.Column(db.Integer, nullable=False)

    def __init__(self, nombre, precio, descripcion, foto, cupos_disponibles):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.foto = foto
        self.cupos_disponibles = cupos_disponibles


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
else:
    print('Importing {}'.format(__name__))    
