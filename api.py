#!flask/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    #return "Hello world!"
    info = {
        "mensaje" : "Bienvenido a la API del curriculum vitae de MORALES, Cesar Luis",
        "acciones" : [
            "GET /curriculum",
            "POST /mensajes"
        ]
    }
    return jsonify(info)

@app.route('/curriculum', methods=['GET'])
def cv():
    url_imagen = request.host_url + 'static/profileImage.png'
    cv = {
        "nombre" : "Cesar Luis",
        "apellido" : "MORALES",
        "residencia" : "Argentina",
        "experiencia" : [{
            "posicion" : "<posicion>"
        }],
        "educacion" : [{
            "titulo" : "<titulo>"
        }],
        "intereses" : ["python", "apis", "programacion"],
        "foto" : url_imagen
    }
    return jsonify(cv)

if __name__ == '__main__':
    app.run(debug=True)