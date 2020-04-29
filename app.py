import os
from flask import Flask, render_template, abort
import json

app = Flask(__name__)

with open("books.json") as fichero:
	datos=json.load(fichero)




@app.route('/', methods=["GET", "POST"])
def inicio():
	return render_template("index.html", lista=datos)




# Tienes que crear esta variable si no la tienes, en heroku no hace falta.
# Ponemos en el terminal para poner el puerto en nustra maquina local el siguiente comando.
#   $ export PORT=8080
port=os.environ["PORT"]

app.run('0.0.0.0', int(port), debug=True)
