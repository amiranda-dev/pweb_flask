from dao.db_config import get_connection

class AlunoDAO:
    sqlSelect = "SELECT a.id, a.nome, a.idade, a.cidade FROM aluno a order by id desc"

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista
    

    def salvar(self, id, nome, idade, cidade):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO aluno (nome, idade, cidade) VALUES (%s, %s, %s)', (nome, idade, cidade))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()
