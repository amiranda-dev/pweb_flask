from dao.db_config import get_connection

class CursoDAO:
    sqlSelect = "SELECT id, nome_curso, duracao FROM curso ORDER BY id DESC"

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista

    def salvar(self, id, nome_curso, duracao):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            if id:  # atualizar
                cursor.execute(
                    'UPDATE curso SET nome_curso = %s, duracao = %s WHERE id = %s',
                    (nome_curso, duracao, id)
                )
            else:  # inserir
                cursor.execute(
                    'INSERT INTO curso (nome_curso, duracao) VALUES (%s, %s)',
                    (nome_curso, duracao)
                )

            conn.commit()
            return {"status": "ok"}

        except Exception as e:
            conn.rollback()
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}

        finally:
            conn.close()

    def buscar_por_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT id, nome_curso, duracao FROM curso WHERE id = %s',
            (id,)
        )
        registro = cursor.fetchone()
        conn.close()
        return registro

    def remover(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM curso WHERE id = %s', (id,))
            conn.commit()
            return {"status": "ok"}

        except Exception as e:
            if "violates foreign key constraint" in str(e):
                return {
                    "status": "erro",
                    "mensagem": "Não é possível remover este curso pois está vinculado a uma turma."
                }
            else:
                return {"status": "erro", "mensagem": f"Erro: {str(e)}"}

        finally:
            conn.close()
