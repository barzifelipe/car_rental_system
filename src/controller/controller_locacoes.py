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

        cpf = input("CPF do Cliente: ")
        id_carro = int(input("ID do Veículo: "))
        id_funcionario = int(input("ID do Funcionário: "))
        data_inicio = input("Data de Início (dd/mm/aaaa): ")
        data_fim = input("Data de Fim (dd/mm/aaaa): ")

        
        df_cliente = oracle.sqlToDataFrame(f"SELECT cpf, nome FROM clientes WHERE cpf = '{cpf}'")
        df_carro = oracle.sqlToDataFrame(f"SELECT id_carro, modelo FROM carros WHERE id_carro = {id_carro}")
        df_func = oracle.sqlToDataFrame(f"SELECT id_funcionario, nome FROM funcionarios WHERE id_funcionario = {id_funcionario}")

        if df_cliente.empty:
            print(f"Cliente com CPF {cpf} não encontrado.")
            input("\nPressione Enter para prosseguir")
            return None
        if df_carro.empty:
            print(f"Veículo com ID {id_carro} não encontrado.")
            input("\nPressione Enter para prosseguir")
            return None
        if df_func.empty:
            print(f"Funcionário com ID {id_funcionario} não encontrado.")
            input("\nPressione Enter para prosseguir")
            return None

       
        df_reserva = oracle.sqlToDataFrame(
            f"SELECT numero_reserva FROM locacoes "
            f"WHERE id_carro = {id_carro} "
            f"AND (TO_DATE('{data_inicio}','DD/MM/YYYY') BETWEEN data_inicio AND data_fim "
            f"OR TO_DATE('{data_fim}','DD/MM/YYYY') BETWEEN data_inicio AND data_fim)"
        )
        if not df_reserva.empty:
            print(f"O carro {id_carro} já está reservado neste período.")
            input("\nPressione Enter para prosseguir")
            return None

        
        oracle.write(
            f"INSERT INTO locacoes (numero_reserva, data_inicio, data_fim, cpf, id_carro, id_funcionario) "
            f"VALUES (LABDATABASE.LOCACOES_NUMERO_RESERVA_SEQ.NEXTVAL, "
            f"TO_DATE('{data_inicio}', 'DD/MM/YYYY'), TO_DATE('{data_fim}', 'DD/MM/YYYY'), "
            f"'{cpf}', {id_carro}, {id_funcionario})"
        )

       
        df_loc = oracle.sqlToDataFrame(
            f"SELECT numero_reserva, data_inicio, data_fim, cpf, id_carro, id_funcionario "
            f"FROM locacoes "
            f"WHERE rownum = 1 "
            f"ORDER BY numero_reserva DESC"
        )

        cliente = Cliente(df_cliente.cpf.values[0], df_cliente.nome.values[0])
        carro = Carro(df_carro.id_carro.values[0], df_carro.modelo.values[0])
        funcionario = Funcionario(df_func.id_funcionario.values[0], df_func.nome.values[0])

        nova_locacao = Locacao(
            df_loc.numero_reserva.values[0],
            df_loc.data_inicio.values[0],
            df_loc.data_fim.values[0],
            cliente,
            carro,
            funcionario
        )

        print("\nLocação inserida com sucesso!")
        print(nova_locacao.to_string())
        input("\nPressione Enter para prosseguir")
        return nova_locacao

    def atualizar_locacao(self) -> Locacao:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        numero_reserva = int(input("Número da reserva que deseja atualizar: "))

        df_loc = oracle.sqlToDataFrame(f"SELECT * FROM locacoes WHERE numero_reserva = {numero_reserva}")
        if df_loc.empty:
            print(f"A reserva {numero_reserva} não existe.")
            input("\nPressione Enter para prosseguir")
            return None

        data_fim = input("Nova Data de Fim (dd/mm/aaaa): ")
        oracle.write(
            f"UPDATE locacoes SET data_fim = TO_DATE('{data_fim}', 'DD/MM/YYYY') "
            f"WHERE numero_reserva = {numero_reserva}"
        )

       
        df_loc = oracle.sqlToDataFrame(f"SELECT * FROM locacoes WHERE numero_reserva = {numero_reserva}")
        df_cliente = oracle.sqlToDataFrame(f"SELECT cpf, nome FROM clientes WHERE cpf = '{df_loc.cpf.values[0]}'")
        df_carro = oracle.sqlToDataFrame(f"SELECT id_carro, modelo FROM carros WHERE id_carro = {df_loc.id_carro.values[0]}")
        df_func = oracle.sqlToDataFrame(f"SELECT id_funcionario, nome FROM funcionarios WHERE id_funcionario = {df_loc.id_funcionario.values[0]}")

        cliente = Cliente(df_cliente.cpf.values[0], df_cliente.nome.values[0])
        carro = Carro(df_carro.id_carro.values[0], df_carro.modelo.values[0])
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
        input("\nPressione Enter para prosseguir")
        return loc_atualizada

    def excluir_locacao(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        numero_reserva = int(input("Número da reserva que deseja excluir: "))

        df_loc = oracle.sqlToDataFrame(f"SELECT * FROM locacoes WHERE numero_reserva = {numero_reserva}")
        if df_loc.empty:
            print(f"A reserva {numero_reserva} não existe.")
            input("\nPressione Enter para prosseguir")
            return None

        oracle.write(f"DELETE FROM locacoes WHERE numero_reserva = {numero_reserva}")

        print("\nLocação removida com sucesso!")
        print(f"Reserva: {df_loc.numero_reserva.values[0]} | CPF: {df_loc.cpf.values[0]} | Veículo: {df_loc.id_carro.values[0]}")
        input("\nPressione Enter para prosseguir")

    def verifica_existencia_locacao(self, oracle: OracleQueries, numero_reserva: int = None, id_carro: int = None) -> bool:
        if numero_reserva:
            df_loc = oracle.sqlToDataFrame(f"SELECT numero_reserva FROM locacoes WHERE numero_reserva = {numero_reserva}")
        elif id_carro:
            df_loc = oracle.sqlToDataFrame(f"SELECT numero_reserva FROM locacoes WHERE id_carro = {id_carro}")
        else:
            return False
        return not df_loc.empty
