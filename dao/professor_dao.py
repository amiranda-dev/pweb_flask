from dao.db_config import get_connection

class ProfessorDAO:
    sqlSelect = "SELECT p.id, p.nome, p.disciplina  FROM professor p order by id desc"

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista
    

    def salvar(self, id, nome, disciplina):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if id:
                cursor.execute(
                    'UPDATE professor SET nome = %s, disciplina = %s WHERE id = %s',
                    (nome, disciplina, id)
                )
            else:
                cursor.execute(
                    'INSERT INTO professor (nome, disciplina) VALUES (%s, %s)',
                    (nome, disciplina)
                )

            conn.commit()
            return {"status": "ok"}

        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}

        finally:
            conn.close()


    def buscar_por_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT id, nome, disciplina FROM professor WHERE id = %s',
            (id,)
        )
        registro = cursor.fetchone()
        conn.close()
        return registro


    def remover(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM professor WHERE id = %s', (id,))
            conn.commit()
            return {"status": "ok"}

        except Exception as e:
            # mensagem amigável para caso de FK
            if "violates foreign key constraint" in str(e):
                return {
                    "status": "erro",
                    "mensagem": "Não é possível remover este professor porque ele está vinculado a uma turma."
                }
            else:
                return {
                    "status": "erro",
                    "mensagem": f"Erro inesperado: {str(e)}"
                }

        finally:
            conn.close()

