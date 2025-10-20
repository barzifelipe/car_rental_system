class Cliente:
    def __init__(self,
                cpf:str=None,
                nome:str=None,
                cnh:str=None
                ):
        self.set_cpf(cpf)
        self.set_nome(nome)
        self.set_cnh(cnh)
    
    def set_cpf(self, cpf:str):
        self.cpf = cpf
    
    def set_nome(self, nome:str):
        self.nome = nome

    def set_cnh(self, cnh:str):
        self.cnh = cnh

    def get_cpf(self) -> str:
        return self.cpf
    
    def get_nome(self) -> str:
        return self.nome

    def get_cnh(self) -> str:
        return self.cnh
    
    def to_string(self) -> str:
        return f"CPF: {self.get_cpf()} | Nome: {self.get_nome()} | CNH: {self.get_cnh()}"