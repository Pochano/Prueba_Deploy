from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def Index():
    Ultimas_Noticias = ["Noticia 1", "Noticia 2"]
    Proximo_Partido = ["Equipo A vs Equipo B"]
    return render_template("index.html", Ultimas_Noticias_R=Ultimas_Noticias, Proximo_Partido_R=Proximo_Partido)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)