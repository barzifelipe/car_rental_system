from model.carros import Carro
from conexion.oracle_queries import OracleQueries

class Controller_Carro:
    def __init__(self):
        pass

    def inserir_carro(self) -> Carro:

        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário a placa do novo carro
        placa = input("Placa do carro (Nova): ")

        # Verifica se o carro já existe
        if self.verifica_existencia_carro(oracle, placa):
            print(f"A placa {placa} já está cadastrada no sistema.")
            return None

        # Solicita os demais dados do carro
        categoria = input("Categoria do carro: ")
        valor_diaria = float(input("Valor da diária de locação: "))
        
        # Insere e persiste o novo carro
        oracle.write(f"insert into carros (placa, categoria, valor_diaria) values ('{placa}', '{categoria}', {valor_diaria})")
        
        # Recupera os dados do novo carro criado
        df_carro = oracle.sqlToDataFrame(f"select id_carro, placa, categoria, valor_diaria from carros where placa = '{placa}'")
        
        # Cria um novo objeto Carro
        novo_carro = Carro(df_carro.id_carro.values[0], df_carro.placa.values[0], df_carro.categoria.values[0], df_carro.valor_diaria.values[0])
        
        # Exibe os atributos do novo carro
        print(novo_carro.to_string())
        
        # Retorna o objeto novo_carro
        return novo_carro

    def atualizar_carro(self) -> Carro:

        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o ID do carro a ser alterado
        id_carro = int(input("ID do carro que deseja alterar: "))

        # Verifica se o carro existe
        if not self.verifica_existencia_carro(oracle, id_carro=id_carro):
            print(f"O carro com ID {id_carro} não foi encontrado.")
            return None

        # Solicita os novos dados do carro
        nova_categoria = input("Nova categoria: ")
        novo_valor_diaria = float(input("Novo valor da diária: "))
        
        # Atualiza os dados do carro
        oracle.write(f"update carros set categoria = '{nova_categoria}', valor_diaria = {novo_valor_diaria} where id_carro = {id_carro}")
        
        # Recupera os dados atualizados do carro
        df_carro = oracle.sqlToDataFrame(f"select id_carro, placa, categoria, valor_diaria from carros where id_carro = {id_carro}")
        
        # Cria um objeto Carro com os dados atualizados
        carro_atualizado = Carro(df_carro.id_carro.values[0], df_carro.placa.values[0], df_carro.categoria.values[0], df_carro.valor_diaria.values[0])
        
        # Exibe os atributos do carro atualizado
        print(carro_atualizado.to_string())
        
        # Retorna o objeto carro_atualizado
        return carro_atualizado

    def excluir_carro(self):

        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o ID do carro a ser excluído
        id_carro = int(input("ID do carro que será excluído: "))

        # Verifica se o carro existe
        if not self.verifica_existencia_carro(oracle, id_carro=id_carro):
            print(f"O carro com ID {id_carro} não foi encontrado.")
            return

        # Recupera os dados do carro antes de excluir
        df_carro = oracle.sqlToDataFrame(f"select id_carro, placa, categoria, valor_diaria from carros where id_carro = {id_carro}")
        
        # Exclui o carro
        oracle.write(f"delete from carros where id_carro = {id_carro}")
        
        # Cria um objeto Carro com os dados do carro excluído para exibição
        carro_excluido = Carro(df_carro.id_carro.values[0], df_carro.placa.values[0], df_carro.categoria.values[0], df_carro.valor_diaria.values[0])
        
        # Exibe a confirmação da exclusão
        print("Carro Removido com Sucesso!")
        print(carro_excluido.to_string())

    def verifica_existencia_carro(self, oracle: OracleQueries, placa: str = None, id_carro: int = None) -> bool:

        if placa:
            query = f"select id_carro from carros where placa = '{placa}'"
        elif id_carro:
            query = f"select id_carro from carros where id_carro = {id_carro}"
        else:
            return False
            
        df_carro = oracle.sqlToDataFrame(query)
        return not df_carro.empty
