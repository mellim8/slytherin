from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 
import folium

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


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

  def __init__(self, nombre_emp, descripcion, nombre, apellido, contacto, direccion, ciudad, latitud, longitud):
    self.nombre_emp = nombre_emp
    self.descripcion = descripcion
    self.nombre = nombre
    self.apellido = apellido
    self.contacto = contacto
    self.direccion = direccion
    self.ciudad = ciudad
    self.latitud = latitud
    self.longitud = longitud
    

@app.route('/registro', methods=['GET','POST'])
def registro():
    if request.method == 'POST':
        nombre_emp = request.form['username']
        descripcion = request.form['about']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        contacto = request.form['numero']
        direccion = request.form['direccion']
        ciudad = request.form['ciudad']
        latitud = request.form['latitud']
        longitud = request.form['longitud']

        emprendimientos = Emprendimientos(nombre_emp, descripcion, nombre, apellido, contacto, direccion, ciudad, latitud, longitud)
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



@app.route("/Mapa")
def mapa():
    popup = '<b> Nombre del emprendimiento </b>'

    lugar_del_emprendimiento = folium.Map(location=[-25.300894456479014, -57.58135401902809],zoom_start=16)

    folium.Marker(location=[-25.300894456479014, -57.58135401902809],popup = popup).add_to(lugar_del_emprendimiento)

    return lugar_del_emprendimiento._repr_html_()

    
@app.route("/Alianza")
def alianza():
    pass

if __name__ =='__main__':
    app.run(debug=True)
    db.create_all()