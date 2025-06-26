from models.classes.Usuário import Usuario
from models.enums.StatusNumeroRifa import StatusNumeroRifa

class NumeroRifa():
    def __init__(self, numero: int):
        self.numero:int = numero
        self.status: StatusNumeroRifa = StatusNumeroRifa.DISPONIVEL
        self.usuario:Usuario = None

    def __str__(self):
        return f"NumeroRifa(numero={self.numero}, vendido={self.vendido})"