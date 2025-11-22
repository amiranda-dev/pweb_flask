from flask import Flask, render_template # importanto a classe Flask
import sqlite3

app = Flask(__name__) # objeto chamado app e sua localização


@app.route('/') # uma rota (decorator)
def home():
    return render_template('index.html')


@app.route('/aluno')
def listar_aluno():
    DB_PATH = "banco_escola.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT a.id, a.nome, a.idade, a.cidade FROM aluno a")
    lista = cursor.fetchall()
    conn.close()
    return render_template('aluno/lista.html',lista=lista)


@app.route('/professor')
def listar_professor():
    DB_PATH = "banco_escola.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT p.id, p.nome, p.disciplina  FROM professor p ")
    lista = cursor.fetchall()
    conn.close()
    return render_template('professor/lista.html',lista=lista)


@app.route('/turma')
def listar_turma():
    DB_PATH = "banco_escola.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(''' 
                        SELECT turma.id, semestre, nome_curso, professor.nome  FROM turma 
                        JOIN curso on curso.id=turma.curso_id
                        JOIN professor on professor.id=turma.professor_id
                    '''
                )
    lista = cursor.fetchall()
    conn.close()
    return render_template('turma/lista.html',lista=lista)


@app.route('/sobre') # uma rota (decorator)
def sobre():
    return render_template('sobre.html')


@app.route('/ajuda')
def ajuda():
    return 'Ajuda do sistema'


if __name__ == '__main__':
    app.run(debug=True)