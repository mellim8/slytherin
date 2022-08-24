import base64
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 
import folium
from folium import IFrame
from folium.plugins import MarkerCluster
# import pandas as pd

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/db.sqlite3'
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
  rubro = db.Column(db.String(200), nullable=False)
  ciudad = db.Column(db.String(10), nullable=False)
  latitud = db.Column(db.Float(200), nullable=False)
  longitud = db.Column(db.Float(200), nullable=False)
  correo = db.Column(db.String(200), nullable=False)
  contrasenha = db.Column(db.String(80), nullable=False)

  def __init__(self, nombre_emp, descripcion, nombre, apellido, contacto, direccion, rubro, ciudad, latitud, longitud, correo, contrasenha):
    self.nombre_emp = nombre_emp
    self.descripcion = descripcion
    self.nombre = nombre
    self.apellido = apellido
    self.contacto = contacto
    self.direccion = direccion
    self.rubro = rubro
    self.ciudad = ciudad
    self.latitud = latitud
    self.longitud = longitud
    self.correo = correo
    self.contrasenha = contrasenha

@app.route('/registro', methods=['GET','POST'])
def registro():
    if request.method == 'POST':
        nombre_emp = request.form['nombre_emp']
        descripcion = request.form['about']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        contacto = request.form['numero_de_telefono']
        direccion = request.form['direccion']
        rubro = request.form['rubro']
        ciudad = request.form['ciudad']
        latitud = request.form['latitud']
        longitud = request.form['longitud']
        correo = request.form['correo']
        contrasenha = request.form['contrasenha']


        emprendimientos = Emprendimientos(nombre_emp, descripcion, nombre, apellido, contacto, direccion, rubro, ciudad, latitud, longitud, correo, contrasenha)
        db.session.add(emprendimientos)
        db.session.commit()

    return render_template('registro.html')
    
    #luego creamos una ruta para enlistar los emprendimientos
@app.route ('/emprendimientos')
def emprendimientos():
	emprendimientos = Emprendimientos.query.all() ## de la tabla emprendimeintos, Hace una consulta de todos los registros en la base de datos y guarda en un objeto 
	return render_template('emprendimientos.html', emprendimientos=emprendimientos) ##hacemos un render de una pagina HTML y a esa pagina le vamos a agarrar al objeto de 
   ## de Python que tenemos, le vamos a guardar en el front end


##Creamos una ruta para borrar
# @app.route('/emprendimiento/<int:id>/borrar') ##que el agarre un id de tipo entero, lo meta como argumento en la funcion
# def borrar(id):						    ##y haga un query que se llama get que sirve para obtener informacion correspondiente a este id
# 	emprendimiento = Emprendimientos.query.get(id)	##y esa info va guardar en emprendimiento
# 	db.session.delete(emprendimiento)		##despues va a hacer uso del metodo session de la base de datos (db) y del metodo delete y va borrar el contenido que nosotros obtuvimos de la base de datos db
# 	db.session.commit()				## luego hace un commit para que esos cambios se guarden
						
# 	return redirect(url_for('emprendimientos'))						##y luego hace un redireccionamiento a la URL de emprendimiento 



@app.route('/Belleza')
def mapa_belleza():
    coor_mapa = [-25.301379182412745, -57.58094636564712]
    coor_1 = [-25.301379182412745, -57.58094636564712]


    #creación del mapa
    mapa = folium.Map(location=coor_mapa,zoom_start=18)

    # emprenIcon=folium.features.CustomIcon("static/mujerico.png",icon_size=(50,50))

    emprendedoras = Emprendimientos.query.all()
    for emprendedora in emprendedoras:
        if emprendedora.rubro =="Belleza":
            folium.Marker(location=[emprendedora.latitud, emprendedora.longitud],
            popup=f'''
                    <h2>{emprendedora.nombre_emp} </h2>
                    <p>{emprendedora.descripcion}</p>
                    <a href="https://wa.me/595{emprendedora.contacto}/?" target="_blank">
                        <img src="logo-wasap.png" width="50" height="50">
                    </a>
                ''').add_to(mapa)

    mapa.save('templates/Belleza.html')
    return render_template('Belleza.html')

@app.route('/Gastronomia')
def mapa_Gastronomia():
    coor_mapa = [-25.301379182412745, -57.58094636564712]
    coor_1 = [-25.301379182412745, -57.58094636564712]


    #creación del mapa
    mapa = folium.Map(location=coor_mapa,zoom_start=18)

    # emprenIcon=folium.features.CustomIcon("static/mujerico.png",icon_size=(50,50))

    emprendedoras = Emprendimientos.query.all()
    for emprendedora in emprendedoras:
        if emprendedora.rubro =="Gastronomia":
            folium.Marker(location=[emprendedora.latitud, emprendedora.longitud],
            popup=f'''
                    <h2>{emprendedora.nombre_emp} </h2>
                    <p>{emprendedora.descripcion}</p>
                    <a href="https://wa.me/595{emprendedora.contacto}/?" target="_blank">
                        <img src="logo-wasap.png" width="50" height="50">
                    </a>
                ''').add_to(mapa)

    mapa.save('templates/Gastronomia.html')
    return render_template('Gastronomia.html')

@app.route('/Artesanias')
def mapa_Artesanias():
    coor_mapa = [-25.301379182412745, -57.58094636564712]
    coor_1 = [-25.301379182412745, -57.58094636564712]


    #creación del mapa
    mapa = folium.Map(location=coor_mapa,zoom_start=18)

    # emprenIcon=folium.features.CustomIcon("static/mujerico.png",icon_size=(50,50))

    emprendedoras = Emprendimientos.query.all()
    for emprendedora in emprendedoras:
        if emprendedora.rubro =="Artesanias":
            folium.Marker(location=[emprendedora.latitud, emprendedora.longitud],
            popup=f'''
                    <h2>{emprendedora.nombre_emp} </h2>
                    <p>{emprendedora.descripcion}</p>
                    <a href="https://wa.me/595{emprendedora.contacto}/?" target="_blank">
                        <img src="logo-wasap.png" width="50" height="50">
                    </a>
                ''').add_to(mapa)

    mapa.save('templates/Artesanias.html')
    return render_template('Artesanias.html')

@app.route('/Prendas_de_vestir')
def mapa_Prendas_de_vestir():
    coor_mapa = [-25.301379182412745, -57.58094636564712]
    coor_1 = [-25.301379182412745, -57.58094636564712]


    #creación del mapa
    mapa = folium.Map(location=coor_mapa,zoom_start=18)

    # emprenIcon=folium.features.CustomIcon("static/mujerico.png",icon_size=(50,50))

    emprendedoras = Emprendimientos.query.all()
    for emprendedora in emprendedoras:
        if emprendedora.rubro =="Prendas_de_vestir":
            folium.Marker(location=[emprendedora.latitud, emprendedora.longitud],
            popup=f'''
                    <h2>{emprendedora.nombre_emp} </h2>
                    <p>{emprendedora.descripcion}</p>
                    <a href="https://wa.me/595{emprendedora.contacto}/?" target="_blank">
                        <img src="logo-wasap.png" width="50" height="50">
                    </a>
                ''').add_to(mapa)

    mapa.save('templates/Prendas_de_vestir.html')
    return render_template('Prendas_de_vestir.html')

@app.route('/Cuidado_de_ancianos')
def mapa_Cuidado_de_ancianos():
    coor_mapa = [-25.301379182412745, -57.58094636564712]
    coor_1 = [-25.301379182412745, -57.58094636564712]


    #creación del mapa
    mapa = folium.Map(location=coor_mapa,zoom_start=18)

    # emprenIcon=folium.features.CustomIcon("static/mujerico.png",icon_size=(50,50))

    emprendedoras = Emprendimientos.query.all()
    for emprendedora in emprendedoras:
        if emprendedora.rubro =="Cuidado_de_ancianos":
            folium.Marker(location=[emprendedora.latitud, emprendedora.longitud],
            popup=f'''
                    <h2>{emprendedora.nombre_emp} </h2>
                    <p>{emprendedora.descripcion}</p>
                    <a href="https://wa.me/595{emprendedora.contacto}/?" target="_blank">
                        <img src="logo-wasap.png" width="50" height="50">
                    </a>
                ''').add_to(mapa)

    mapa.save('templates/Cuidado_de_ancianos.html')
    return render_template('Cuidado_de_ancianos.html')

@app.route('/Trabajo_domestico')
def mapa_Trabajo_domestico():
    coor_mapa = [-25.301379182412745, -57.58094636564712]
    coor_1 = [-25.301379182412745, -57.58094636564712]


    #creación del mapa
    mapa = folium.Map(location=coor_mapa,zoom_start=18)

    # emprenIcon=folium.features.CustomIcon("static/mujerico.png",icon_size=(50,50))

    emprendedoras = Emprendimientos.query.all()
    for emprendedora in emprendedoras:
        if emprendedora.rubro =="Trabajo_domestico":
            folium.Marker(location=[emprendedora.latitud, emprendedora.longitud],
            popup=f'''
                    <h2>{emprendedora.nombre_emp} </h2>
                    <p>{emprendedora.descripcion}</p>
                    <a href="https://wa.me/595{emprendedora.contacto}/?" target="_blank">
                        <img src="logo-wasap.png" width="50" height="50">
                    </a>
                ''').add_to(mapa)

    mapa.save('templates/Trabajo_domestico.html')
    return render_template('Trabajo_domestico.html')

@app.route('/Educacion')
def mapa_Educacion():
    coor_mapa = [-25.301379182412745, -57.58094636564712]
    coor_1 = [-25.301379182412745, -57.58094636564712]


    #creación del mapa
    mapa = folium.Map(location=coor_mapa,zoom_start=18)

    # emprenIcon=folium.features.CustomIcon("static/mujerico.png",icon_size=(50,50))

    emprendedoras = Emprendimientos.query.all()
    for emprendedora in emprendedoras:
        if emprendedora.rubro =="Educacion":
            folium.Marker(location=[emprendedora.latitud, emprendedora.longitud],
            popup=f'''
                    <h2>{emprendedora.nombre_emp} </h2>
                    <p>{emprendedora.descripcion}</p>
                   <a href="https://wa.me/595{emprendedora.contacto}/?" target="_blank">
                        <img src="logo-wasap.png" width="50" height="50">
                    </a>
                ''').add_to(mapa)

    mapa.save('templates/Educacion.html')
    return render_template('Educacion.html')

@app.route('/Cuidado_de_ninhos')
def mapa_Cuidado_de_ninhos():
    coor_mapa = [-25.301379182412745, -57.58094636564712]
    coor_1 = [-25.301379182412745, -57.58094636564712]


    #creación del mapa
    mapa = folium.Map(location=coor_mapa,zoom_start=18)

    # emprenIcon=folium.features.CustomIcon("static/mujerico.png",icon_size=(50,50))

    emprendedoras = Emprendimientos.query.all()
    for emprendedora in emprendedoras:
        if emprendedora.rubro =="Cuidado_de_ninhos":
            folium.Marker(location=[emprendedora.latitud, emprendedora.longitud],
            popup=f'''
                    <h2>{emprendedora.nombre_emp} </h2>
                    <p>{emprendedora.descripcion}</p>
                    <a href="https://wa.me/595{emprendedora.contacto}/?" target="_blank">
                        <img src="logo-wasap.png" width="50" height="50">
                    </a>
                ''').add_to(mapa)

    mapa.save('templates/Cuidado_de_ninhos.html')
    return render_template('Cuidado_de_ninhos.html')

@app.route('/Decoracion')
def mapa_Decoracion():
    coor_mapa = [-25.301379182412745, -57.58094636564712]
    coor_1 = [-25.301379182412745, -57.58094636564712]


    #creación del mapa
    mapa = folium.Map(location=coor_mapa,zoom_start=18)

    # emprenIcon=folium.features.CustomIcon("static/mujerico.png",icon_size=(50,50))

    emprendedoras = Emprendimientos.query.all()
    for emprendedora in emprendedoras:
        if emprendedora.rubro =="Decoracion":
            folium.Marker(location=[emprendedora.latitud, emprendedora.longitud],
            popup=f'''
                    <h2>{emprendedora.nombre_emp} </h2>
                    <p>{emprendedora.descripcion}</p>
                    <a href="https://wa.me/595{emprendedora.contacto}/?" target="_blank">
                        <img src="logo-wasap.png" width="50" height="50">
                    </a>
                ''').add_to(mapa)

    mapa.save('templates/Decoracion.html')
    return render_template('Decoracion.html')

@app.route('/Floricultura')
def mapa_Floricultura():
    coor_mapa = [-25.301379182412745, -57.58094636564712]
    coor_1 = [-25.301379182412745, -57.58094636564712]


    #creación del mapa
    mapa = folium.Map(location=coor_mapa,zoom_start=18)

    # emprenIcon=folium.features.CustomIcon("static/mujerico.png",icon_size=(50,50))

    emprendedoras = Emprendimientos.query.all()
    for emprendedora in emprendedoras:
        if emprendedora.rubro =="Floricultura":
            folium.Marker(location=[emprendedora.latitud, emprendedora.longitud],
            popup=f'''
                    <h2>{emprendedora.nombre_emp} </h2>
                    <p>{emprendedora.descripcion}</p>
                    <a href="https://wa.me/595{emprendedora.contacto}/?" target="_blank">
                        <img src="logo-wasap.png" width="50" height="50">
                    </a>
                ''').add_to(mapa)

    mapa.save('templates/Floricultura.html')
    return render_template('Floricultura.html')

@app.route("/crear_alianza")
def crear_alianza():
    return render_template ("crear_alianza.html")

@app.route("/alianzas")
def alianzas():
    return render_template ("Alianzas.html")

@app.route("/vista_mapa")
def vista_mapa():
    return render_template ("vista_mapa.html")



if __name__ =='__main__':
    app.run(debug=True)
    db.create_all()