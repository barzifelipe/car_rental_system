from datetime import datetime
from model.locacoes import Locacao
from model.clientes import Cliente
from model.carros import Carro
from model.funcionarios import Funcionario
from conexion.oracle_queries import OracleQueries

class Controller_Locacao:
    def __init__(self):
        pass

    def inserir_locacao(self) -> Locacao:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        numero_reserva = int(input("Número da Reserva (Novo): "))

        if self.verifica_existencia_locacao(oracle, numero_reserva):
            data_inicio = input("Data de Início (dd/mm/aaaa): ")
            data_fim = input("Data de Fim (dd/mm/aaaa): ")
            cpf = input("CPF do Cliente: ")
            id_veiculo = int(input("ID do Veículo: "))
            id_funcionario = int(input("ID do Funcionário: "))

            # Verifica existência das entidades relacionadas
            df_cliente = oracle.sqlToDataFrame(f"SELECT cpf, nome_cliente FROM clientes WHERE cpf = '{cpf}'")
            df_carro = oracle.sqlToDataFrame(f"SELECT id_veiculo, modelo FROM carros WHERE id_veiculo = {id_veiculo}")
            df_func = oracle.sqlToDataFrame(f"SELECT id_funcionario, nome FROM funcionarios WHERE id_funcionario = {id_funcionario}")

            if df_cliente.empty:
                print(f"\nCliente com CPF {cpf} não encontrado.")
                return None
            if df_carro.empty:
                print(f"\nVeículo com ID {id_veiculo} não encontrado.")
                return None
            if df_func.empty:
                print(f"\nFuncionário com ID {id_funcionario} não encontrado.")
                return None

            # Inserção no banco
            oracle.write(
                f"INSERT INTO locacoes (numero_reserva, data_inicio, data_fim, cpf, id_veiculo, id_funcionario) "
                f"VALUES ({numero_reserva}, TO_DATE('{data_inicio}', 'DD/MM/YYYY'), TO_DATE('{data_fim}', 'DD/MM/YYYY'), "
                f"'{cpf}', {id_veiculo}, {id_funcionario})"
            )

            # Recupera dados da nova locação
            df_loc = oracle.sqlToDataFrame(
                f"SELECT numero_reserva, data_inicio, data_fim, cpf, id_veiculo, id_funcionario "
                f"FROM locacoes WHERE numero_reserva = {numero_reserva}"
            )

            cliente = Cliente(df_cliente.cpf.values[0], df_cliente.nome_cliente.values[0])
            carro = Carro(df_carro.id_veiculo.values[0], df_carro.modelo.values[0])
            funcionario = Funcionario(df_func.id_funcionario.values[0], df_func.nome.values[0])

            nova_locacao = Locacao(
                df_loc.numero_reserva.values[0],
                df_loc.data_inicio.values[0],
                df_loc.data_fim.values[0],
                cliente,
                carro,
                funcionario
            )

            print("\nLocação registrada com sucesso!")
            print(nova_locacao.to_string())
            return nova_locacao
        else:
            print(f"O número de reserva {numero_reserva} já existe.")
            return None

    def atualizar_locacao(self) -> Locacao:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        numero_reserva = int(input("Número da Reserva que deseja atualizar: "))

        if not self.verifica_existencia_locacao(oracle, numero_reserva):
            data_fim = input("Nova Data de Fim (dd/mm/aaaa): ")

            oracle.write(
                f"UPDATE locacoes SET data_fim = TO_DATE('{data_fim}', 'DD/MM/YYYY') "
                f"WHERE numero_reserva = {numero_reserva}"
            )

            df_loc = oracle.sqlToDataFrame(
                f"SELECT numero_reserva, data_inicio, data_fim, cpf, id_veiculo, id_funcionario "
                f"FROM locacoes WHERE numero_reserva = {numero_reserva}"
            )

            df_cliente = oracle.sqlToDataFrame(f"SELECT cpf, nome_cliente FROM clientes WHERE cpf = '{df_loc.cpf.values[0]}'")
            df_carro = oracle.sqlToDataFrame(f"SELECT id_veiculo, modelo FROM carros WHERE id_veiculo = {df_loc.id_veiculo.values[0]}")
            df_func = oracle.sqlToDataFrame(f"SELECT id_funcionario, nome FROM funcionarios WHERE id_funcionario = {df_loc.id_funcionario.values[0]}")

            cliente = Cliente(df_cliente.cpf.values[0], df_cliente.nome_cliente.values[0])
            carro = Carro(df_carro.id_veiculo.values[0], df_carro.modelo.values[0])
            funcionario = Funcionario(df_func.id_funcionario.values[0], df_func.nome.values[0])

            loc_atualizada = Locacao(
                df_loc.numero_reserva.values[0],
                df_loc.data_inicio.values[0],
                df_loc.data_fim.values[0],
                cliente,
                carro,
                funcionario
            )

            print("\nLocação atualizada com sucesso!")
            print(loc_atualizada.to_string())
            return loc_atualizada
        else:
            print(f"A reserva {numero_reserva} não existe.")
            return None

    def excluir_locacao(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        numero_reserva = int(input("Número da Reserva que deseja excluir: "))

        if not self.verifica_existencia_locacao(oracle, numero_reserva):
            df_loc = oracle.sqlToDataFrame(
                f"SELECT numero_reserva, cpf, id_veiculo, id_funcionario "
                f"FROM locacoes WHERE numero_reserva = {numero_reserva}"
            )

            oracle.write(f"DELETE FROM locacoes WHERE numero_reserva = {numero_reserva}")

            print("\nLocação removida com sucesso!")
            print(f"Reserva: {df_loc.numero_reserva.values[0]} | CPF: {df_loc.cpf.values[0]} | Veículo: {df_loc.id_veiculo.values[0]}")
        else:
            print(f"A reserva {numero_reserva} não existe.")

    def verifica_existencia_locacao(self, oracle: OracleQueries, numero_reserva: int = None) -> bool:
        df_loc = oracle.sqlToDataFrame(f"SELECT numero_reserva FROM locacoes WHERE numero_reserva = {numero_reserva}")
        return df_loc.empty
