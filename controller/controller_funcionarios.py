from model.funcionarios import Funcionario
from conexion.oracle_queries import OracleQueries

class Controller_Funcionario:
    def __init__(self):
        pass

    def inserir_funcionario(self) -> Funcionario:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_funcionario = int(input("ID do Funcionário (Novo): "))

        # Verifica se já existe funcionário com esse ID
        if self.verifica_existencia_funcionario(oracle, id_funcionario):
            nome = input("Nome do Funcionário: ")
            cargo = input("Cargo do Funcionário: ")

            oracle.write(
                f"INSERT INTO funcionarios (id_funcionario, nome, cargo) "
                f"VALUES ({id_funcionario}, '{nome}', '{cargo}')"
            )

            df_func = oracle.sqlToDataFrame(
                f"SELECT id_funcionario, nome, cargo FROM funcionarios WHERE id_funcionario = {id_funcionario}"
            )

            novo_func = Funcionario(
                df_func.id_funcionario.values[0],
                df_func.nome.values[0],
                df_func.cargo.values[0]
            )

            print("\nFuncionário inserido com sucesso!")
            print(novo_func.to_string())
            return novo_func
        else:
            print(f"O ID {id_funcionario} já está cadastrado.")
            return None

    def atualizar_funcionario(self) -> Funcionario:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_funcionario = int(input("ID do Funcionário que deseja atualizar: "))

        if not self.verifica_existencia_funcionario(oracle, id_funcionario):
            nome = input("Novo Nome: ")
            cargo = input("Novo Cargo: ")

            oracle.write(
                f"UPDATE funcionarios SET nome = '{nome}', cargo = '{cargo}' "
                f"WHERE id_funcionario = {id_funcionario}"
            )

            df_func = oracle.sqlToDataFrame(
                f"SELECT id_funcionario, nome, cargo FROM funcionarios WHERE id_funcionario = {id_funcionario}"
            )

            func_atualizado = Funcionario(
                df_func.id_funcionario.values[0],
                df_func.nome.values[0],
                df_func.cargo.values[0]
            )

            print("\nFuncionário atualizado com sucesso!")
            print(func_atualizado.to_string())
            return func_atualizado
        else:
            print(f"O ID {id_funcionario} não existe.")
            return None

    def excluir_funcionario(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_funcionario = int(input("ID do Funcionário que deseja excluir: "))

        if not self.verifica_existencia_funcionario(oracle, id_funcionario):
            df_func = oracle.sqlToDataFrame(
                f"SELECT id_funcionario, nome, cargo FROM funcionarios WHERE id_funcionario = {id_funcionario}"
            )

            oracle.write(f"DELETE FROM funcionarios WHERE id_funcionario = {id_funcionario}")

            func_excluido = Funcionario(
                df_func.id_funcionario.values[0],
                df_func.nome.values[0],
                df_func.cargo.values[0]
            )

            print("\nFuncionário removido com sucesso!")
            print(func_excluido.to_string())
        else:
            print(f"O ID {id_funcionario} não existe.")

    def verifica_existencia_funcionario(self, oracle: OracleQueries, id_funcionario: int = None) -> bool:
        df_func = oracle.sqlToDataFrame(
            f"SELECT id_funcionario FROM funcionarios WHERE id_funcionario = {id_funcionario}"
        )
        return df_func.empty
