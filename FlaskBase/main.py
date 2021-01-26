from flask import Flask, request, make_response, redirect, render_template
app = Flask(__name__)


@app.route('/') # RUTA RAIZ
def index ():
    response = make_response (redirect("/hello"))
    # Creando cookie con nombre user_ip y se almacena la dirección ip del cliente (remote_addr)
    response.set_cookie ("user_ip", request.remote_addr)
    return response # RETORNO DE RESPUESTA DE FLASK

@app.route('/hello') # RUTA HELLO
def hello():
    template = "menu.html"
    text = "IP = {}, name = {}".format(request.cookies.get("user_ip"), __name__)
    return render_template (template, text = text)
