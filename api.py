#!flask/bin/python
# -*- cidubg: UTF-8 -*-

from flask import Flask, jsonify

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

if __name__ == '__main__':
    app.run(debug=True)