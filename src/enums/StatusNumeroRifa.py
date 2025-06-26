import enum

class StatusNumeroRifa(int, enum.Enum):
    DISPONIVEL = 1
    RESERVADO = 2
    PAGO = 3