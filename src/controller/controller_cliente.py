from model.clientes import Cliente
from conexion.oracle_queries import OracleQueries

class Controller_Cliente:
    def __init__(self):
        pass

    def inserir_cliente(self) -> Cliente:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        nome_cliente = input("Informe o nome do novo Cliente: ")

        if self.verifica_existencia_cliente(oracle, nome_cliente=nome_cliente):
            print(f"O Cliente '{nome_cliente}' já está cadastrado no sistema.")
            input("\nPressione Enter para prosseguir")
            return None
        
        cpf = input("Informe o CPF do Cliente: ")

        oracle.write(f"""
            INSERT INTO clientes (id_cliente, nome_cliente, cpf)
            VALUES (LABDATABASE.CLIENTES_ID_CLIENTE_SEQ.NEXTVAL, '{nome_cliente}', '{cpf}')
        """)

        df_cliente = oracle.sqlToDataFrame(f"""
            SELECT id_cliente, nome_cliente, cpf
            FROM clientes
            WHERE nome_cliente = '{nome_cliente}'
        """)

        novo_cliente = Cliente(
            df_cliente.id_cliente.values[0],
            df_cliente.nome_cliente.values[0],
            df_cliente.cpf.values[0]
        )

        print("\nCliente inserido com sucesso!")
        print(novo_cliente.to_string())
        input("\nPressione Enter para prosseguir")
        return novo_cliente

    def atualizar_cliente(self) -> Cliente:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_cliente = int(input("Informe o ID do Cliente que deseja atualizar: "))

        if not self.verifica_existencia_cliente(oracle, id_cliente=id_cliente):
            print(f"O ID {id_cliente} não foi encontrado.")
            input("\nPressione Enter para prosseguir")
            return None

        nome_cliente = input("Informe o novo nome do Cliente: ")
        cpf = input("Informe o novo CPF do Cliente: ")

        oracle.write(f"""
            UPDATE clientes
            SET nome_cliente = '{nome_cliente}', cpf = '{cpf}'
            WHERE id_cliente = {id_cliente}
        """)

        df_cliente = oracle.sqlToDataFrame(f"""
            SELECT id_cliente, nome_cliente, cpf
            FROM clientes
            WHERE id_cliente = {id_cliente}
        """)

        cliente_atualizado = Cliente(
            df_cliente.id_cliente.values[0],
            df_cliente.nome_cliente.values[0],
            df_cliente.cpf.values[0]
        )

        print("\nCliente atualizado com sucesso!")
        print(cliente_atualizado.to_string())
        input("\nPressione Enter para prosseguir")
        return cliente_atualizado

    def excluir_cliente(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_cliente = int(input("Informe o ID do Cliente que deseja excluir: "))

        if not self.verifica_existencia_cliente(oracle, id_cliente=id_cliente):
            print(f"O ID {id_cliente} não foi encontrado.")
            input("\nPressione Enter para prosseguir")
            return

        df_cliente = oracle.sqlToDataFrame(f"""
            SELECT id_cliente, nome_cliente, cpf
            FROM clientes
            WHERE id_cliente = {id_cliente}
        """)

        oracle.write(f"DELETE FROM clientes WHERE id_cliente = {id_cliente}")

        cliente_excluido = Cliente(
            df_cliente.id_cliente.values[0],
            df_cliente.nome_cliente.values[0],
            df_cliente.cpf.values[0]
        )

        print("\nCliente removido com sucesso!")
        print(cliente_excluido.to_string())
        input("\nPressione Enter para prosseguir")

    def verifica_existencia_cliente(self, oracle: OracleQueries, id_cliente: int = None, nome_cliente: str = None) -> bool:
        if id_cliente is not None:
            query = f"SELECT id_cliente FROM clientes WHERE id_cliente = {id_cliente}"
        elif nome_cliente is not None:
            query = f"SELECT nome_cliente FROM clientes WHERE nome_cliente = '{nome_cliente}'"
        else:
            return False

        df_cliente = oracle.sqlToDataFrame(query)
        return not df_cliente.empty
