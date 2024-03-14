from flask import Flask, jsonify
import os

app = Flask(__name__)

app.config["PORT"] = 5000
port = os.getenv("PORT", app.config["PORT"])

"""
Saludo: esta función es para saber que el programa está vivo

"""
@app.route("/api/ejemplo")
def hello():
    return jsonify({"mensaje": "Hola desde la API"})


"""
Modelo: esta función recibe el modelo que se desea usar, la entrada del modelo y devuelve el resultado

"""
@app.route("/api/modelo/<path:model>")
def apply_model(model):
    print(os.listdir("Models"))
    return jsonify({"modelo": "Se usará el modelo: " + model})



# Inicia el servidor
if __name__ == "__main__":
    app.run(port=port)