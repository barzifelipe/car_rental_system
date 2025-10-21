# SISTEMA DE LOCAÇÃO DE VEÍCULOS

O Sistema de Locação de Veículos tem como objetivo gerenciar o processo de aluguel de carros, controlando informações de clientes, funcionários, veículos e locações.  
O projeto registra reservas, calcula períodos de locação e permite relatórios por modelo e duração.

O sistema possibilita o controle completo do ciclo de locação, desde o cadastro de clientes e veículos até o registro das reservas feitas pelos funcionários.  
Cada locação armazena quem alugou, qual carro foi alugado, quem realizou o atendimento e as datas de início e término da reserva.

## Relatórios Disponíveis
- Locações por modelo de veículo  
- Duração média das locações  
- Histórico de clientes e atendimentos  

## Estrutura do Banco de Dados
O banco de dados é composto por quatro entidades principais:

- **CLIENTE**: Guarda as informações dos clientes cadastrados.  
- **FUNCIONARIO**: Armazena dados dos funcionários responsáveis pelos atendimentos.  
- **CARRO**: Registra os veículos disponíveis para locação.  
- **LOCACAO**: Registra cada reserva efetuada, relacionando cliente, carro e funcionário.  

## Banco de Dados
- Banco utilizado: MySQL  
- Scripts disponíveis em: [SQL](.src/sql)  

## Relacionamentos
- Cliente → Locação: um cliente pode realizar várias locações (1:N)  
- Carro → Locação: um carro pode estar em várias locações ao longo do tempo (1:N)  
- Funcionário → Locação: um funcionário pode registrar várias locações (1:N)  

## Diagrama Entidade-Relacionamento (ER)
O sistema possui quatro entidades principais: Cliente, Funcionário, Carro e Locação.  
Cada locação conecta um cliente, um carro e um funcionário.

erDiagram
    CLIENTE ||--o{ LOCACAO : "realiza"
    FUNCIONARIO ||--o{ LOCACAO : "registra"
    CARRO ||--o{ LOCACAO : "é alugado em"
    
Arquivo do diagrama: [diagrama.mmd](./diagrams/diagrama.mmd)

## Tecnologias Utilizadas
>Python;
>MySQL;
>Mermaid (para o diagrama ER);
>GitHub.

## Como Executar o Projeto:

1. Clone o repositório:
git clone https://github.com/seu-usuario/sistema-locacao-veiculos.git

2. Acesse a pasta do projeto:
cd (sistema-locacao-veiculos)

3. Crie as tabelas:
[Executar create_tables_and_records.py](./src/create_tables_and_records.py)

4. Execute o sistema:
[Executar principal.py](./src/principal.py)

## Autores:
Emanoel Vitor Atanazio Ventura;
Felipe Rodrigues Barzilai;
João Emanoel Justino;
Rogeres José Prates da Silva;
Livia Favato Bastos Neves.












