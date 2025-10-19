from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):
        
        with open("sql/relatorio_carros_sistema.sql") as f:
            self.query_relatorio_carros_sistema = f.read()

        
        with open("sql/relatorio_clientes.sql") as f:
            self.query_relatorio_clientes = f.read()

       
        with open("sql/relatorio_funcionarios.sql") as f:
            self.query_relatorio_funcionarios = f.read()

        
        with open("sql/relatorio_locacao.sql") as f:
            self.query_relatorio_locacao = f.read()


    def get_relatorio_carros_sistema(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_carros_sistema))
        input("Tecle Enter para sair deste relatório")

    def get_relatorio_relatorio_clientes(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_clientes))
        input("Tecle Enter para sair deste relatório")
    
    def get_relatorio_funcionarios(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_funcionarios))
        input("Tecle Enter para sair deste relatório")

    def get_relatorio_locacao(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_locacao))
        input("Tecle Enter para sair deste relatório")


