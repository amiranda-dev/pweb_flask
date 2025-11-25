from dao.db_config import get_connection

class AlunoDAO:
    sqlSelect = "SELECT a.id, a.nome, a.idade, a.cidade FROM aluno a"

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista