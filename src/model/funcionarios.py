class Funcionario:
    def __init__(self,
                 id_funcionario:int=None,
                 nome:str=None,
                 cargo:str=None
                ):
        self.set_id_funcionario(id_funcionario)
        self.set_nome(nome)
        self.set_cargo(cargo)

    def set_id_funcionario(self, id_funcionario:int):
        self.id_funcionario = id_funcionario
    
    def set_nome(self, nome:str):
        self.nome = nome

    def set_cargo(self, cargo:str):
        self.cargo = cargo

    def get_id_funcionario(self) -> int:
        return self.id_funcionario
    
    def get_nome(self) -> str:
        return self.nome
    
    def get_cargo(self) -> str:
        return self.cargo
    
    def to_string(self):
        return f"ID Funcionário: {self.get_id_funcionario()} | Nome: {self.get_nome()} | Cargo: {self.get_cargo()}"
