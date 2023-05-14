from flask import (
    Flask,
    render_template, 
    )
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid;
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hp:1234@localhost:5432/educaweb1'
db = SQLAlchemy(app)

#Models

from sqlalchemy import func

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.String(36), nullable=False, default=lambda: str(uuid.uuid4()), primary_key=True)
    nombre = db.Column(db.String(), nullable=False)
    apellido = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    contraseña = db.Column(db.String(), nullable=False)
    foto = db.Column(db.String(), nullable=True)
    fecha_nacimiento = db.Column(db.Date(), nullable=True)
    biografia = db.Column(db.String(), nullable=True)
    intereses = db.Column(db.String(), nullable=True)
    created_at = db.Column(db.DateTime, default=func.now())

    def __init__(self, nombre, apellido, email, contraseña, foto=None, fecha_nacimiento=None, biografia=None, intereses=None):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña
        self.foto = foto
        self.fecha_nacimiento = fecha_nacimiento
        self.biografia = biografia
        self.intereses = intereses

    def __repr__(self):
        return f"Usuario(id={self.id}, nombre={self.nombre}, apellido={self.apellido})"


class Cursos(db.Model):
    __tablename__ = 'Curso'
    id = db.Column(db.String(7), primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    descripcion = db.Column(db.String(500), nullable=False)
    foto = db.Column(db.String(500), nullable=True)
    cupos_disponibles = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)


    def __init__(self, nombre, precio, descripcion, foto, cupos_disponibles):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.foto = foto
        self.cupos_disponibles = cupos_disponibles

    def __repr__(self):
        return f"Cursos(id={self.id}, nombre={self.nombre}, precio={self.precio})"

    
class Premium(Usuario):
    __tablename__ = 'premium'
    __mapper_args__ = {
        'polymorphic_identity': 'miembro_pay',
    }
    def __init__(self, name, lastname, nickname, fecha_de_nacimiento, codeforces_handle, atcoder_handle, vjudge_handle):
        super().__init__(name, lastname, nickname, fecha_de_nacimiento, codeforces_handle, atcoder_handle, vjudge_handle)

class Freemium(Usuario):
    __tablename__ = 'freemium'
    __mapper_args__ = {
        'polymorphic_identity': 'miembro_free',
    }
    def __init__(self, name, lastname, nickname, fecha_de_nacimiento, codeforces_handle, atcoder_handle, vjudge_handle):
        super().__init__(name, lastname, nickname, fecha_de_nacimiento, codeforces_handle, atcoder_handle, vjudge_handle)

with app.app_context():
    db.create_all()
        
#routes
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
else:
    print('Importing {}'.format(__name__))    
    
    


