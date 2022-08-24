import base64
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 
import folium
from folium import IFrame
from folium.plugins import MarkerCluster
# import pandas as pd

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template ("index.html")

db = SQLAlchemy(app) ##Creamos una variable que nos permite hacer consulta a la base de datos

class Emprendimientos(db.Model):
#   __tablename__= "Registo de Emprendedoras"
  id = db.Column(db.Integer, primary_key=True)
  nombre_emp = db.Column(db.String(80), unique=True, nullable=False)
  descripcion = db.Column(db.String(200), nullable=False)
#   foto = db.Colum
  nombre = db.Column(db.String(80), nullable=False)
  apellido = db.Column(db.String(80), nullable=False)
  contacto = db.Column(db.String(10), nullable=False)
  direccion = db.Column(db.String(200), nullable=False)
  ciudad = db.Column(db.String(10), nullable=False)
  latitud = db.Column(db.Float(200), nullable=False)
  longitud = db.Column(db.Float(200), nullable=False)
  correo = db.Column(db.String(200), nullable=False)
  contrasenha = db.Column(db.String(80), nullable=False)

  def __init__(self, nombre_emp, descripcion, nombre, apellido, contacto, direccion, ciudad, latitud, longitud, correo, contrasenha):
    self.nombre_emp = nombre_emp
    self.descripcion = descripcion
    self.nombre = nombre
    self.apellido = apellido
    self.contacto = contacto
    self.direccion = direccion
    self.ciudad = ciudad
    self.latitud = latitud
    self.longitud = longitud
    self.correo = correo
    self.contrasenha = contrasenha

@app.route('/registro', methods=['GET','POST'])
def registro():
    if request.method == 'POST':
        # print(request.form['nombre_emp'])
        # nombre_emp = request.form['nombre_emp']
        nombre_emp = "pepito"
        descripcion = request.form['about']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        contacto = request.form['numero_de_telefono']
        direccion = request.form['direccion']
        ciudad = request.form['ciudad']
        latitud = request.form['latitud']
        longitud = request.form['longitud']
        correo = request.form['correo']
        contrasenha = request.form['contrasenha']


        emprendimientos = Emprendimientos(nombre_emp, descripcion, nombre, apellido, contacto, direccion, ciudad, latitud, longitud, correo, contrasenha)
        db.session.add(emprendimientos)
        db.session.commit()

    return render_template('registro.html')
    
    #luego creamos una ruta para enlistar los emprendimientos
# @app.route ('/emprendimientos')
# def emprendimientos():
# 	emprendimientos = emprendimientos.query.all() ## de la tabla emprendimientos, Hace una consulta de todos los registros en la base de datos y guarda en un objeto 
# 	return render_template('emprendimientos.html', emprendimientos=emprendimientos) ##hacemos un render de una pagina HTML y a esa pagina le vamos a agarrar al objeto de 
#    ## de Python que tenemos, le vamos a guardar en el front end


##Creamos una ruta para borrar
# @app.route('/emprendimiento/<int:id>/borrar') ##que el agarre un id de tipo entero, lo meta como argumento en la funcion
# def borrar(id):						    ##y haga un query que se llama get que sirve para obtener informacion correspondiente a este id
# 	emprendimiento = Emprendimientos.query.get(id)	##y esa info va guardar en emprendimiento
# 	db.session.delete(emprendimiento)		##despues va a hacer uso del metodo session de la base de datos (db) y del metodo delete y va borrar el contenido que nosotros obtuvimos de la base de datos db
# 	db.session.commit()				## luego hace un commit para que esos cambios se guarden
						
# 	return redirect(url_for('emprendimientos'))						##y luego hace un redireccionamiento a la URL de emprendimiento 



@app.route('/map')
def mapa():
    #Inicializamos el mapa 
#     map= folium.Map(
#         location=[-25.360106678758992, -57.63123446013285],
#         zoom_start=13,
#         )
#     # cluster = MarkerCluster().add_to(map)
# # mapa de datos
#     return map._repr_html_()

#variables de coordenadas
    coor_mapa = [-25.301379182412745, -57.58094636564712]
    # coor_1 = [-25.301379182412745, -57.58094636564712]


    #creación del mapa
    mapa = folium.Map(location=coor_mapa,zoom_start=12)

    # emprenIcon=folium.features.CustomIcon("static/mujerico.png",icon_size=(50,50))

    emprendedoras = Emprendimientos.query.all()
    for emprendedora in emprendedoras:
        folium.Marker(location=[emprendedora.latitud, emprendedora.longitud],
        popup=f'''
                <h2>{emprendedora.nombre_emp}</h2>
                <p>{emprendedora.descripcion}</p>
                <p>celular:{emprendedora.contacto}</p>


            ''').add_to(mapa)

  #se puede usar despues de la ,Icom y dentro del html se puede hacer de todo,trabaja con "boostran"
    #guardamos el mapa en un archivo html
    mapa.save('templates/map.html')

    return render_template('map.html')

@app.route("/crear_alianza")
def crear_alianza():
    return render_template ("crear_alianza.html")


@app.route("/alianzas")
def alianzas():
    return render_template ("Alianzas.html")

@app.route("/vista_mapa")
def vista_mapa():
    return render_template ("vista_mapa.html")

@app.route("/solicitud")
def solicitud():
    return render_template ("solicitud_Alian.html")


if __name__ =='__main__':
    app.run(debug=True)
    db.create_all()