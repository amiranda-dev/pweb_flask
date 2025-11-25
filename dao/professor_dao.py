from dao.db_config import get_connection

class ProfessorDAO:
    sqlSelect = "SELECT p.id, p.nome, p.disciplina  FROM professor p"

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista