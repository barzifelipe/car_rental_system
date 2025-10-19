from conexion.oracle_queries import OracleQueries
from utils import config

class SplashScreenLocadora:
    def __init__(self):
        self.qry_total_clientes = config.QUERY_COUNT.format(tabela="clientes")
        self.qry_total_veiculos = config.QUERY_COUNT.format(tabela="carros")
        self.qry_total_funcionarios = config.QUERY_COUNT.format(tabela="funcionarios")
        self.qry_total_locacoes = config.QUERY_COUNT.format(tabela="locacoes")

        self.created_by = "Emanoel Vitor Ventura Atanazio" \
                        "Felipe Rodrigues Barzilai" \
                        "João Emanoel Justino" \
                        "Livia Favato Bastos Neves" \
                        "Rogeres Jose Prates da Silva"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2025/2"

    def get_total(self, tabela: str, alias: str):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(config.QUERY_COUNT.format(tabela=tabela))[f"total_{tabela}"].values[0]

    def get_updated_screen(self):
        return f"""
        ###############################################################
        #             SISTEMA DE LOCAÇÃO DE VEÍCULOS                 
        #                                                            
        #  TOTAL DE REGISTROS:                                        
        #      1 - CLIENTES:         {str(self.get_total('clientes', 'total_clientes')).rjust(5)}
        #      2 - VEÍCULOS:         {str(self.get_total('carros', 'total_carros')).rjust(5)}
        #      3 - FUNCIONÁRIOS:     {str(self.get_total('funcionarios', 'total_funcionarios')).rjust(5)}
        #      4 - LOCAÇÕES:         {str(self.get_total('locacoes', 'total_locacoes')).rjust(5)}
        #
        #  CRIADO POR: {self.created_by}
        #  PROFESSOR:  {self.professor}
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ###############################################################
        """
