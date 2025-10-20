from model.clientes import Cliente
from conexion.oracle_queries import OracleQueries

class Controller_Cliente:
    def __init__(self):
        pass

    def inserir_cliente(self) -> Cliente:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        cpf = input("Informe o CPF do cliente: ")

        if self.verifica_existencia_cliente(oracle, cpf):
            print(f"O CPF {cpf} já está cadastrado no sistema.")
            return None

        nome = input("Informe o nome completo do cliente: ")
        cnh = float(input("Informe o número da CNH do cliente: "))

        oracle.write(f"INSERT INTO clientes (cpf, nome, cnh) VALUES ('{cpf}', '{nome}', {cnh})")

        df_cliente = oracle.sqlToDataFrame(f"SELECT cpf, nome, cnh FROM clientes WHERE cpf = '{cpf}'")
  
        novo_cliente = Cliente(df_cliente.cpf.values[0], df_cliente.nome.values[0], df_cliente.cnh.values[0])

        print("\nCliente inserido com sucesso:")
        print(novo_cliente.to_string())

        return novo_cliente

    def atualizar_cliente(self) -> Cliente:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        cpf = input("Informe o CPF do cliente que deseja alterar: ")

        if not self.verifica_existencia_cliente(oracle, cpf=cpf):
            print(f"O cliente com o CPF {cpf} não foi encontrado.")
            return None

        novo_nome = input("Novo nome: ")
        oracle.write(f"UPDATE clientes SET nome = '{novo_nome}' WHERE cpf = '{cpf}'")

        df_cliente = oracle.sqlToDataFrame(f"SELECT cpf, nome, cnh FROM clientes WHERE cpf = '{cpf}'")

        cliente_atualizado = Cliente(df_cliente.cpf.values[0], df_cliente.nome.values[0], df_cliente.cnh.values[0])

        print("\nCliente atualizado com sucesso:")
        print(cliente_atualizado.to_string())

        return cliente_atualizado

    def excluir_cliente(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        cpf = input("Informe o CPF do cliente a ser excluído: ")

        # Verifica se o CPF existe
        if not self.verifica_existencia_cliente(oracle, cpf=cpf):
            print(f"O cliente com o CPF {cpf} não foi encontrado.")
            return

        # Recupera os dados do cliente antes de excluir
        df_cliente = oracle.sqlToDataFrame(f"SELECT cpf, nome, cnh FROM clientes WHERE cpf = '{cpf}'")

        # Exclui o cliente
        oracle.write(f"DELETE FROM clientes WHERE cpf = '{cpf}'")

        # Cria um objeto Cliente com os dados do cliente excluído para exibição
        cliente_excluido = Cliente(df_cliente.cpf.values[0], df_cliente.nome.values[0], df_cliente.cnh.values[0])

        print("\nCliente removido com sucesso:")
        print(cliente_excluido.to_string())

    def verifica_existencia_cliente(self, oracle: OracleQueries, cpf: str = None) -> bool:
        if not cpf:
            return False

        query = f"SELECT cpf FROM clientes WHERE cpf = '{cpf}'"
        df_cliente = oracle.sqlToDataFrame(query)
        return not df_cliente.empty
