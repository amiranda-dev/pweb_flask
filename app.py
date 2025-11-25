from flask import Flask, render_template, request # importanto a classe Flask
from dao.db_config import get_connection
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.curso_dao import CursoDAO
from dao.turma_dao import TurmaDAO


app = Flask(__name__) # objeto chamado app e sua localização


@app.route('/') # uma rota (decorator)
def home():
    return render_template('index.html')


@app.route('/aluno')
def listar_aluno():
    dao = AlunoDAO()
    lista = dao.listar()
    return render_template('aluno/lista.html',lista=lista)


@app.route('/professor')
def listar_professor():
    dao = ProfessorDAO()
    lista = dao.listar()
    return render_template('professor/lista.html',lista=lista)


@app.route('/curso')
def listar_curso():
    dao = CursoDAO()
    lista = dao.listar()
    return render_template('curso/lista.html', lista=lista)

@app.route('/turma')
def listar_turma():
    dao = TurmaDAO()
    lista = dao.listar()
    return render_template('turma/lista.html',lista=lista)

@app.route('/saudacao1/<nome>')
def saudacao1(nome):
    print(f"Você digitou na URL {nome}")
    # gravar no banco de nome
    # dao.salvar(nome)
    return render_template('saudacao/saudacao.html', valor_recebido=nome)


@app.route('/saudacao2/')
def saudacao2():
    id = request.args.get('id')
    status = request.args.get('status')
    dados = f'O id envaido foi: {id} e o status: {status}'
    return render_template('saudacao/saudacao.html', valor_recebido=dados)

@app.route('/sobre') # uma rota (decorator)
def sobre():
    return render_template('sobre.html')


@app.route('/ajuda')
def ajuda():
    return 'Ajuda do sistema'


if __name__ == '__main__':
    app.run(debug=True)