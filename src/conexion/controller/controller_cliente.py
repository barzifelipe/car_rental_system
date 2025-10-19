from model.clientes import Cliente
from conexion.oracle_queries import OracleQueries

class Controller_Cliente:
    def __init__(self):
        pass

    def inserir_cliente(self) -> Cliente:

        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o seu CPF
        cpf = input("Informe o seu CPF: ")

        # Verifica se o cliente já está cadastrado no sistema
        if self.verifica_existencia_cliente(oracle, cpf):
            print(f"A placa {cpf} já está cadastrada no sistema.")
            return None

        # Solicita os dados restantes do cliente
        nome_cliente = input("Informe o seu nome completo: ")
        cnh = float(input("Informe o número da sua CNH: "))
        
        # Insere e persiste o novo cliente no sistema
        oracle.write(f"insert into clientes (cpf, nome_cliente, cnh) values ('{cpf}', '{nome_cliente}', {cnh})")
        
        # Recupera os dados do novo cliente criado
        df_cliente = oracle.sqlToDataFrame(f"select cpf, nome_cliente, cnh from clientes where cpf = '{cpf}'")
        
        # Cria um novo objeto Cliente
        novo_cliente = Cliente(df_cliente.cpf.values[0], df_cliente.nome_cliente.values[0], df_cliente.cnh.values[0])
        
        # Exibe os atributos do novo Cliente
        print(novo_cliente.to_string())
        
        # Retorna o objeto novo_carro
        return novo_cliente

    def atualizar_cliente(self) -> Cliente:

        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o CPF do cliente a ser alterado
        cpf = (input("CPF do cliente que deseja alterar: "))

        # Verifica se o carro existe
        if not self.verifica_existencia_cliente(oracle, cpf=cpf):
            print(f"O carro com CPF {cpf} não foi encontrado.")
            return None

        # Solicita os novos dados do cliente
        novo_nome = input("Novo Nome: ")
        
        # Atualiza os dados do cliente
        oracle.write(f"update clientes set nome_cliente = '{novo_nome}' where cpf = '{cpf}'")
        
        # Recupera os dados atualizados do cliente
        df_cliente = oracle.sqlToDataFrame(f"select cpf, nome_cliente, cnh from clientes where cpf = '{cpf}'")
        
        # Cria um objeto cliente com os dados atualizados
        cliente_atualizado = Cliente(df_cliente.cpf.values[0], df_cliente.nome_cliente.values[0], df_cliente.cnh.values[0])
        
        # Exibe os atributos do cliente atualizado
        print(cliente_atualizado.to_string())
        
        # Retorna o objeto cliente_atualizado
        return cliente_atualizado

    def excluir_cliente(self):

        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o CPF do cliente a ser excluído
        cpf = int(input("CPF do cliente que será excluído: "))

        # Verifica se o CPF existe
        if not self.verifica_existencia_cliente(oracle, cpf=cpf):
            print(f"O cliente com o CPF: {cpf} não foi encontrado.")
            return

        # Recupera os dados do cliente antes de excluir
        df_cliente = oracle.sqlToDataFrame(f"select cpf, nome_cliente, cnh from clientes where cpf = '{cpf}'")
        
        # Exclui o cliente
        oracle.write(f"delete from clientes where cpf = {cpf}")
        
        # Cria um objeto Cliente com os dados do cliente excluído para exibição
        cliente_excluido = Cliente(df_cliente.cpf.values[0], df_cliente.nome_cliente.values[0], df_cliente.cnh.values[0])
        
        # Exibe a confirmação da exclusão
        print("Cliente Removido com Sucesso!")
        print(cliente_excluido.to_string())

    def verifica_existencia_cliente(self, oracle: OracleQueries, cpf: str = None) -> bool:

        if cpf:
            query = f"select cpf from clientes where cpf = '{cpf}'"
        else:
            return False
            
        df_cliente = oracle.sqlToDataFrame(query)
        return not df_cliente.empty
