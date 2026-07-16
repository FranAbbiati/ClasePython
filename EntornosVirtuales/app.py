from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Menu')
def Menu():
    return render_template('Menu.html')

@app.route('/Tutorial')
def Tutorial():
    return render_template('Tutorial.html')

@app.route('/Youtube')
def Youtube():
    return render_template('Youtube.html')

@app.route('/Formulario')
def Formulario():
    return render_template('Formulario.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/AlbumPerros')
def AlbumPerros():
    return render_template('AlbumPerros.html')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)