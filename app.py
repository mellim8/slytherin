from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import folium

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/")

def index():
    return render_template ("index.html")

db = SQLAlchemy(app)

class Emprendimientos(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String(80), unique=True, nullable=False)
  descripcion = db.Column(db.String(200), nullable=False)
  contacto = db.Column(db.String(10), nullable=False)
  lat = db.Column(db.Float(200), nullable=False)
  lon = db.Column(db.Float(200), nullable=False)

def _init_(self, nombre, descripcion, contacto, lat, lon):
    self.nombre = nombre
    self.descripcion = descripcion
    self.contacto = contacto
    self.lat = lat
    self.lon = lon


@app.route('/registro')
def registro():
	return render_template('registro.html')

@app.route("/Mapa")
def mapa():
    popup = '<b> Nombre del emprendimiento </b>'

    lugar_del_emprendimiento = folium.Map(location=[-25.300894456479014, -57.58135401902809],zoom_start=16)

    folium.Marker(location=[-25.300894456479014, -57.58135401902809],popup = popup).add_to(lugar_del_emprendimiento)

    return lugar_del_emprendimiento._repr_html_()

if __name__ =='__main__':
    app.run(debug=True)
    db.create_all()