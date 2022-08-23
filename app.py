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
    id = db.Column(db.Integer, primary_key=True)
    nombre_del_emprendimiento = db.Column(db.String(80), unique=True, nullable=False)
    encargada = db.Column(db.String(200), nullable=False)
    correo = db.Column(db.String(10), nullable=False)
    contacto = db.Column(db.Float(200), nullable=False)
    latitud = db.Column(db.Float(200), nullable=False)
    longitud = db.Column(db.Float(200), nullable=False)
    ciudad = db.Column(db.String(10), nullable=False)
    servicio_o_producto = db.Column(db.String(200), nullable=False)
    rubro = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.String(500), nullable=False)

    def __init__(self, nombre_del_emprendimiento, encargada, correo, contacto, latitud, longitud, ciudad,   servicio_o_producto, rubro,descripcion):
        self.nombre_del_emprendimiento = nombre_del_emprendimiento
        self.encargada = encargada
        self.correo = correo
        self.contacto = contacto
        self.latitud = latitud
        self.longitud = longitud
        self.ciudad = ciudad
        self.servicio_o_producto = servicio_o_producto
        self.rubro = rubro
        self.descripcion = descripcion

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre_del_emprendimiento = request.form['nombre_del_emprendimiento']
        encargada = request.form['encargada']
        correo = request.form ['correo']
        contacto = request.form['contacto']
        latitud = request.form['latitud']
        longitud = request.form['longitud']
        ciudad = request.form['ciudad']
        servicio_o_producto = request.form['servicio_o_producto']
        rubro = request.form['rubro']
        descripcion = request.form['descripcion']

        emprendimiento = Emprendimientos (nombre_del_emprendimiento, encargada, correo, contacto, latitud, longitud, ciudad,  servicio_o_producto, rubro, descripcion)      ##creamos una variable u objeto
        db.session.add(emprendimiento) 		##por medio del session.add agarramos el objeto emprendimiento
        db.session.commit(emprendimiento)	## y luego commiteamos para que se aguarde en la base de datos
 
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


if __name__ =='app':
    app.run(debug=True)
    db.create_all()