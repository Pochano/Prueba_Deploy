from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def Index():
    Ultimas_Noticias = [
    ["Victoria en Champions", "El Barça gana 3-1 en la ida de cuartos", "2025-09-10", "champions_victoria.png"],
    ["Lesión de jugador clave", "Messi sufre una lesión durante el entrenamiento", "2025-09-09", "lesion_messi.png"],
    ["Nuevo fichaje confirmado", "El club ficha a un prometedor centrocampista", "2025-09-08", "nuevo_fichaje.png"]
    ]

    Proximo_Partido = [
    ["FC Barcelona", "Real Madrid", "FC Barcelona", "Real Madrid", "campo_principal", "real_madrid.png", "20/09/2025 18:00"]
    ]
    return render_template("index.html", Ultimas_Noticias_R=Ultimas_Noticias, Proximo_Partido_R=Proximo_Partido)

@app.route('/Login')
def login():
    return "Página de login"

@app.route('/Register')
def register():
    return "Página de register"

@app.route('/Logout')
def logout():
    return "Logout exitoso"

@app.route('/Deportes')
def deportes():
    return "Página de deportes"

@app.route('/Instalaciones')
def instalaciones():
    return "Página de instalaciones"

@app.route('/Noticias')
def noticias():
    return "Página de noticias"

@app.route('/Directiva')
def directiva():
    return "Página de directiva"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)