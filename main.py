from flask import Flask

app = Flask (__name__)

@app.route("/hola")
def hola():
    return("Hola mundo")

@app.route("/saludo/<nombre>")
def saludar(nombre):
    return f"Hola {nombre}"

app.run()