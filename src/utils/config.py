# utils/config.py
import os


def clear_console(wait_seconds: int = 0):
    
    import time
    if wait_seconds > 0:
        time.sleep(wait_seconds)
    os.system('cls' if os.name == 'nt' else 'clear')


DB_SCHEMA = "LABDATABASE"

# Query genérica para contar registros em qualquer tabela
QUERY_COUNT = "SELECT COUNT(*) AS total_{tabela} FROM LABDATABASE.{tabela}"

QUERY_INSERT_CLIENTE = """
INSERT INTO LABDATABASE.CLIENTES (CPF, NOME_CLIENTE, CNH)
VALUES (:cpf, :nome, :cnh)
"""

QUERY_INSERT_CARRO = """
INSERT INTO LABDATABASE.CARROS (ID_CARRO, MODELO, PLACA, CATEGORIA, VALOR_DIARIA)
VALUES (CARROS_ID_CARRO_SEQ.NEXTVAL, :modelo, :placa, :categoria, :valor_diaria)
"""

QUERY_INSERT_FUNCIONARIO = """
INSERT INTO LABDATABASE.FUNCIONARIOS (ID_FUNCIONARIO, NOME, CARGO)
VALUES (FUNCIONARIOS_ID_FUNCIONARIO_SEQ.NEXTVAL, :nome, :cargo)
"""

QUERY_INSERT_LOCACAO = """
DECLARE
    VNUM_RESERVA NUMBER;
    VID_CARRO NUMBER;
BEGIN
    VNUM_RESERVA := LABDATABASE.LOCACOES_NUMERO_RESERVA_SEQ.NEXTVAL;
    
    SELECT ID_CARRO
      INTO VID_CARRO
      FROM LABDATABASE.CARROS
     WHERE PLACA = :placa;
    
    INSERT INTO LABDATABASE.LOCACOES (
        NUMERO_RESERVA,
        DATA_INICIO,
        DATA_FIM,
        CPF,
        ID_VEICULO,
        ID_FUNCIONARIO
    ) VALUES (
        VNUM_RESERVA,
        TO_DATE(:data_inicio, 'YYYY-MM-DD'),
        TO_DATE(:data_fim, 'YYYY-MM-DD'),
        :cpf,
        VID_CARRO,
        :id_funcionario
    );
END;
"""


MENU_PRINCIPAL = """
================== SISTEMA DE LOCAÇÃO ==================
1 - Relatórios
2 - Inserir registros
3 - Atualizar registros
4 - Excluir registros
5 - Sair
=========================================================
"""

MENU_RELATORIOS = """
================== RELATÓRIOS ==================
1 - Relatório de Clientes
2 - Relatório de Carros
3 - Relatório de Funcionários
4 - Relatório de Locações
5 - Voltar
===============================================
"""

MENU_ENTIDADES = """
================== ENTIDADES ==================
1 - Clientes
2 - Carros
3 - Funcionários
4 - Locações
5 - Voltar
==============================================
"""