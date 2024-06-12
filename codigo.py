from flask import flask

app = Flask(__name__)
#cria um site
#route --> danonagus.com
#função -->  o que tu vai exibir na tela

@app.route("/")
def homepage():
    return "Jean passou por aqui"

#agora coloca isso(site) no ar

app.run(debug = true)
