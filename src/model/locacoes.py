from datetime import date
from model.clientes import Cliente
from model.carros import Carro
from model.funcionarios import Funcionario

class Locacao:
    def __init__(self,
                 numero_reserva:int=None,
                 data_inicio:date=None,
                 data_fim:date=None,
                 cliente:Cliente=None,
                 carro:Carro=None,
                 funcionario:Funcionario=None
                 ):
       self.set_numero_reserva(numero_reserva)
       self.set_data_inicio(data_inicio)
       self.set_data_fim(data_fim)
       self.set_cliente(cliente)
       self.set_carro(carro)
       self.set_funcionario(funcionario)

    def set_numero_reserva(self, numero_reserva:int):
        self.numero_reserva = numero_reserva

    def set_data_inicio(self, data_inicio: date):
        self.data_inicio = data_inicio
    
    def set_data_fim(self, data_fim: date):
        self.data_fim = data_fim

    def set_cliente(self, cliente: Cliente):
        self.cliente = cliente

    def set_carro(self, carro: Carro):
        self.carro = carro 
    
    def set_funcionario(self, funcionario: Funcionario):
        self.funcionario = funcionario 

    def get_numero_reserva(self) -> int:
        return self.numero_reserva
    
    def get_data_inicio(self) -> date:
        return self.data_inicio
    
    def get_data_fim(self) -> date:
        return self.data_fim
    
    def get_cliente(self) -> Cliente:
        return self.cliente
    
    def get_carro(self) -> Carro:
        return self.carro
    
    def get_funcionario(self) -> Funcionario:
        return self.funcionario

    def to_string(self) -> str:
        return f"Reserva: {self.get_numero_reserva()} | Início: {self.get_data_inicio()} | Fim: {self.get_data_fim()} | CPF: {self.get_cliente().get_cpf()} | ID Carro: {self.get_carro().get_id_carro()} | ID Funcionario: {self.get_funcionario().get_id_funcionario()}"