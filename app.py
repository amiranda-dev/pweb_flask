from flask import Flask, render_template # importanto a classe Flask


app = Flask(__name__) # objeto chamado app e sua localização


@app.route('/') # uma rota (decorator)
def home():
    return render_template('index.html')


@app.route('/sobre') # uma rota (decorator)
def sobre():
    return render_template('sobre.html')


@app.route('/ajuda')
def ajuda():
    return 'Ajuda do sistema'


if __name__ == '__main__':
    app.run(debug=True)