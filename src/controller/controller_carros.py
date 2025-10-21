from model.carros import Carro
from conexion.oracle_queries import OracleQueries

class Controller_Carro:
    def __init__(self):
        pass

    def inserir_carro(self) -> Carro:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        placa = input("Informe a placa do novo Carro: ")

       
        if self.verifica_existencia_carro(oracle, placa=placa):
            print(f"A placa {placa} já está cadastrada no sistema.")
            input("\nPressione Enter para prosseguir")
            return None

        modelo = input("Informe o modelo do Carro: ")
        categoria = input("Informe a categoria do Carro: ")
        valor_diaria = float(input("Informe o valor da diária de locação: "))

       
        oracle.write(f"""
            INSERT INTO carros (id_carro, modelo, placa, categoria, valor_diaria)
            VALUES (LABDATABASE.CARROS_ID_CARRO_SEQ.NEXTVAL, '{modelo}', '{placa}', '{categoria}', {valor_diaria})
        """)

        df_carro = oracle.sqlToDataFrame(f"""
            SELECT id_carro, modelo, placa, categoria, valor_diaria 
            FROM carros 
            WHERE placa = '{placa}'
        """)

        novo_carro = Carro(
            df_carro.id_carro.values[0],
            df_carro.modelo.values[0],
            df_carro.placa.values[0],
            df_carro.categoria.values[0],
            df_carro.valor_diaria.values[0]
        )

        print("\nCarro inserido com sucesso!")
        print(novo_carro.to_string())
        input("\nPressione Enter para prosseguir")
        return novo_carro

    def atualizar_carro(self) -> Carro:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_carro = int(input("Informe o ID do Carro que deseja alterar: "))

        if not self.verifica_existencia_carro(oracle, id_carro=id_carro):
            print(f"O Carro com ID {id_carro} não foi encontrado.")
            input("\nPressione Enter para prosseguir")
            return None

        novo_modelo = input("Informe o novo modelo do Carro: ")
        nova_placa = input("Informe a nova placa do Carro: ")
        nova_categoria = input("Informe a nova categoria do Carro: ")
        novo_valor_diaria = float(input("Informe o novo valor da diária do Carro: "))

       
        oracle.write(f"""
            UPDATE carros 
            SET modelo = '{novo_modelo}', 
                placa  = '{nova_placa}',
                categoria = '{nova_categoria}', 
                valor_diaria = '{novo_valor_diaria}'
            WHERE id_carro = {id_carro}
        """)

        df_carro = oracle.sqlToDataFrame(f"""
            SELECT id_carro, modelo, placa, categoria, valor_diaria 
            FROM carros 
            WHERE id_carro = {id_carro}
        """)

        carro_atualizado = Carro(
            df_carro.id_carro.values[0],
            df_carro.modelo.values[0],
            df_carro.placa.values[0],
            df_carro.categoria.values[0],
            df_carro.valor_diaria.values[0]
        )

        print("\nCarro atualizado com sucesso!")
        print(carro_atualizado.to_string())
        input("\nPressione Enter para prosseguir")
        return carro_atualizado

    def excluir_carro(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_carro = int(input("Informe o ID do Carro a ser excluído: "))

      
        if not self.verifica_existencia_carro(oracle, id_carro=id_carro):
            print(f"O Carro com ID {id_carro} não foi encontrado.")
            input("\nPressione Enter para prosseguir")
            return None

        df_carro = oracle.sqlToDataFrame(f"""
            SELECT id_carro, modelo, placa, categoria, valor_diaria 
            FROM carros 
            WHERE id_carro = {id_carro}
        """)

        oracle.write(f"DELETE FROM carros WHERE id_carro = {id_carro}")

        carro_excluido = Carro(
            df_carro.id_carro.values[0],
            df_carro.modelo.values[0],
            df_carro.placa.values[0],
            df_carro.categoria.values[0],
            df_carro.valor_diaria.values[0]
        )

        print("\nCarro removido com sucesso!")
        print(carro_excluido.to_string())
        input("\nPressione Enter para prosseguir")

    def verifica_existencia_carro(self, oracle: OracleQueries, placa: str = None, id_carro: int = None) -> bool:
        if placa:
            query = f"SELECT id_carro FROM carros WHERE placa = '{placa}'"
        elif id_carro:
            query = f"SELECT id_carro FROM carros WHERE id_carro = {id_carro}"
        else:
            return False

        df_carro = oracle.sqlToDataFrame(query)
        return not df_carro.empty
