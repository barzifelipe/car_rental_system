class Cliente:
    def __init__(self,
                CPF:str=None,
                nome:str=None,
                CNH:str=None
                ):
        self.set_CPF(CPF)
        self.set_nome(nome)
        self.set_CNH(CNH)
    
    def set_CPF(self, CPF:str):
        self.CPF = CPF
    
    def set_nome(self, nome:str):
        self.nome = nome

    def set_CNH(self, CNH:str):
        self.CNH = CNH

    def get_CPF(self) -> str:
        return self.CPF
    
    def get_nome(self) -> str:
        return self.nome

    def get_CNH(self) -> str:
        return self.CNH
    
    def to_string(self) -> str:
        return f"CPF: {self.get_CPF()} | Nome: {self.get_nome()} | CNH: {self.get_CNH()}"