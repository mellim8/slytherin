from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import folium

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/")

def index():
    return render_template ("index.html")


class Emprendimientos(db.Model):
#   __tablename__= "Registo de Emprendedoras"
  id = db.Column(db.Integer, primary_key=True)
  nombre_emp = db.Column(db.String(80), unique=True, nullable=False)
  descripcion = db.Column(db.String(200), nullable=False)
  foto = db.Colum
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
        nombre = request.form['first-name']
        apellido = request.form['last-name']
        contacto = request.form['email']
        direccion = request.form['street-address']
        ciudad = request.form['city']
        latitud = request.form['latitud']
        longitud = request.form['longitud']      

        emprendimientos = Emprendimientos(nombre_emp, descripcion, nombre, apellido, contacto, direccion, ciudad, latitud, longitud)
        db.session.add(emprendimientos)
        db.session.commit()

    return render_template('registro.html')
    
if __name__ =='__main__':
    app.run(debug=True)
    db.create_all()

@app.route("/Mapa")
def mapa():
    popup = '<b> Nombre del emprendimiento </b>'

    lugar_del_emprendimiento = folium.Map(location=[-25.300894456479014, -57.58135401902809],zoom_start=16)

    folium.Marker(location=[-25.300894456479014, -57.58135401902809],popup = popup).add_to(lugar_del_emprendimiento)

    return lugar_del_emprendimiento._repr_html_()

    
@app.route("/Alianza")
def alianza():

