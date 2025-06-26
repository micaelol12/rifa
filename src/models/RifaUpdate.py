from pydantic import BaseModel
from typing import List
import datetime
from .NumeroRifa import NumeroRifaModel


class RifaUpdateModel(BaseModel):
    name: str
    description: str
    numeros: List[NumeroRifaModel] = []
    data_criacao: datetime.datetime