import os
from flask import Flask, render_template, abort
import json

app = Flask(__name__)

with open("books.json") as fichero:
	datos=json.load(fichero)


@app.route('/', methods=["GET", "POST"])
def inicio():
	return render_template("index.html", lista=datos)

@app.route('/libro/<isbn>', methods=["GET", "POST"])
def detalle(isbn):
	for libro in datos:
		if 'isbn' in libro:
			if libro["isbn"] == isbn:
				return render_template("detalle.html", libro=libro)
	abort(404)


@app.route('/categorias/<categoria>', methods=["GET", "POST"])
def categorias(categoria):
	for libro in datos:
		if 'categories' in libro:
			if categoria in libro["categories"]:
				return render_template("categorias.html", lista=datos, categoria=categoria)
	abort(404)


# Tienes que crear esta variable si no la tienes, en heroku no hace falta.
# Ponemos en el terminal para poner el puerto en nustra maquina local el siguiente comando.
#   $ export PORT=8080
port=os.environ["PORT"]

app.run('0.0.0.0', int(port), debug=False)
