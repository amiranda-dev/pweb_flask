from dao.db_config import get_connection

class CursoDAO:
    sqlSelect = '''
                SELECT curso.id, curso.nome_curso, curso.duracao, professor.nome
                FROM curso
                JOIN turma ON turma.curso_id = curso.id
                JOIN professor ON turma.professor_id = professor.id;
                '''
    
    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista