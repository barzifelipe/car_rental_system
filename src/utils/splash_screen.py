from conexion.oracle_queries import OracleQueries
from utils import config

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
        ||     2 - CARROS:         {total_carros}                       ||
        ||     3 - FUNCIONÁRIOS:     {total_funcionarios}               ||
        ||     4 - LOCAÇÕES:         {total_locacoes}                   ||
        ||                                                              ||
        ||   CRIADO POR: {self.created_by}                              ||
        ||   PROFESSOR:  {self.professor}                               ||
        ||   DISCIPLINA: {self.disciplina}                              ||
        ||               {self.semestre}                                ||
         =================================================================
        """