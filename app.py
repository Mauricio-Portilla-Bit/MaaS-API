from flask import Flask, jsonify
import os

app = Flask(__name__)

app.config["PORT"] = 5000
port = os.getenv("PORT", app.config["PORT"])

"""
hello: esta función es para saber que el programa está vivo

"""
@app.route("/api/ejemplo")
def hello():
    return jsonify({"mensaje": "Hola desde la API"})


"""
apply_model: esta función recibe el modelo que se desea usar, la entrada del modelo y devuelve el resultado
model: nombre del model que se desea usar
"""
@app.route("/api/modelo/<path:model>")
def apply_model(model):

    "1. Definir si el modelo solicitado existe"
    if False:
        return jsonify({"Error": "El modelo solicitado no existe"})

    "2. Obtener archivo de entrada del usuario"

    "3. Verificar que el archivo sea menor a cierto peso"

    "4. Verificar que el archivo sea el mismo tipo que el que solicita la red"

    "5. Realizar el cobro"

    "6. Calcular el resultado por medio del modelo"

    "7. Guardar los resultados en la base de datos del usuario"

    "8. Devolver la salida del modelo"

    print(os.listdir("Models"))
    return jsonify({"modelo": "Se usará el modelo: " + model})



"""
download_results: si existen resultados para este usuario, envairlos para descarga 
"""
@app.route("/api/download")
def download_results():

    return jsonify({"Descargando": "Descargando Resultados" })




"""
verify_user: verificar si el usuario existe y, en caso de que no, crear el usuario (cuenta de google)

"""
@app.route("/api/verify")
def verify_user():
    return jsonify({"modelo": "Se usará el modelo: " })


"""
charge_use: verificar si el usuario existe
model: modelo usado al que se le realizará el cargo 
counts: número de veces que se utilizó el modelo 
user: usuario al que se le cargará por usar el modelo 
"""
#@app.route("/api/carge")
def charge_use(model, counts):
    return jsonify({"modelo": "Se usará el modelo: " })


"""
get_user_data: obtener la información básica del usuario  
"""

@app.route("/api/user_data")
def get_user_data():
    return jsonify({"name": "Nombre"})


"""
get_user_results: obtener los resultados de los diferentes entrenamientos del usuario 
"""

@app.route("/api/user_results")
def get_user_data():
    return jsonify({"Res 1": "- - - -  ",
                    "Res 2": "- - - - - "})


# Inicia el servidor
if __name__ == "__main__":
    app.run(port=port)
