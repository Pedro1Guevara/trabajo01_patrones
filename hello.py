from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World 2024 UABC!</p>"

@app.route("/saludo")
def saludoatodos():
    return "<p>Saludo a todos los que me lean!</p>"

@app.route("/about")
def sobremi():
    return "<marques><hl>pedro.guevara.rodriguez@uabc.edu.mx</hl></marques>"

@app.route("/grafica")
def grafica():
    return "<img src='grafica_lugares_visitados.png' alt='Gráfica de Lugares Visitados por Anthony Bourdain en Coordenadas'>"
