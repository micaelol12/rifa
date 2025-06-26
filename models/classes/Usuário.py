class Usuario():
    def __init__(self, nome, email):
        self.nome:str = nome
        self.email:str = email
        self.telefone: int

    def __str__(self):
        return f"Usuário: {self.nome}, Email: {self.email}"