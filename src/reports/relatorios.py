from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):
        with open("/home/labdatabase/Documents/car_rental_system/src/sql/relatorio_carros_sistema.sql") as f:
            self.query_relatorio_carros_sistema = f.read()

        with open("/home/labdatabase/Documents/car_rental_system/src/sql/relatorio_clientes.sql") as f:
            self.query_relatorio_clientes = f.read()

        with open("/home/labdatabase/Documents/car_rental_system/src/sql/relatorio_funcionarios.sql") as f:
            self.query_relatorio_funcionarios = f.read()

        with open("/home/labdatabase/Documents/car_rental_system/src/sql/relatorio_locacao.sql") as f:
            self.query_relatorio_locacao = f.read()

        with open("/home/labdatabase/Documents/car_rental_system/src/sql/relatorio_total_valor_diarias.sql") as f:
            self.query_relatorio_total_valor_diarias = f.read()

    def get_relatorio_carros_sistema(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_carros_sistema))
        input("\nPressione Enter para prosseguir ou sair\n")

    def get_relatorio_clientes(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_clientes))
        input("\nPressione Enter para prosseguir ou sair\n")
    
    def get_relatorio_funcionarios(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_funcionarios))
        input("\nPressione Enter para prosseguir ou sair\n")

    def get_relatorio_locacao(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_locacao))
        input("\nPressione Enter para prosseguir ou sair\n")

    def get_relatorio_total_valor_diarias(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_total_valor_diarias))
        input("\nPressione Enter para prosseguir ou sair\n")

