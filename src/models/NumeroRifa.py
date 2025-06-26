from .Usuario import UsuarioModel
from src.enums import StatusNumeroRifa
from pydantic import BaseModel
from typing import  Optional

class NumeroRifaModel(BaseModel):
    numero: int
    status: StatusNumeroRifa
    usuario: Optional[UsuarioModel] = None

    @classmethod
    def from_create(cls, num: int):
        return cls(
                numero=num,
                status=StatusNumeroRifa.DISPONIVEL
        )
        