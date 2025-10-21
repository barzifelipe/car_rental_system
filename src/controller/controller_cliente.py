from model.clientes import Cliente
from conexion.oracle_queries import OracleQueries

class Controller_Cliente:
    def __init__(self):
        pass

    def inserir_cliente(self) -> Cliente:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        cpf = input("Informe o CPF do novo Cliente: ")

        if self.verifica_existencia_cliente(oracle, cpf):
            print(f"O CPF {cpf} já está cadastrado no sistema.")
            input("\nPressione Enter para prosseguir")
            return None

        nome = input("Informe o nome completo do Cliente: ")
        cnh = input("Informe o número da CNH do Cliente: ")

        oracle.write(f"""
            INSERT INTO clientes (cpf, nome, cnh)
            VALUES ('{cpf}', '{nome}', '{cnh}')
        """)

        df_cliente = oracle.sqlToDataFrame(f"""
            SELECT cpf, nome, cnh FROM clientes WHERE cpf = '{cpf}'
        """)

        novo_cliente = Cliente(
            df_cliente.cpf.values[0],
            df_cliente.nome.values[0],
            df_cliente.cnh.values[0]
        )

        print("\nCliente inserido com sucesso!")
        print(novo_cliente.to_string())
        input("\nPressione Enter para prosseguir")
        return novo_cliente

    def atualizar_cliente(self) -> Cliente:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        cpf = input("Informe o CPF do Cliente que deseja alterar: ")

        if not self.verifica_existencia_cliente(oracle, cpf=cpf):
            print(f"O Cliente com o CPF {cpf} não foi encontrado.")
            input("\nPressione Enter para prosseguir")
            return None
        
        novo_cpf = input("Informe o novo CPF do Cliente: ")
        novo_nome = input("Informe o novo nome do Cliente: ")
        nova_cnh = input("Informe sua nova CNH do Cliente:: ")

        oracle.write(f"""
            UPDATE clientes 
            SET cpf = '{novo_cpf}', nome = '{novo_nome}', cnh = '{nova_cnh}'
            WHERE cpf = '{cpf}'
        """)

        df_cliente = oracle.sqlToDataFrame(f"""
            SELECT cpf, nome, cnh FROM clientes WHERE cpf = '{novo_cpf}'
        """)

        cliente_atualizado = Cliente(
            df_cliente.cpf.values[0],
            df_cliente.nome.values[0],
            df_cliente.cnh.values[0]
        )

        print("\nCliente atualizado com sucesso! ")
        print(cliente_atualizado.to_string())
        input("\nPressione Enter para prosseguir")
        return cliente_atualizado

    def excluir_cliente(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        cpf = input("Informe o CPF do Cliente a ser excluído: ")

        if not self.verifica_existencia_cliente(oracle, cpf=cpf):
            print(f"O Cliente com o CPF {cpf} não foi encontrado.")
            input("\nPressione Enter para prosseguir")
            return

        df_cliente = oracle.sqlToDataFrame(f"""
            SELECT cpf, nome, cnh FROM clientes WHERE cpf = '{cpf}'
        """)

        oracle.write(f"""
            DELETE FROM clientes WHERE cpf = '{cpf}'
        """)

        cliente_excluido = Cliente(
            df_cliente.cpf.values[0],
            df_cliente.nome.values[0],
            df_cliente.cnh.values[0]
        )

        print("\nCliente removido com sucesso! ")
        print(cliente_excluido.to_string())
        input("\nPressione Enter para prosseguir")

    def verifica_existencia_cliente(self, oracle: OracleQueries, cpf: str = None) -> bool:
        if not cpf:
            return False

        query = f"SELECT cpf FROM clientes WHERE cpf = '{cpf}'"
        df_cliente = oracle.sqlToDataFrame(query)
        return not df_cliente.empty

