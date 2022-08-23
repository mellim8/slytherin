from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

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
  nombre = db.Column(db.String(80), unique=True, nullable=False)
  testimonio = db.Column(db.String(200), nullable=False)
  contacto = db.Column(db.String(10), nullable=False)
  rubro = db.Column(db.String(200), nullable=False)
  latitud = db.Column(db.Float(200), nullable=False)
  longitud = db.Column(db.Float(200), nullable=False)

  def __init__(self, nombre, testimonio, contacto, rubro, latitud, longitud):
    self.nombre = nombre
    self.testimonio = testimonio
    self.contacto = contacto
    self.rubro = rubro
    self.latitud = latitud
    self.longitud = longitud
    

@app.route('/registro', methods=['GET','POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        testimonio = request.form['testimonio']
        contacto = request.form['contacto']
        rubro = request.form['rubro']
        latitud = request.form['latitud']
        longitud = request.form['longitud']      

        emprendimientos = Emprendimientos(nombre, testimonio, contacto, rubro, latitud, longitud)
        db.session.add(emprendimientos)
        db.session.commit()

    return render_template('registro.html')
    
if __name__ =='__main__':
    app.run(debug=True)
    db.create_all()