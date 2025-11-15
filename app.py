from flask import Flask, render_template # importanto a classe Flask


app = Flask(__name__) # objeto chamado app e sua localização


@app.route('/') # uma rota (decorator)
def home():
    return render_template('index.html')


@app.route('/aluno')
def listar_aluno():
    lista_alunos = [
        (1, "Ana Beatriz Silva", 20, "Teresina"),
        (2, "Carlos Eduardo Lima", 22, "Parnaíba"),
        (3, "Mariana Souza", 19, "Picos"),
        (4, "Rafael Oliveira", 23, "Floriano"),
        (5, "Juliana Costa", 21, "Campo Maior"),
        (6, "Pedro Henrique", 20, "Oeiras"),
        (7, "Fernanda Gomes", 18, "Piripiri"),
        (8, "Lucas Almeida", 22, "Altos"),
        (9, "Bianca Rocha", 24, "Esperantina"),
        (10, "Matheus Ribeiro", 19, "Barras"),
    ]
    return render_template('aluno/lista.html',lista=lista_alunos)


@app.route('/sobre') # uma rota (decorator)
def sobre():
    return render_template('sobre.html')


@app.route('/ajuda')
def ajuda():
    return 'Ajuda do sistema'


if __name__ == '__main__':
    app.run(debug=True)