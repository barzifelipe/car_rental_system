from model.funcionarios import Funcionario
from conexion.oracle_queries import OracleQueries

class Controller_Funcionario:
    def __init__(self):
        pass

    def inserir_funcionario(self) -> Funcionario:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        nome = input("Informe o nome do novo Funcionário: ")

        if self.verifica_existencia_funcionario(oracle, nome=nome):
            print(f"O Funcionário '{nome}' já está cadastrado no sistema.")
            input("\nPressione Enter para prosseguir")
            return None
        
        cargo = input("Informe o cargo do Funcionário: ")

        oracle.write(f"""
            INSERT INTO funcionarios (id_funcionario, nome, cargo)
            VALUES (LABDATABASE.FUNCIONARIOS_ID_FUNCIONARIO_SEQ.NEXTVAL, '{nome}', '{cargo}')
        """)

        df_func = oracle.sqlToDataFrame(f"""
            SELECT id_funcionario, nome, cargo
            FROM funcionarios
            WHERE nome = '{nome}'
        """)

        novo_func = Funcionario(
            df_func.id_funcionario.values[0],
            df_func.nome.values[0],
            df_func.cargo.values[0]
        )

        print("\nFuncionário inserido com sucesso!")
        print(novo_func.to_string())
        input("\nPressione Enter para prosseguir")
        return novo_func

    def atualizar_funcionario(self) -> Funcionario:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_funcionario = int(input("Informe o ID do Funcionário que deseja atualizar: "))

        if not self.verifica_existencia_funcionario(oracle, id_funcionario=id_funcionario):
            print(f"O ID {id_funcionario} não foi encontrado.")
            input("\nPressione Enter para prosseguir")
            return None

        nome = input("Informe o novo nome do Fucionário: ")
        cargo = input("Informe o novo cargo do Funcionário: ")

        oracle.write(f"""
            UPDATE funcionarios
            SET nome = '{nome}', cargo = '{cargo}'
            WHERE id_funcionario = {id_funcionario}
        """)

        df_func = oracle.sqlToDataFrame(f"""
            SELECT id_funcionario, nome, cargo
            FROM funcionarios
            WHERE id_funcionario = {id_funcionario}
        """)

        func_atualizado = Funcionario(
            df_func.id_funcionario.values[0],
            df_func.nome.values[0],
            df_func.cargo.values[0]
        )

        print("\nFuncionário atualizado com sucesso!")
        print(func_atualizado.to_string())
        input("\nPressione Enter para prosseguir")
        return func_atualizado

    def excluir_funcionario(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_funcionario = int(input("Informe o ID do Funcionário que deseja excluir: "))

        if not self.verifica_existencia_funcionario(oracle, id_funcionario=id_funcionario):
            print(f"O ID {id_funcionario} não foi encontrado.")
            input("\nPressione Enter para prosseguir")
            return

        df_func = oracle.sqlToDataFrame(f"""
            SELECT id_funcionario, nome, cargo
            FROM funcionarios
            WHERE id_funcionario = {id_funcionario}
        """)

        oracle.write(f"DELETE FROM funcionarios WHERE id_funcionario = {id_funcionario}")

        func_excluido = Funcionario(
            df_func.id_funcionario.values[0],
            df_func.nome.values[0],
            df_func.cargo.values[0]
        )

        print("\nFuncionário removido com sucesso!")
        print(func_excluido.to_string())
        input("\nPressione Enter para prosseguir")

    def verifica_existencia_funcionario(self, oracle: OracleQueries, id_funcionario: int = None, nome: str = None) -> bool:
        if id_funcionario is not None:
            query = f"SELECT id_funcionario FROM funcionarios WHERE id_funcionario = {id_funcionario}"
        elif nome is not None:
            query = f"SELECT nome FROM funcionarios WHERE nome = '{nome}'"
        else:
            return False

        df_func = oracle.sqlToDataFrame(query)
        return not df_func.empty
