from flask import Flask, render_template, request, redirect, flash # importanto a classe Flask
from dao.db_config import get_connection
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.curso_dao import CursoDAO
from dao.turma_dao import TurmaDAO


app = Flask(__name__) # objeto chamado app e sua localização
app.secret_key = 'uma_chave_muito_secreta_e_unica'


@app.route('/') # uma rota (decorator)
def home():
    return render_template('index.html')


@app.route('/aluno')
def listar_aluno():
    dao = AlunoDAO()
    lista = dao.listar()
    return render_template('aluno/lista.html',lista=lista)


@app.route('/aluno/form')
def form_aluno():
    return render_template('aluno/form.html', aluno=None)


@app.route('/aluno/salvar/', methods=['POST'])  # Inserção
@app.route('/aluno/salvar/<int:id>', methods=['POST'])  # Atualização
def salvar_aluno(id=None):
    nome = request.form['nome']
    idade = request.form['idade']
    cidade = request.form['cidade']

    # salvar os dados no banco
    dao = AlunoDAO()
    result = dao.salvar(id,nome, idade, cidade)
    if result["status"] == "ok":
        flash("Registro salvo com sucesso", "success")
    else:
        flash(result['mensagem'], "danger")
    return redirect('/aluno')

@app.route('/aluno/editar/<int:id>')
def editar_aluno(id):
    dao = AlunoDAO()
    aluno = dao.buscar_por_id(id)
    return render_template('aluno/form.html', aluno=aluno)


@app.route("/aluno/remover/<int:id>")
def remover_aluno(id):
    dao = AlunoDAO()
    resultado = dao.remover(id)

    if resultado["status"] == "ok":
        flash("Registro removido com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")

    return redirect('/aluno')


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
    nome = request.args.get('nome')
    return render_template('saudacao/saudacao.html', valor_recebido=nome)


@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    senha = request.form['senha']
    email = request.form['email']
    dados = f'Usuário: {usuario}, Senha: {senha} e e-mail: {email}'
    return render_template('saudacao/saudacao.html', valor_recebido=dados)


@app.route('/desafio')
def desafio():
    return render_template('desafio/desafio.html')


@app.route('/registro', methods=['POST'])
def registro():
    nome = request.form['nome']
    dataNascimento = request.form['dataNasc']
    cpf = request.form['cpf']
    nomeMae = request.form['nomeMae']
    dados = f'Nome: {nome} - Data de Nascimento: {dataNascimento} - CPF: {cpf} - Nome da Mãe: {nomeMae}'
    return render_template('desafio/desafio.html', valor_recebido=dados)


@app.route('/sobre') # uma rota (decorator)
def sobre():
    return render_template('sobre.html')


@app.route('/ajuda')
def ajuda():
    return 'Ajuda do sistema'


if __name__ == '__main__':
    app.run(debug=True)