class Carro:
    def __init__(self,
                 id_carro:str=None,
                 modelo:str=None,
                 placa:str=None,
                 categoria:str=None,
                 valor_diaria:float=None
                 ):
        self.set_id_carro(id_carro)
        self.set_modelo(modelo)
        self.set_placa(placa)
        self.set_categoria(categoria)
        self.set_valor_diaria(valor_diaria)

    def set_id_carro(self, id_carro:str):
        self.id_carro = id_carro
    
    def set_modelo(self, modelo:str):
        self.modelo = modelo

    def set_placa(self, placa:str):
        self.placa = placa
    
    def set_categoria(self, categoria:str):
        self.categoria = categoria

    def set_valor_diaria(self, valor_diaria:float):
        self.set_valor_diaria = valor_diaria

    def get_id_carro(self) -> str:
        return self.id_carro
    
    def get_modelo(self) -> str:
        return self.modelo
    
    def get_placa(self) -> str:
        return self.placa
    
    def get_categoria(self) -> str:
        return self.categoria
    
    def get_valor_diaria(self) -> float:
        return self.valor_diaria
    
    def to_string(self):
        return f"ID Carro: {self.get_id_carro()} | Modelo: {self.get_modelo()} | Placa: {self.get_placa()} | Categoria: {self.get_categoria()} | Valor da diária: {self.get_valor_diaria()}"
