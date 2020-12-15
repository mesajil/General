from flask import Flask, request, make_response, redirect
app = Flask(__name__)


@app.route('/') # RUTA RAIZ
def index ():
    reponse = make_response (redirect("/hello"))
    reponse.set_cookie ("user_ip", request.remote_addr) # CREANDO NUEVA COOKIE
    return reponse # RETORNO DE RESPUESTA DE FLASK

@app.route('/hello') # RUTA HELLO
def hello():
    return "IP = {}".format(request.cookies.get("user_ip"))
