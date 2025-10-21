class Cliente:
    def __init__(self,
                 id_cliente: int = None,
                 nome_cliente: str = None,
                 cpf: str = None
                ):
        self.set_id_cliente(id_cliente)
        self.set_nome_cliente(nome_cliente)
        self.set_cpf(cpf)

    def set_id_cliente(self, id_cliente: int):
        self.id_cliente = id_cliente
    
    def set_nome_cliente(self, nome_cliente: str):
        self.nome_cliente = nome_cliente

    def set_cpf(self, cpf: str):
        self.cpf = cpf

    def get_id_cliente(self) -> int:
        return self.id_cliente
    
    def get_nome_cliente(self) -> str:
        return self.nome_cliente
    
    def get_cpf(self) -> str:
        return self.cpf
    
    def to_string(self):
        return f"ID Cliente: {self.get_id_cliente()} | Nome: {self.get_nome_cliente()} | CPF: {self.get_cpf()}"
