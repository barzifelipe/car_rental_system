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


class SplashScreenLocadora:
    def __init__(self):
        self.created_by = (
            "Emanoel Vitor Ventura Atanazio | "
            "Felipe Rodrigues Barzilai | "
            "João Emanoel Justino | "
            "Livia Favato Bastos Neves | "
            "Rogeres Jose Prates da Silva"
        )
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2025/2"

    def get_total(self, tabela: str):
        """Retorna o total de registros de uma tabela"""
        oracle = OracleQueries()
        oracle.connect()
        df = oracle.sqlToDataFrame(
            f"SELECT COUNT(*) AS total_{tabela} FROM LABDATABASE.{tabela.upper()}"
        )
        return df[f"total_{tabela}"].values[0]

    def get_updated_screen(self):
        """Retorna a splash screen atualizada com os totais"""
        total_clientes = str(self.get_total('clientes')).rjust(5)
        total_carros = str(self.get_total('carros')).rjust(5)
        total_funcionarios = str(self.get_total('funcionarios')).rjust(5)
        total_locacoes = str(self.get_total('locacoes')).rjust(5)

        return f"""
        ================== SISTEMA DE LOCAÇÃO DE VEÍCULOS ================
        ||                                                              ||
        || TOTAL DE REGISTROS:                                          ||    
        ||     1 - CLIENTES:         {total_clientes}                   ||
        ||     2 - VEÍCULOS:         {total_carros}                     ||
        ||     3 - FUNCIONÁRIOS:     {total_funcionarios}               ||
        ||     4 - LOCAÇÕES:         {total_locacoes}                   ||
        ||                                                              ||
        ||   CRIADO POR: {self.created_by}                              ||
        ||   PROFESSOR:  {self.professor}                               ||
        ||   DISCIPLINA: {self.disciplina}                              ||
        ||               {self.semestre}                                ||
         =================================================================
        """