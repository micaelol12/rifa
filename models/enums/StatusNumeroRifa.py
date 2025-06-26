import enum

class StatusNumeroRifa(str, enum.Enum):
    DISPONIVEL = 1
    RESERVADO = 2
    PAGO = 3