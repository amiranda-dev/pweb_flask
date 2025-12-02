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


#  ====================================== INICIO ALUNO ====================================== #
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

#====================================== FIM ALUNO =======================================#


#====================================== INICIO PROFESSOR ================================#
@app.route('/professor')
def listar_professor():
    dao = ProfessorDAO()
    lista = dao.listar()
    return render_template('professor/lista.html',lista=lista)


@app.route('/professor/form')
def form_professor():
    return render_template('professor/form.html', professor=[None, "", ""])


@app.route('/professor/salvar/', methods=['POST'])  # Inserção
@app.route('/professor/salvar/<int:id>', methods=['POST'])  # Atualização
def salvar_professor(id=None):

    nome = request.form['nome']
    disciplina = request.form['disciplina']

    dao = ProfessorDAO()
    result = dao.salvar(id, nome, disciplina)

    if result["status"] == "ok":
        flash("Registro salvo com sucesso", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/professor')


@app.route('/professor/editar/<int:id>')
def editar_professor(id):
    dao = ProfessorDAO()
    professor = dao.buscar_por_id(id)
    return render_template('professor/form.html', professor=professor)


@app.route('/professor/remover/<int:id>')
def remover_professor(id):
    dao = ProfessorDAO()
    resultado = dao.remover(id)

    if resultado["status"] == "ok":
        flash("Professor removido com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")

    return redirect('/professor')
#  ====================================== FIM PROFESSOR ====================================== #

@app.route('/curso')
def listar_curso():
    dao = CursoDAO()
    lista = dao.listar()
    return render_template('curso/lista.html', lista=lista)


@app.route('/curso/form')
def form_curso():
    return render_template('curso/form.html', curso=None)


@app.route('/curso/salvar/', methods=['POST'])       # Inserção
@app.route('/curso/salvar/<int:id>', methods=['POST'])  # Atualização
def salvar_curso(id=None):

    nome_curso = request.form['nome_curso']
    duracao = request.form['duracao']  

    dao = CursoDAO()
    result = dao.salvar(id, nome_curso, duracao)

    if result["status"] == "ok":
        flash("Curso salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/curso')



@app.route('/curso/editar/<int:id>')
def editar_curso(id):
    dao = CursoDAO()
    curso = dao.buscar_por_id(id)
    return render_template('curso/form.html', curso=curso)


@app.route('/curso/remover/<int:id>')
def remover_curso(id):
    dao = CursoDAO()
    resultado = dao.remover(id)

    if resultado["status"] == "ok":
        flash("Curso removido com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")

    return redirect('/curso')


@app.route('/turma')
def listar_turma():
    dao = TurmaDAO()
    lista = dao.listar()
    return render_template('turma/lista.html',lista=lista)

@app.route('/turma/form')
def form_turma():
    listar_professores = ProfessorDAO.listar()
    listar_cursos = CursoDAO.listar()

    return render_template('turma/form.html', turma=None, listar_professores=listar_professores, listar_cursos=listar_cursos)

@app.route('/turma/salvar', methods=['POST'])
@app.route('/turma/salvar/<int:id>', methods=['POST'])
def salvar_turma(id=None):
    semestre = request.form['semestre']
    curso_id = request.form['curso_id']
    professor_id = request.form['professor_id']

    dao = TurmaDAO()
    resultado = dao.salvar(id, semestre, curso_id, professor_id)

    if resultado['status'] == 'ok':
        flash('Regsitro salvo com sucesso', 'success')
    else:
        flash(resultado['mensagem'], 'danger')

    return redirect('/turma')


@app.route('/turma/editar/<int:id>')
def editar_turma(id):
    listar_professores = ProfessorDAO.listar()
    listar_cursos = CursoDAO.listar()
    dao = TurmaDAO()
    turma = dao.buscar_por_id(id)

    return render_template('turma/form.html', turma=turma, listar_professores=listar_professores, listar_cursos=listar_cursos)

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

@app.route('/teste')
def teste():
    turma = [6, '2025.2', 2, 2]
    listar_cursos = CursoDAO().listar()
    return render_template('saudacao/teste.html', turma=turma, listar_cursos=listar_cursos)


if __name__ == '__main__':
    app.run(debug=True)