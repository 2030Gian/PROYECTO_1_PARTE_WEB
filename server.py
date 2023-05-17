from flask import (
    Flask,
    render_template, 
    request, 
    )
from flask_sqlalchemy import SQLAlchemy
from flask import session, flash, redirect, url_for
import uuid;
from datetime import datetime
from sqlalchemy import LargeBinary

server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/educaweb1'
db = SQLAlchemy(server)

#Models

from sqlalchemy import func

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

    

    
class Premiun(db.Model):
    __tablename__ = "premiuns"
    id = db.Column(db.String(7), primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    contrasena = db.Column(db.String(), nullable=False)
    tarjeta_credito = db.Column(db.String())
    fecha_caducidad = db.Column(db.DateTime, default=datetime.utcnow)
    numseguridad = db.Column(db.String())
    tiempodesuscripcion = db.Column(db.Integer)

    def __init__(self, id, nombre, contrasena, tarjeta_credito, fecha_caducidad, numseguridad, tiempodesuscripcion):
        self.id = id
        self.nombre = nombre
        self.contrasena = contrasena
        self.tarjeta_credito = tarjeta_credito
        self.fecha_caducidad = fecha_caducidad
        self.numseguridad = numseguridad
        self.tiempodesuscripcion = tiempodesuscripcion



with server.app_context():
    db.create_all()

#routes
@server.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@server.route('/log', methods=['GET'])
def log():
    return render_template('login.html')

@server.route('/cursos', methods=['GET'])
def cursos():
    return render_template('cursos.html')

@server.route('/mate', methods=['GET'])
def mate():
    return render_template('mate.html')

@server.route('/comu', methods=['GET'])
def comu():
    return render_template('comu.html')

@server.route('/progra', methods=['GET'])
def progra():
    return render_template('progra.html')

@server.route('/planes', methods=['GET'])
def planes():
    return render_template('planes.html')

@server.route('/premiun', methods=['GET'])
def premiun():
    return render_template('premiun.html')

@server.route('/perfil')
def perfil():
    if 'user_id' not in session:
        flash('Debes iniciar sesión para acceder a esta página.')
        return redirect(url_for('login'))

    user_id = session['user_id']

    usuario = Student.query.get(user_id)

    if not usuario:
        flash('El usuario no existe.')
        return redirect(url_for('login'))

    return render_template('perfil.html', usuario=usuario)

@server.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        contrasena = request.form['contrasena']
        usuario = Student.query.filter_by(email=email).first()

        if usuario.contrasena == contrasena:
            #flash('¡Inicio de sesión exitoso!')

            return redirect(url_for('crear-cuenta'))

        #flash('Credenciales inválidas. Por favor, inténtalo de nuevo.')
    
    return render_template('login.html')

'''
@server.route('/ingresar', methods = ['POST'])
def login():

     user_email = request.form['email']
     user_contrasena = request.form['contrasena']
     usuario = Student.query.filter_by(email=user_email).first()
     return 'El usuario es {}'.format(usuario.name)


    #return redirect(url_for('crear-cuenta'))

'''



@server.route('/crear-cuenta', methods=['GET', 'POST'])
def crear_cuenta():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        celular = request.form['celular']
        contrasena = request.form['contrasena'] 
        universidad = request.form['universidad']
        ciclo = request.form['ciclo']
        carrera = request.form['carrera']
        fecha_nacimiento = datetime.strptime(request.form['fecha_nacimiento'], '%Y-%m-%d').date()

        usuario = Student(nombre=nombre, apellido=apellido, email=email, celular=celular, 
                          contrasena=contrasena, universidad=universidad,
                          ciclo=ciclo, carrera=carrera, fecha_nacimiento=fecha_nacimiento)
        
        db.session.add(usuario)
        db.session.commit()
        #flash('¡Cuenta creada exitosamente! Por favor, inicia sesión.')
        return redirect(url_for('ingresar'))

    return render_template('crear_cuenta.html')

@server.route('/premiun', methods=['POST'])
def premiun1():
    nombre = request.form.get('nombre')
    contrasena = request.form.get('contrasena')
    tarjeta = request.form.get('tarjeta')
    numseguridad = request.form.get('numseguridad')
    caducidad = request.form.get('caducidad')
    tiempo = request.form.get('tiempo')

    premiun = premiun1(id=str(uuid.uuid4())[:7],nombre=nombre,contrasena=contrasena,tarjeta_credito=tarjeta,fecha_caducidad=caducidad,numseguridad=numseguridad,tiempodesuscripcion=int(tiempo)
    )

    db.session.add(premiun)
    db.session.commit()
    db.session.close()
    
    return redirect('/cursos') 

# Run the app
if __name__ == '__main__':
    server.run(debug=True)
else:
    print('Importing {}'.format(__name__))    
    
    

