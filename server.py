from flask import (
    Flask,
    render_template, 
    request
    )
from flask_sqlalchemy import SQLAlchemy

import uuid;
from datetime import datetime
from sqlalchemy import LargeBinary

server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/educaweb1'
db = SQLAlchemy(server)

#Models
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable = False)
    celular = db.Column(db.Integer, nullable = True)
    contrasena = db.Column(db.String(80), nullable=False)
    foto = db.Column(LargeBinary, nullable=True)
    universidad = db.Column(db.String(50), nullable = False)
    ciclo  = db.Column(db.Integer, nullable = True)
    carrera = db.Column(db.String(80), nullable = True)
    fecha_nacimiento = db.Column(db.Date(), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, nombre, apellido, universidad, fecha_nacimiento, email,contrasena, celular=None, 
                 foto=None, ciclo=None,carrera=None):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.celular = celular
        self.contrasena = contrasena
        self.foto = foto
        self.universidad = universidad
        self.ciclo = ciclo
        self.carrera = carrera
        self.fecha_nacimiento = fecha_nacimiento


class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(60), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    foto = db.Column(LargeBinary, nullable=False)
    


    def __init__(self, nombre, precio, descripcion, foto):
        self.nombre = nombre
        self.descripcion = descripcion
        self.foto = foto
      

class Controlador(db.Model):
    __tablename__ = 'controladores'
    id = db.Column(db.Integer, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    def __init__(self,fecha_creacion):
        self.fecha_creacion = fecha_creacion

      
class Premium(db.Model):
    __tablename__ = 'premium'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable = False)
    celular = db.Column(db.Integer, nullable = True)
    contrasena = db.Column(db.String(80), nullable=False)
    foto = db.Column(LargeBinary, nullable=True)
    universidad = db.Column(db.String(50), nullable = False)
    ciclo  = db.Column(db.Integer, nullable = True)
    carrera = db.Column(db.String(80), nullable = True)
    fecha_nacimiento = db.Column(db.Date(), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, nombre, apellido, universidad, fecha_nacimiento, email,contrasena, celular=None, 
                 foto=None, ciclo=None,carrera=None):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.celular = celular
        self.contrasena = contrasena
        self.foto = foto
        self.universidad = universidad
        self.ciclo = ciclo
        self.carrera = carrera
        self.fecha_nacimiento = fecha_nacimiento

class nivel(db.Model):
    __tablename__ = 'niveles'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable = False)
    celular = db.Column(db.Integer, nullable = True)
    contrasena = db.Column(db.String(80), nullable=False)
    foto = db.Column(LargeBinary, nullable=True)
    universidad = db.Column(db.String(50), nullable = False)
    ciclo  = db.Column(db.Integer, nullable = True)
    carrera = db.Column(db.String(80), nullable = True)
    fecha_nacimiento = db.Column(db.Date(), nullable=False)
    nivel = db.Column(db.String(10), nullable = False)
    curso = db.Column(db.String(80), nullable = False)
    promedio = db.Column(db.Float, nullable = False)
    aprobado = db.Column(db.Boolean, default = False)

    def __init__(self, nombre, apellido, universidad, fecha_nacimiento, email,contrasena, 
                 curso,nivel,promedio,aprobado,celular=None,foto=None, ciclo=None,carrera=None):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.celular = celular
        self.contrasena = contrasena
        self.foto = foto
        self.universidad = universidad
        self.ciclo = ciclo
        self.carrera = carrera
        self.fecha_nacimiento = fecha_nacimiento
        self.nivel = nivel
        self.curso = curso
        self.promedio = promedio
        self.aprobado = aprobado



class examen(db.Model):
    __tablename__ = 'examenes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(60), nullable=False)
    nota = db.Column(db.Float, nullable = False)

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

with server.app_context():
    db.create_all()

#routes
@server.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@server.route('/login', methods=['GET'])
def login():
    usuarios_registrado = Student.query.filter()
    return render_template('login.html')

@server.route('/crear-cuenta', methods=['GET', 'POST'])
def crear_cuenta():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        celular = request.form['celular']
        contrasena = request.form['contrasena']  # Updated argument name
        #foto = request.form['foto']
        universidad = request.form['universidad']
        ciclo = request.form['ciclo']
        carrera = request.form['carrera']
        fecha_nacimiento = datetime.strptime(request.form['fecha_nacimiento'], '%Y-%m-%d').date()

        usuario = Student(nombre=nombre, apellido=apellido, email=email, celular=celular, 
                          contrasena=contrasena, universidad=universidad,
                          ciclo=ciclo, carrera=carrera, fecha_nacimiento=fecha_nacimiento)
        
        db.session.add(usuario)
        db.session.commit()
    return render_template('crear_cuenta.html')





# Run the app
if __name__ == '__main__':
    server.run(debug=True)
else:
    print('Importing {}'.format(__name__))    
    
    


